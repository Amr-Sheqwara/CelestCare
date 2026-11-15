# NASA Crew Health Console (with MedGemma-4B-IT)

An autonomous medical, physiological, and clinical monitoring console designed for astronauts on long-duration spaceflight missions across the International Space Station (ISS), Deep-Space Transit, Lunar Surface, and Mars Surface.

The system connects an interactive single-page mission operations dashboard with a dedicated AI clinical backend powered by Google's **MedGemma-4B-IT** multimodal foundation model.

---

## Complete Project Requirements & Specifications (Points 1–16)

All 16 core points from the mission specification document are fully implemented:

1. **Mission Environment & Multimodal AI Scope**: Configured for astronauts on Spaceflight, ISS, Lunar Base/Rover, and Mars Base/Rover. Uses multimodal medical AI processing both natural language descriptions and clinical photographic inputs alongside physiological and environmental sensor feeds.
2. **Personalized Astronaut Profile**: System personalizes all baseline metrics according to individual astronaut parameters: Full Name, Blood Type (A, B, AB, O ±), Biological Sex, Genetic Predispositions/Family History, and current Mission Location.
3. **Interactive Anatomical Body Map**: Vectorized clickable human body figure mapping key anatomical zones (Brain, Heart, Lungs, Abdomen, Arms, Hands, Legs & Spine) to spaceflight pathologies and risks.
4. **Symptom Reporting System**: Dual input interface allowing crew members to enter descriptive clinical text and attach high-resolution clinical photographs (e.g. skin lesions, ocular changes).
5. **Daily Multi-Factor Health Check-ins**: 1-to-5 point scale assessments for Mood, Stress/Anxiety, Sleep Duration (hours), Hydration (liters), Meal Frequency, and behavioral isolation indicators.
6. **Medical Diagnostic Equipment Telemetry**: Dedicated telemetry recording for standard spaceflight medical hardware: Blood Pressure (Systolic & Diastolic mmHg), Blood Glucose (mg/dL), Blood Oxygen (SpO₂ %), Heart Rate (bpm), and Core Body Temperature (°C).
7. **Routine Protocols & Exercise Countermeasures**: Automated scheduling and step-by-step clinical guidance for measurement protocols, enforcing the mandatory 2-hour daily resistive and aerobic exercise plan (ARED / Treadmill / Cycle Ergometer).
8. **Visual Triage & Severity Alert System**: Real-time visual feedback on the anatomical body map. Vital organs (**Heart, Lungs, Brain**) pulse in **red** for critical emergencies requiring immediate intervention. Secondary structures (**Abdomen, Arms, Hands, Legs**) pulse in **yellow** for strain, motion sickness, or musculoskeletal stress.
9. **Automated Trend & Health Record Logging**: Continuous trend monitoring that flags behavioral health shifts, chronic sleep deprivation, or physical deconditioning, recording persistent alerts in the medical log.
10. **Emergency Notification Broadcast**: Critical symptoms or dangerous diagnoses trigger automated emergency dispatch with UTC timestamps to:
    - Flight Surgeon
    - Crew Medical Officer (CMO)
    - Spacecraft / ISS Commander
    - Flight Director
11. **Longitudinal Historical Charts**: Real-time vector SVG trend graphs displaying 12-day historical performance against standard reference bands for all vital signs, sleep, mood, and hydration.
12. **Backend Medical Server**: Production-grade FastAPI service (`medgemma_server.py`) operating on port 8000 with Cross-Origin Resource Sharing (CORS) enabled for seamless browser console communication.
13. **MedGemma-4B-IT Neural Integration**: Direct integration with Google's instruction-tuned multimodal medical model (`google/medgemma-4b-it`) via Hugging Face Transformers and Accelerate, providing simultaneous visual and clinical text reasoning.
14. **NASA HRP Core Clinical Domains**: Comprehensive coverage of the 8 Human Research Program disciplines:
    - *Behavioral Health & Performance*: Circadian alignment and cognitive fatigue tracking.
    - *Biochemical Markers & Fluids*: Microgravity cephalad fluid shifts and renal stone risk.
    - *Immune Dysregulation & Dermatology*: Latent viral reactivation (EBV/VZV) and rash inspection.
    - *Cardiovascular & Neuro-Ocular (SANS)*: Carotid deconditioning, resting ECG, and SANS screening.
    - *Microbiome & Nutrition*: Caloric and fluid deficit tracking.
    - *Sensorimotor & Vestibular Adaptation*: Space Motion Sickness (SMS) triage.
    - *Musculoskeletal Performance*: Body mass and bone/muscle atrophy mitigation.
    - *Cabin Life Support & Radiation*: Real-time cabin air tracking (CO₂, O₂, pressure, PM2.5, radiation).
15. **Resilient Dual-Mode Architecture**: Automated graceful degradation: executes live neural weights when authenticated, and falls back to a deterministic rule-based spaceflight triage engine if weights are pending, ensuring 100% console uptime.
16. **Production & Repository Security**: Full Git repository configuration with strict secret isolation (`.gitignore`, `.env.example`, `requirements.txt`) safeguarding astronaut telemetry and credentials.

---

## System Architecture

The solution uses a clean separation between the mission interface and the clinical reasoning backend:

- **Frontend Console (`Crew Health Console.html`)**: Single-page application built with clean HTML5, CSS3, and JavaScript with zero external CDN dependencies. Features light mode, dark mode, and a specialized red-amber circadian sleep mode with night dimming.
- **Backend Service (`medgemma_server.py`)**: Asynchronous FastAPI service handling preflight CORS, payload validation via Pydantic, base64 image decoding, and model inference.
- **Model Engine (`google/medgemma-4b-it`)**: Google's Gemma 3 multimodal architecture utilizing SigLIP vision encoding and bfloat16 precision.

---

## Project Structure

```text
├── Crew Health Console.html    # Interactive frontend console application
├── medgemma_server.py          # FastAPI backend server with MedGemma-4B-IT integration
├── requirements.txt            # Python dependencies
├── .env.example                # Safe environment variable template for HF_TOKEN
├── .gitignore                  # Prevents committing credentials, caches, and .env
├── README.md                   # Complete documentation and operational guide
└── Login, so the system...pdf  # Full project specification document
```

---

## Quick Start Guide

### Step 1: Install Dependencies
Ensure you have Python 3.10+ installed, then run:

```bash
pip install -r requirements.txt
```

### Step 2: Start the Backend Server
Run the FastAPI backend:

```bash
python medgemma_server.py
```
The server will start listening on `http://127.0.0.1:8000`.

### Step 3: Launch the Console
Open `Crew Health Console.html` directly in your browser, or serve it locally:

```bash
python -m http.server 3000
```
Then navigate to `http://localhost:3000/Crew Health Console.html`.

---

## Enabling Neural Model Weights (google/medgemma-4b-it)

Because `google/medgemma-4b-it` is a gated medical foundation model:

1. Log in to [Hugging Face](https://huggingface.co).
2. Visit the model page and accept the license terms: [google/medgemma-4b-it](https://huggingface.co/google/medgemma-4b-it).
3. Generate a User Access Token under **Settings -> Access Tokens**.
4. Create your `.env` file from the example template:
   ```bash
   cp .env.example .env
   ```
5. Add your token to `.env`:
   ```text
   HF_TOKEN=hf_your_token_here
   ```
6. Start `medgemma_server.py`. The weights (~8.6 GB) will automatically download and map into memory.

---

## Security and Secret Protection

Never commit your `.env` file or personal Hugging Face access token to a public repository. The included `.gitignore` file strictly excludes `.env` and local model caches.
