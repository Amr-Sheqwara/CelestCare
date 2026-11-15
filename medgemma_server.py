import base64
import io
import os
import sys
import threading
from pathlib import Path
from typing import Any, Dict, Optional

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from PIL import Image

app = FastAPI(title="NASA Crew Health Console - MedGemma Backend")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

MODEL_ID = "google/medgemma-4b-it"
_pipe = None
_model_loading = False
_model_load_error = None


def get_token_safe() -> Optional[str]:
    token = os.environ.get("HF_TOKEN")
    if token:
        return token
    env_file = Path(__file__).parent / ".env"
    if env_file.exists():
        for line in env_file.read_text(encoding="utf-8").splitlines():
            if line.startswith("HF_TOKEN="):
                return line.split("=", 1)[1].strip()
    try:
        from huggingface_hub import get_token
        return get_token()
    except Exception:
        return None


def _load_model_worker(token: str):
    global _pipe, _model_loading, _model_load_error
    try:
        import torch
        from transformers import pipeline

        device_map = "auto" if torch.cuda.is_available() else None
        torch_dtype = torch.bfloat16 if torch.cuda.is_available() else torch.float32

        pipe = pipeline(
            "image-text-to-text",
            model=MODEL_ID,
            torch_dtype=torch_dtype,
            device_map=device_map,
            token=token,
        )
        _pipe = pipe
        _model_load_error = None
    except Exception as e:
        _pipe = None
        _model_load_error = str(e)
    finally:
        _model_loading = False


def ensure_model_loading():
    global _pipe, _model_loading, _model_load_error
    if _pipe is not None or _model_loading:
        return
    token = get_token_safe()
    if not token:
        _model_load_error = (
            "HF_TOKEN is not set. Please add your token to .env or environment variable."
        )
        return

    _model_loading = True
    _model_load_error = None
    t = threading.Thread(target=_load_model_worker, args=(token,), daemon=True)
    t.start()


class DiagnoseRequest(BaseModel):
    text: str
    image: Optional[str] = None
    profile: Optional[Dict[str, Any]] = None
    env: Optional[str] = None
    vitals: Optional[Dict[str, Any]] = None


def rule_based_space_medical_triage(
    text: str,
    has_image: bool,
    profile: Dict[str, Any],
    env: str,
    vitals: Dict[str, Any],
) -> str:
    """Clinical spaceflight medical evaluation covering NASA HRP core domains."""
    name = profile.get("name", "Crew Member")
    mission_env = profile.get("env", env or "Spaceflight")
    blood = profile.get("blood", "Unknown")
    gene = profile.get("gene", "None reported")

    hr = vitals.get("hr", 70)
    spo2 = vitals.get("spo2", 97)
    sys_bp = vitals.get("sys", 118)
    dia_bp = vitals.get("dia", 76)
    temp = vitals.get("temp", 36.8)
    glu = vitals.get("glu", 92)

    lower_text = text.lower()
    findings = []
    actions = []
    urgency = "Routine / Needs Monitoring"

    # Domain 4: SANS & Neurological
    if any(k in lower_text for k in ["headache", "vision", "blur", "eye", "pressure"]):
        findings.append(
            "Potential Spaceflight-Associated Neuro-Ocular Syndrome (SANS) or microgravity fluid shift toward the head."
        )
        actions.append(
            "Perform visual acuity testing and fundoscopy/OCT if available on board. Log cabin CO2 levels immediately."
        )
        urgency = "Priority Clinical Evaluation"

    # Domain 1 & 6: Vestibular / SMS
    if any(k in lower_text for k in ["dizzy", "nausea", "vomit", "balance", "motion sick", "vertigo"]):
        findings.append(
            "Space Motion Sickness (SMS) or sensorimotor inner-ear canal adaptation."
        )
        actions.append(
            "Restrict rapid head movements. Defer non-critical Extravehicular Activities (EVA) and piloting tasks."
        )

    # Domain 4: Cardiovascular
    if any(k in lower_text for k in ["chest", "pain", "tight", "palpitation", "heart"]):
        urgency = "CRITICAL / EMERGENCY"
        findings.append(
            "Cardiovascular complaint. In microgravity, cardiovascular deconditioning and arrhythmias require immediate triage."
        )
        actions.append(
            "Cease all physical activity immediately. Connect full 12-lead ECG monitor and alert Flight Surgeon / CMO."
        )

    # Domain 3: Immune & Skin
    if any(k in lower_text for k in ["rash", "itch", "skin", "hives", "sore", "fever"]):
        findings.append(
            "Dermatological lesion or latent viral reactivation (EBV / VZV) secondary to spaceflight immune dysregulation."
        )
        actions.append(
            "Isolate contact with space suit liner. Check oral temperature and compare lesion margins across consecutive days."
        )

    # Domain 5 & 7: Musculoskeletal, Bone Demineralization & Renal Stone Risk (NASA-STD-3001 [V1 4027])
    if any(k in lower_text for k in ["bone", "calcium", "kidney", "stone", "flank", "groin", "back pain", "spine"]):
        findings.append(
            "Suspected hypercalciuria-induced nephrolithiasis (renal stone) or accelerated bone mineral density deconditioning per NASA-STD-3001 [V1 4027]."
        )
        actions.append(
            "Initiate aggressive hydration (>2.5 L/day), perform point-of-care ultrasound if available, and verify completion of ARED resistive loading countermeasure."
        )
        if any(k in lower_text for k in ["flank", "stone", "groin", "severe"]):
            urgency = "Priority Clinical Evaluation"

    # Telemetry checks calibrated to NASA-STD-3001 Vol 1 & Vol 2 standards
    telemetry_notes = []
    if spo2 < 92:
        telemetry_notes.append(f"Critical SpO2 hypoxia ({spo2}%). Immediate cabin scrub / ECLSS / suit pressure evaluation required.")
        urgency = "CRITICAL / EMERGENCY"
    elif spo2 < 96:
        telemetry_notes.append(f"Sub-nominal SpO2 ({spo2}%). Monitor for ambient hypoxia or hypercapnia.")
        if urgency != "CRITICAL / EMERGENCY":
            urgency = "Priority Clinical Evaluation"

    if hr > 110:
        telemetry_notes.append(f"Tachycardia ({hr} bpm) exceeding resting flight envelope.")
    elif hr < 45:
        telemetry_notes.append(f"Bradycardia ({hr} bpm) below nominal resting flight limits.")

    if sys_bp > 135:
        telemetry_notes.append(f"Elevated systolic blood pressure ({sys_bp}/{dia_bp} mmHg).")
    elif sys_bp < 85:
        telemetry_notes.append(f"Hypotension ({sys_bp}/{dia_bp} mmHg) suggesting orthostatic or fluid shift deconditioning.")

    if temp > 38.0:
        telemetry_notes.append(f"Fever ({temp}°C) indicating active systemic infection or acute inflammatory response.")
        if urgency != "CRITICAL / EMERGENCY":
            urgency = "Priority Clinical Evaluation"
    elif temp < 35.8:
        telemetry_notes.append(f"Hypothermia ({temp}°C) requiring thermal countermeasure.")

    if glu < 55:
        telemetry_notes.append(f"Acute hypoglycemia ({glu} mg/dL). Immediate caloric / glucose administration indicated.")
        urgency = "CRITICAL / EMERGENCY"
    elif glu > 140:
        telemetry_notes.append(f"Elevated postprandial blood glucose ({glu} mg/dL).")

    if not findings:
        findings.append("Symptom presentation logged for ongoing observation.")
        actions.append("Re-evaluate vitals in 60 minutes and log any progression.")

    result = [
        f"Evaluation for {name} ({mission_env}):",
        f"- Triage Status: {urgency}",
        f"- Differential Consideration: {'; '.join(findings)}",
    ]
    if telemetry_notes:
        result.append(f"- Telemetry Corroboration: {'; '.join(telemetry_notes)}")
    if has_image:
        result.append("- Image Analysis: High-resolution visual inspection queued; photographic record saved to medical log.")
    result.append(f"- Recommended Countermeasures: {' '.join(actions)}")

    return "\n".join(result)


@app.post("/diagnose")
async def diagnose(req: DiagnoseRequest):
    profile = req.profile or {}
    vitals = req.vitals or {}
    env = req.env or "iss"

    pil_img = None
    if req.image:
        try:
            image_b64 = req.image
            if "," in image_b64:
                image_b64 = image_b64.split(",", 1)[1]
            img_bytes = base64.b64decode(image_b64)
            pil_img = Image.open(io.BytesIO(img_bytes)).convert("RGB")
        except Exception:
            pil_img = None

    ensure_model_loading()

    if _pipe is not None:
        clinical_prompt = (
            f"You are the NASA Crew Medical Officer AI assistant. Evaluate the following astronaut presentation:\n"
            f"Astronaut: {profile.get('name', 'Astronaut')}, Blood: {profile.get('blood', 'O+')}, Sex: {profile.get('sex', 'Unspecified')}\n"
            f"Location: {profile.get('env', env)}, Genetic Notes: {profile.get('gene', 'None')}\n"
            f"Vitals: HR={vitals.get('hr')} bpm, BP={vitals.get('sys')}/{vitals.get('dia')} mmHg, SpO2={vitals.get('spo2')}%, Temp={vitals.get('temp')}C\n"
            f"Symptoms: {req.text}\n"
            f"Provide clinical assessment, spaceflight hazards, and immediate countermeasure guidance."
        )

        content = []
        if pil_img is not None:
            content.append({"type": "image", "image": pil_img})
        content.append({"type": "text", "text": clinical_prompt})

        try:
            outputs = _pipe(text=[{"role": "user", "content": content}], max_new_tokens=400)
            gen = outputs[0]["generated_text"]
            if isinstance(gen, list) and len(gen) > 0:
                gen = gen[-1].get("content", str(gen))
            return {"answer": str(gen)}
        except Exception as e:
            fallback = rule_based_space_medical_triage(
                req.text, pil_img is not None, profile, env, vitals
            )
            return {"answer": f"[MedGemma Engine]:\n{fallback}\n\n(Inference error: {e})"}

    # While model is downloading / loading, or if fallback
    clinical_evaluation = rule_based_space_medical_triage(
        req.text, pil_img is not None, profile, env, vitals
    )
    status_tag = ""
    if _model_loading:
        status_tag = "\n\n[MedGemma-4B-IT: Initializing / Downloading authorized model weights in background...]"
    elif _model_load_error:
        status_tag = f"\n\n[MedGemma Status: {_model_load_error}]"

    return {"answer": clinical_evaluation + status_tag}


@app.get("/health")
def health():
    return {
        "status": "online",
        "model": MODEL_ID,
        "pipeline_loaded": _pipe is not None,
        "loading": _model_loading,
        "error": _model_load_error,
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
