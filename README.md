# NASA Crew Health Console (with MedGemma-4B-IT)

An autonomous medical and clinical monitoring console designed for astronauts on long-duration spaceflight missions (International Space Station, Deep-Space Transit, Lunar Surface, and Mars Surface). 

The system couples an interactive clinical dashboard with an AI-powered diagnostic backend using Google's **MedGemma-4B-IT** multimodal medical model.

---

## Key Capabilities

1. **Interactive Anatomical Body Map**: Visual representation of astronaut organ systems (brain, heart, lungs, abdomen, arms, hands, legs) highlighting critical (red) and elevated (yellow) spaceflight risks.
2. **NASA HRP Clinical Assessment Domains**:
   - **Behavioral Health & Performance**: Sleep-wake rhythm tracking, mood, cognitive fatigue, and circadian screen dimming.
   - **Biochemical & Fluid Shift**: Microgravity cephalad fluid shifts, hydration, and renal stone risk monitoring.
   - **Immune Dysregulation & Dermatology**: Multimodal image inspection for rashes, hives, and latent virus reactivation (EBV, VZV).
   - **Cardiovascular & Neuro-Ocular (SANS)**: Real-time simulated ECG, blood pressure tracking, and SANS (Spaceflight-Associated Neuro-Ocular Syndrome) screening.
   - **Sensorimotor & Vestibular Adaptation**: Space Motion Sickness (SMS) triage and EVA readiness scoring.
   - **Cabin Environmental Telemetry**: Real-time cabin air monitoring (CO₂, O₂, pressure, particulate matter, and radiation) mapped to affected anatomical regions.
3. **Emergency Escalation Protocol**: Automatic alerts dispatched to Flight Surgeons, Crew Medical Officers, and Flight Directors upon critical vitals or symptoms.

---

## Architecture Overview

- **Frontend**: Single-page application in clean HTML5, CSS3, and JavaScript (`Crew Health Console.html`) with zero external CDN dependencies.
- **Backend**: FastAPI service (`medgemma_server.py`) handling telemetry, multimodal photographic inputs, mission profile context, and clinical inference.
- **Medical Model**: Google's **`google/medgemma-4b-it`** (Gemma 3 multimodal instruction-tuned medical architecture).
- **Graceful Fallback**: Implements high-fidelity spaceflight triage out of the box, with seamless transition to neural model weights once Hugging Face credentials are authenticated.

---

## Quick Start

### 1. Prerequisites
- Python 3.10+ (64-bit)
- Modern web browser (Chrome, Edge, Firefox, or Safari)

### 2. Installation
Clone the repository and install the Python dependencies:

```bash
git clone https://github.com/your-username/nasa-crew-health-console.git
cd nasa-crew-health-console
pip install -r requirements.txt
```

### 3. Start the Backend
```bash
python medgemma_server.py
```
The server will start on `http://127.0.0.1:8000`.

### 4. Open the Console
Open `Crew Health Console.html` directly in your browser, or serve it using any local static file server:

```bash
# Optional: using Python's built-in HTTP server
python -m http.server 3000
```
Then navigate to: `http://localhost:3000/Crew Health Console.html`

---

## Enabling Live Neural Weights (google/medgemma-4b-it)

Because `google/medgemma-4b-it` is a gated medical model under the Health AI Developer Foundations (HAI-DEF) license:

1. Log in to your account at [Hugging Face](https://huggingface.co).
2. Visit the model repository and accept the license terms: [google/medgemma-4b-it](https://huggingface.co/google/medgemma-4b-it).
3. Create an Access Token under **Settings -> Access Tokens**.
4. Configure your token:
   - Copy `.env.example` to `.env`:
     ```bash
     cp .env.example .env
     ```
   - Add your token inside `.env`:
     ```env
     HF_TOKEN=hf_your_token_here
     ```
5. Restart `medgemma_server.py`. The weights (~8.6 GB) will automatically download and map into memory.

---

## Security Note

Never commit your `.env` file or Hugging Face access token to a public repository. The `.gitignore` file included in this repository prevents secret leakage.
