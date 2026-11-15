# NASA Crew Health Console (with MedGemma-4B-IT)

An autonomous medical, physiological, and clinical monitoring console designed for astronauts on long-duration spaceflight missions (International Space Station, Deep-Space Transit, Lunar Surface, and Mars Surface).

The system pairs an interactive single-page mission operations dashboard with a dedicated AI clinical backend powered by Google's **MedGemma-4B-IT** multimodal foundation model.

---

## Complete Feature Matrix (Specification & Implementation)

Every requirement specified in the project documentation has been fully implemented:

### 1. Astronaut Mission Profiles & Personalized Login
- **Target Environments**: Configured for low-Earth orbit (ISS), deep-space transit, Lunar base (0.166 g), Lunar rover, Mars base (0.38 g), and Mars rover.
- **Personalized Baselines**: Incorporates astronaut blood type (A, B, AB, O ±), biological sex, and specific genetic markers/family history notes to calibrate physiological interpretation and expected ranges.

### 2. Interactive Anatomical Body Map
- **Visual SVG Body Figure**: Fully interactive, vectorized anatomical representation of the human body.
- **Organ-Specific Pathologies**: Clicking on any anatomical zone (Brain, Heart, Lungs, Abdomen, Arms, Hands, Legs & Spine) displays spaceflight-specific adaptations, pathologies, and risks.

### 3. Visual Triage & Severity Alert System
- **Dual-Priority Color Coding**:
  - **Pulsing Red**: Essential vital organs (Brain, Heart, Lungs) indicating critical or life-threatening compromise requiring immediate intervention.
  - **Pulsing Yellow**: Secondary priority structures (Abdomen, Arms, Hands, Legs & Spine) indicating strain, motion sickness, or musculoskeletal stress requiring attention.
- **Live Heart Animation**: Cardiac rate dynamically scales with astronaut pulse telemetry.

### 4. Multimodal Problem & Symptom Reporting
- **Free-Text Clinical Description**: Natural language input describing pain, sensations, and duration.
- **Severity Rating**: 1 to 5 scale calibrated against NASA medical severity metrics.
- **Photographic Inspection**: Upload capability for skin lesions, glove injuries, and ocular changes, formatted for multimodal neural processing.

### 5. Daily Health & Behavioral Check-in
- **Mental & Cognitive Health**: Quantified Mood (1–5) and Stress/Anxiety (1–5) tracking.
- **Sleep Architecture**: Recorded sleep duration with automatic circadian deficit alerts.
- **Nutrition & Hydration**: Daily fluid intake (liters) and meal count logging to guard against bone mineral deconditioning and renal stone formation.
- **Crew Dynamics Checkboxes**: Behavioral markers including isolation feelings, interpersonal friction, and cognitive focus lapses.

### 6. Medical Hardware & Wearable Telemetry
- **Standard Spaceflight Vitals**:
  - Heart Rate (bpm) with animated rhythm strip (ECG).
  - Blood Oxygen Saturation (SpO₂ %).
  - Blood Pressure (Systolic and Diastolic mmHg).
  - Blood Glucose (mg/dL).
  - Core Body Temperature (°C).
- **Environment-Aware Baselines**: Physiological standard bands automatically adjust for microgravity (e.g. lower blood pressure and higher resting core temperature on ISS).

### 7. Routine Protocols & Exercise Guidance
- **Daily Task Tracker**: Live checklist tracking completion of check-ins, measurements, and exercise.
- **NASA Measurement Instructions**: Accordion guides detailing standard operating procedures for blood pressure cuffs, pulse oximetry, glucometers, and ear thermometers.
- **Countermeasure Enforcement**: Daily exercise tracking enforcing the mandatory 2-hour aerobic and resistive workout plan (ARED / T2 Treadmill / Cycle Ergometer).

### 8. Emergency Escalation Protocol
- **Automated Broadcast**: Severe symptoms (chest pain, respiratory arrest, decompression sickness, collapse) instantly trigger the emergency state.
- **Command Notification**: Logs automatic timestamps and dispatches alerts to:
  - Flight Surgeon
  - Crew Medical Officer (CMO)
  - Spacecraft / ISS Commander
  - Flight Director

### 9. Longitudinal Trend Analytics
- **Historical SVG Charts**: Interactive time-series visualizers displaying 12-day historical curves against safe clinical baseline bands for all vitals, sleep, mood, and hydration.

### 10. Live Cabin & Suit Life-Support Sensors
- **Multi-Zone Sensor Telemetry**: Simulated 3-second live sensor feeds across vehicle compartments (Crew quarters, Laboratory, Galley, Airlock, Command deck, and EVA Space Suit).
- **Environmental Hazard Tracking**: Real-time monitoring of CO₂, O₂, cabin pressure, temperature, humidity, particulate matter (PM2.5), carbon monoxide, and cosmic radiation (µSv/h).
- **Hazard Simulations**: Test buttons for realistic emergency events (CO₂ scrub failure, smoke, hull pressure leaks, solar particle events).

### 11. Circadian Sleep Mode
- **Spectrally Dimmable UI**: Transitions the entire console into a dark red-amber palette with customizable night overlay dimming to preserve astronaut melatonin production.
- **Emergency Wake Feature**: Any critical sensor or vital alert automatically disengages sleep mode and illuminates the screen.

### 12. NASA Human Research Program (HRP) Core Domains
Systematically addresses the 8 clinical disciplines recognized by NASA HRP:
1. *Behavioral Health & Performance* (circadian alignment, cognitive vigilance).
2. *Biochemical Markers & Fluids* (cephalad fluid redistribution, electrolyte shifts).
3. *Immunity & Cellular Health* (latent viral reactivation, skin barrier degradation).
4. *Cardiovascular & Neuro-Ocular (SANS)* (intracranial pressure shifts, ophthalmic flattening).
5. *Microbiome & Gastrointestinal* (gut dysbiosis, space motion sickness).
6. *Sensorimotor & Vestibular Adaptation* (otolith canal discordance, post-flight ataxia).
7. *Musculoskeletal Performance* (bone mineral loss, body mass monitoring).
8. *Hostile Environment & Radiation* (deep-space galactic cosmic rays, cabin particulate toxicity).

---

## AI Medical Backend (MedGemma-4B-IT)

The console is powered by a dedicated Python FastAPI backend (`medgemma_server.py`) integrating Google's **`google/medgemma-4b-it`**:

- **Model Architecture**: Gemma 3 multimodal instruction-tuned vision-language model combined with SigLIP image encoding.
- **Multimodal Evaluation**: Synthesizes the astronaut's symptom text, uploaded image, mission profile, mission environment, and current telemetry into a unified clinical prompt.
- **Dual-Mode Graceful Fallback**:
  - **Live Neural Weights**: Runs GPU/CPU inference with `torch.bfloat16` and `accelerate` when authenticated with a Hugging Face token.
  - **Deterministic Clinical Engine**: If weights are offline or downloading, an automated rule-based spaceflight triage engine provides uninterrupted clinical evaluation.
- **Cross-Origin Resource Sharing (CORS)**: Pre-configured on port 8000 for browser security compliance.

---

## Project Structure

```text
├── Crew Health Console.html    # Interactive frontend console application
├── medgemma_server.py          # FastAPI backend server with MedGemma-4B-IT integration
├── requirements.txt            # Python dependencies
├── .env.example                # Safe environment variable template for HF_TOKEN
├── .gitignore                  # Prevents committing credentials, caches, and .env
├── README.md                   # Full documentation and operational guide
└── Login, so the system...pdf  # Comprehensive project specification document
```

---

## Quick Start Guide

### 1. Prerequisites
- Python 3.10+ (64-bit)
- Modern web browser

### 2. Installation
Clone the repository and install the dependencies:

```bash
git clone https://github.com/Amr-Sheqwara/your-repository-name.git
cd your-repository-name
pip install -r requirements.txt
```

### 3. Launch the Backend Server
```bash
python medgemma_server.py
```
The server will start on `http://127.0.0.1:8000`.

### 4. Open the Console
Double-click `Crew Health Console.html` to open it in your browser, or serve it locally:

```bash
python -m http.server 3000
```
Then navigate to: `http://localhost:3000/Crew Health Console.html`

---

## Enabling Neural Model Weights (`google/medgemma-4b-it`)

`google/medgemma-4b-it` is a gated model under Google's Health AI Developer Foundations (HAI-DEF) license.

To load the official neural weights:
1. Log in to [Hugging Face](https://huggingface.co).
2. Accept the license agreement at [google/medgemma-4b-it](https://huggingface.co/google/medgemma-4b-it).
3. Create an Access Token under **Settings -> Access Tokens**.
4. Create your `.env` file from the template:
   ```bash
   cp .env.example .env
   ```
5. Insert your token into `.env`:
   ```env
   HF_TOKEN=hf_your_token_here
   ```
6. Start `medgemma_server.py`. The ~8.6 GB weights will automatically download to your local cache and begin serving inference.

---

## Security & Secrets

Never commit your `.env` file to any public Git repository. The provided `.gitignore` automatically excludes `.env` and local caches to prevent credential exposure.
