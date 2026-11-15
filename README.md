# NASA Crew Health Console (CelestCare)

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.115%2B-009688.svg)](https://fastapi.tiangolo.com/)
[![Model](https://img.shields.io/badge/Model-MedGemma--4B--IT-red.svg)](https://huggingface.co/google/medgemma-4b-it)
[![NASA Standard](https://img.shields.io/badge/Standard-NASA--STD--3001-orange.svg)](https://www.nasa.gov/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

An autonomous medical, physiological, and clinical monitoring workstation engineered for astronauts on long-duration spaceflight missions across Low Earth Orbit (ISS), Deep-Space Transit, Lunar Surface, and Mars Exploration.

The system pairs an interactive single-page mission operations console with an AI clinical decision support backend powered by Google's **MedGemma-4B-IT** multimodal foundation model, backed by a deterministic NASA Human Research Program (HRP) rule-based spaceflight triage engine.

---

## Table of Contents

- [System Architecture](#system-architecture)
- [Frontend Architecture (Crew Health Console.html)](#frontend-architecture-crew-health-consolehtml)
  - [Module Breakdown](#module-breakdown)
  - [Interactive Anatomical Map](#interactive-anatomical-map)
  - [Circadian Lighting & Sleep Engine](#circadian-lighting--sleep-engine)
  - [Cognitive Assessment Suite](#cognitive-assessment-suite)
  - [Sensory Sanctuary (Earth Biome Audio)](#sensory-sanctuary-earth-biome-audio)
- [Backend Architecture (medgemma_server.py)](#backend-architecture-medgemma_serverpy)
  - [API Specification](#api-specification)
  - [Dual-Mode Clinical Decision Engine](#dual-mode-clinical-decision-engine)
  - [Rule-Based Triage Decision Matrix](#rule-based-triage-decision-matrix)
- [Repository Structure](#repository-structure)
- [NASA Data & Spaceflight Standards Alignment](#nasa-data--spaceflight-standards-alignment)
- [Installation & Quick Start](#installation--quick-start)
  - [Prerequisites](#prerequisites)
  - [Backend Setup](#backend-setup)
  - [Frontend Launch](#frontend-launch)
  - [Enabling Neural Model Weights](#enabling-neural-model-weights)
- [Environment Configuration](#environment-configuration)
- [Security & Isolation](#security--isolation)
- [References & Open Source Attribution](#references--open-source-attribution)

---

## System Architecture

```text
+-----------------------------------------------------------------------------------+
|                           CREW HEALTH CONSOLE (BROWSER)                           |
|                                                                                   |
|  +------------------------+  +--------------------------+  +-------------------+  |
|  | Landing Page & i18n    |  | Mission Profile Setup    |  | Live SVG Body Map |  |
|  | (English / Arabic)     |  | (Blood, Genes, Location) |  | (Visual Triage)   |  |
|  +------------------------+  +--------------------------+  +-------------------+  |
|                                                                                   |
|  +------------------------+  +--------------------------+  +-------------------+  |
|  | Telemetry & ECG Canvas |  | Circadian Lighting HUD   |  | Cognitive Testing |  |
|  | (Vitals, Cabin ECLSS)  |  | (Day, Dusk, Night Dim)   |  | (Motor & Memory)  |  |
|  +------------------------+  +--------------------------+  +-------------------+  |
+------------------------------------------+----------------------------------------+
                                           |
                                  HTTP / JSON (REST)
                             POST http://127.0.0.1:8000/diagnose
                                           |
+------------------------------------------v----------------------------------------+
|                          FASTAPI CLINICAL BACKEND SERVICE                         |
|                                (medgemma_server.py)                               |
|                                                                                   |
|  +-----------------------------------------------------------------------------+  |
|  | Request Deserializer & Image Decoder (Base64 -> RGB PIL)                    |  |
|  +-------------------------------------+---------------------------------------+  |
|                                        |                                          |
|                     Is Model Loaded & Token Authenticated?                        |
|                                        |                                          |
|                 +----------------------+----------------------+                   |
|                 | YES                                         | NO / FALLBACK     |
|                 v                                             v                   |
|  +-------------------------------+             +-------------------------------+  |
|  | Neural Multimodal Pipeline    |             | NASA HRP Deterministic Triage |  |
|  | (google/medgemma-4b-it)       |             | (SANS, SMS, ECG, Hypoxia,     |  |
|  | SigLIP Vision + bfloat16      |             | Immune Dysregulation Rules)   |  |
|  +-------------------------------+             +-------------------------------+  |
|                 |                                             |                   |
|                 +----------------------+----------------------+                   |
|                                        |                                          |
|                                        v                                          |
|  +-----------------------------------------------------------------------------+  |
|  | Structured Clinical Evaluation & Immediate Countermeasure Recommendations   |  |
|  +-----------------------------------------------------------------------------+  |
+-----------------------------------------------------------------------------------+
```

---

## Frontend Architecture (Crew Health Console.html)

The user interface is delivered as a zero-dependency, self-contained single-page application built strictly with modern HTML5, CSS3, and ES6+ JavaScript. It requires no Node.js runtime, build step, or external content delivery networks (CDNs).

### Module Breakdown

| Function / Component | Scope and Operational Description |
| :--- | :--- |
| `applyLang(lang)` | Full bi-directional internationalization switching between English (`ltr`) and Arabic (`rtl`). Dynamically updates all UI elements via `data-en` and `data-ar` attributes. |
| `enter()` | Validates and persists astronaut identity: Full Name, Blood Group, Biological Sex, Genetic Predispositions, and Mission Environment (ISS, Lunar, Mars, Deep Space Transit). |
| `renderFig()` / `renderPart(p)` | Renders the SVG anatomical vector map, overlays clinical alert zones, and triggers organ pulse animations for active medical complaints. |
| `renderTiles()` / `countUp()` | Formats and animates real-time vital signs: Heart Rate (bpm), Blood Oxygen (SpO2 %), Blood Pressure (Sys/Dia mmHg), Core Body Temperature (C), and Blood Glucose (mg/dL). |
| `ecg()` | Canvas-based continuous rendering engine drawing a physiological 68 bpm P-Q-R-S-T cardiac waveform with calibrated sweep velocity. |
| `applyMode(m)` | Controls interface color grading and brightness: Day Mode, Dusk Mode, and Night/Sleep Mode (amber-red monochrome spectrum below 600nm to preserve astronaut melatonin secretion). |
| `tickEnv()` / `renderEnv()` | Simulates and monitors cabin environmental life support (ECLSS): CO2 concentration (mmHg), O2 percentage, cabin barometric pressure (kPa), PM2.5 particulate count, and cumulative ionizing radiation dosage (mSv). |
| `spark(svg, data, min, max)` | Generates inline dynamic SVG sparklines tracking high-frequency environmental drift across historical observation windows. |
| `askAI()` | Assembles diagnostic payload: clinical narrative, base64 photograph, astronaut profile, and vital telemetry; dispatches to backend service and renders diagnostic assessments. |
| `chart()` / `renderCharts()` | Draws multi-point SVG trend charts across a rolling 12-day mission window against established NASA-STD-3001 physiological safety limits. |
| `notify(msg, lvl)` / `status()` | Multi-tier alert dispatcher sending timestamped notifications to Flight Surgeon, Crew Medical Officer (CMO), Commander, and Flight Director. |

### Interactive Anatomical Map

The console maps astronaut symptoms directly to anatomical regions through an interactive SVG overlay anchored to [Images/human_figure.png](Images/human_figure.png).

- **Critical Alert Tier (Red Pulse)**:
  - **Brain**: Intracranial pressure, cephalad fluid shift, Spaceflight-Associated Neuro-Ocular Syndrome (SANS), cognitive exhaustion.
  - **Heart**: Arrhythmias, orthostatic intolerance, microgravity cardiovascular deconditioning.
  - **Lungs**: Hypoxia, elevated ambient cabin CO2 toxicity, EVA suit scrubber anomalies.
- **Secondary Alert Tier (Yellow Pulse)**:
  - **Abdomen**: Caloric deficit, spaceflight microbiome disruption, constipation, motion-induced gastrointestinal stasis.
  - **Arms / Hands / Legs / Spine**: Musculoskeletal deconditioning, intervertebral disc expansion (spinal elongation backache), resistive exercise strain.

### Circadian Lighting & Sleep Engine

To mitigate spaceflight insomnia, circadian disruption, and sleep debt:

```text
[Day Mode]          -> High color temperature (balanced white/blue) for operational alertness.
[Dusk Mode]         -> Warm amber transition lighting 2 hours prior to scheduled sleep opportunity.
[Night / Sleep Mode]-> Red-spectrum illumination (620-750 nm) eliminating blue photons that suppress
                       melatonin synthesis, integrated with UI brightness dimming.
```

### Cognitive Assessment Suite

Two psychomotor and cognitive performance evaluation modules are built directly into the console to quantify central nervous system fatigue during long-duration operations:

1. **Asteroid Psychomotor Vigilance Test (`initGame`, `gameLoop`, `spawnAsteroid`)**:
   - Measures fine-motor reaction latency, visual tracking precision, and target interception speed.
   - Outputs reaction latency metrics directly into the astronaut's cognitive performance record.
2. **Neural Matrix Working Memory Test (`buildGrid`, `cardClick`, `endMemGame`)**:
   - 4x4 spatial working memory challenge evaluating short-term visual memory retention and pattern recall under mental fatigue.

### Sensory Sanctuary (Earth Biome Audio)

To counter psychological isolation, sensory monotony, and confinement-induced depression on deep space transits:
- Built with the native browser **Web Audio API** (`AudioContext`).
- Synthesizes procedural acoustic profiles without external audio files:
  - **Rainfall**: Filtered white noise with dynamic low-pass resonance.
  - **Forest**: Bandpass-filtered pink noise with simulated intermittent birdsong harmonics.
  - **Ocean Waves**: Ultra-low-frequency oscillator driving slow amplitude-modulated surge cycles.

---

## Backend Architecture (medgemma_server.py)

The backend is built with **FastAPI** and **Uvicorn**, providing asynchronous non-blocking inference with cross-origin resource sharing (CORS) enabled for direct web client interaction.

### API Specification

#### 1. Clinical Diagnosis Endpoint

- **Route**: `POST /diagnose`
- **Content-Type**: `application/json`

**Request Body Schema (`DiagnoseRequest`)**:
```json
{
  "text": "Severe retro-orbital headache and blurred vision after EVA maintenance.",
  "image": "data:image/jpeg;base64,/9j/4AAQSkZJRg...",
  "profile": {
    "name": "Alex Mercer",
    "blood": "A+",
    "sex": "Female",
    "gene": "Cardiovascular predisposition",
    "env": "Deep-Space Transit"
  },
  "env": "Deep-Space Transit",
  "vitals": {
    "hr": 78,
    "spo2": 96,
    "sys": 128,
    "dia": 82,
    "temp": 36.9,
    "glu": 94
  }
}
```

**Response Body Schema**:
```json
{
  "answer": "Evaluation for Alex Mercer (Deep-Space Transit):\n- Triage Status: Priority Clinical Evaluation\n- Differential Consideration: Potential Spaceflight-Associated Neuro-Ocular Syndrome (SANS) or microgravity fluid shift toward the head.\n- Recommended Countermeasures: Perform visual acuity testing and fundoscopy/OCT if available on board. Log cabin CO2 levels immediately."
}
```

#### 2. System Health Endpoint

- **Route**: `GET /health`
- **Response**:
```json
{
  "status": "online",
  "model": "google/medgemma-4b-it",
  "pipeline_loaded": true,
  "loading": false,
  "error": null
}
```

### Dual-Mode Clinical Decision Engine

The server implements a fault-tolerant dual-mode architecture:

```text
                  +----------------------------------+
                  |  Incoming Request to /diagnose   |
                  +-----------------+----------------+
                                    |
                    Is google/medgemma-4b-it loaded?
                                    |
                     +--------------+--------------+
                     |                             |
                   [YES]                         [NO]
                     |                             |
                     v                             v
       +----------------------------+  +----------------------------+
       | MedGemma Neural Inference  |  | NASA HRP Rule-Based Engine |
       | - SigLIP Multimodal Vision |  | - Deterministic Triaging   |
       | - bfloat16 / CUDA Map      |  | - HRP Domain Validation    |
       | - Zero Latency Degradation |  | - 100% Guaranteed Uptime   |
       +----------------------------+  +----------------------------+
```

1. **Neural Mode (`google/medgemma-4b-it`)**:
   - Executes when a valid Hugging Face User Access Token is configured and authorized weights are present.
   - Processes textual observations alongside base64 clinical imagery (rashes, eye scans, skin lesions) via Google's SigLIP vision-language encoder.
2. **Deterministic Triage Mode (`rule_based_space_medical_triage`)**:
   - Active immediately upon server startup while weights download, or as a graceful zero-downtime fallback when running offline or on hardware without a dedicated GPU.
   - Implements clinical diagnostic heuristics grounded in NASA Human Research Program protocols.

### Rule-Based Triage Decision Matrix

| Clinical Domain | Trigger Keywords | Diagnostic Consideration | Prescribed Protocol & Countermeasure |
| :--- | :--- | :--- | :--- |
| **SANS / Neuro-Ocular** | `headache`, `vision`, `blur`, `eye`, `pressure` | Spaceflight-Associated Neuro-Ocular Syndrome; cephalad fluid shifts. | Conduct optical coherence tomography / fundoscopy; log cabin CO2 immediately. |
| **Vestibular / SMS** | `dizzy`, `nausea`, `vomit`, `balance`, `vertigo` | Space Motion Sickness (SMS); inner-ear otolith adaptation. | Restrict rapid head motion; defer all non-critical extravehicular activity (EVA). |
| **Cardiovascular** | `chest`, `pain`, `tight`, `palpitation`, `heart` | Spaceflight cardiovascular deconditioning; cardiac arrhythmia risk. | Emergency status: cease exercise immediately, attach 12-lead ECG, alert Flight Surgeon. |
| **Immune & Skin** | `rash`, `itch`, `skin`, `hives`, `sore`, `fever` | Latent viral reactivation (EBV / VZV); microgravity immune dysregulation. | Inspect lesion margins daily; isolate contact with space suit pressure liner. |
| **Telemetry Outlier** | `spo2 < 95%`, `hr > 100`, `temp > 37.8C` | Hypoxia, cabin scrubber failure, systemic inflammatory response. | Elevate triage urgency; re-evaluate physiological telemetry every 60 minutes. |

---

## Repository Structure

```text
CelestCare/
├── .env.example                # Configuration template for Hugging Face access token
├── .gitignore                  # Exclusion rules for virtual environments, secrets, and caches
├── Crew Health Console.html    # Interactive single-page mission operations console
├── medgemma_server.py          # Asynchronous FastAPI medical server with MedGemma integration
├── README.md                   # System documentation, architectural specifications, and runbook
├── requirements.txt            # Pinned Python package dependencies
└── Images/                     # Visual assets and anatomical diagrams
    ├── human_figure.png        # Anatomical vector mapping overlay
    └── nasa_logo.png           # Official NASA insignia emblem
```

---

## NASA Data & Spaceflight Standards Alignment

This project directly aligns with space medicine research and operational documentation published by NASA:

### 1. NASA Human Research Program (HRP) Evidence Books
The diagnostic logic and health check-ins address core spaceflight physiological risks:
- **Risk of Spaceflight-Associated Neuro-Ocular Syndrome (SANS)**: Ocular flattening, optic disc edema, and hyperopic shifts from sustained cephalad venous fluid redistribution.
- **Risk of Space Motion Sickness (SMS)**: Neurovestibular conflict between semicircular canals and otolith organs during gravity transitions.
- **Risk of Adverse Cognitive and Behavioral Conditions**: Sleep loss, circadian disruption, and operational isolation during long-duration exploration.
- **Risk of Immune System Dysregulation**: Subclinical latent herpesvirus reactivation (Epstein-Barr, Varicella-Zoster) and skin barrier compromise.
- **Risk of Bone and Muscle Deconditioning**: Microgravity-induced muscle atrophy and bone mineral loss mitigated by scheduled resistance training.

### 2. NASA Spaceflight Human-System Standard (NASA-STD-3001)
- **Volume 1 (Crew Health)**:
  - Establishes baseline physiological standards for vital signs, medical hardware interfaces, and clinical record logging.
- **Volume 2 (Human Factors, Habitation, and Environmental Quality)**:
  - Cabin atmospheric limits: Carbon Dioxide concentration ($\text{P}_{\text{CO}_2} < 3.0 \text{ mmHg}$ nominal), Oxygen fraction ($19.5\% - 23.5\%$), and total pressure ($101.3 \text{ kPa}$).
  - Ionizing radiation surveillance: Monitoring cumulative Solar Particle Events (SPE) and Galactic Cosmic Rays (GCR).

### 3. Operational Exercise Countermeasures
- Automated scheduling for the mandatory **2-hour daily exercise prescription**:
  - Advanced Resistive Exercise Device (ARED) for axial skeleton bone retention.
  - T2 Treadmill and Cycle Ergometer (CEVIS) for aerobic and cardiovascular conditioning.

---

## Installation & Quick Start

### Prerequisites

- **Python**: Version 3.10, 3.11, or 3.12 installed.
- **Browser**: Any modern web browser supporting ES6+ (Chrome, Firefox, Safari, Edge).
- **GPU (Optional)**: NVIDIA GPU with CUDA support and at least 12 GB VRAM for local execution of `google/medgemma-4b-it`. If no GPU is available, the server automatically operates in CPU fallback mode.

### Backend Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/YourUsername/CelestCare.git
   cd CelestCare
   ```

2. **Create and activate a virtual environment**:
   ```bash
   # Windows (PowerShell)
   python -m venv .venv
   .venv\Scripts\Activate.ps1

   # Linux / macOS
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Start the FastAPI backend service**:
   ```bash
   python medgemma_server.py
   ```
   The backend service starts at `http://127.0.0.1:8000`. You can verify readiness by navigating to `http://127.0.0.1:8000/health`.

### Frontend Launch

Open `Crew Health Console.html` directly in your browser, or serve it with Python's built-in HTTP server:

```bash
python -m http.server 3000
```
Navigate to `http://localhost:3000/Crew Health Console.html`.

### Enabling Neural Model Weights

To enable the live `google/medgemma-4b-it` foundation model:

1. Create a [Hugging Face](https://huggingface.co) account.
2. Request model access on the repository page: [google/medgemma-4b-it](https://huggingface.co/google/medgemma-4b-it).
3. Generate a User Access Token under **Settings -> Access Tokens**.
4. Create a `.env` file in the project root:
   ```bash
   cp .env.example .env
   ```
5. Add your token to `.env`:
   ```text
   HF_TOKEN=hf_your_actual_access_token_here
   ```
6. Restart `medgemma_server.py`. The model weights (~8.6 GB) will download and initialize automatically in the background.

---

## Environment Configuration

| Variable | Required | Default | Description |
| :--- | :--- | :--- | :--- |
| `HF_TOKEN` | Optional | `None` | Hugging Face User Access Token authorized for `google/medgemma-4b-it`. |
| `HOST` | Optional | `127.0.0.1` | Local network binding address for FastAPI. |
| `PORT` | Optional | `8000` | Local network port for FastAPI. |

---

## Security & Isolation

- **Zero External Telemetry Leaks**: Astronaut health records, vital metrics, and clinical photographic evaluations are processed locally on the workstation or spacecraft intranet.
- **Secret Isolation**: The repository includes [.gitignore](.gitignore) rules that strictly prevent `.env`, personal tokens, Python bytecode, and local Hugging Face weight caches from being committed.
- **Resilient Fallback**: In the event of a deep-space communications blackout or missing GPU hardware, all clinical workflows remain fully operational via deterministic onboard triage heuristics.

---

## References & Open Source Attribution

1. **Google MedGemma**: Open-weight multimodal medical foundation models based on Gemma 3 architecture (`google/medgemma-4b-it`).
2. **NASA Human Research Roadmap (HRR)**: Evidence-based risk mitigation strategies for long-duration space missions.
3. **NASA Open Science Data Repository (OSDR)**: Biological and physiological standards from spaceflight experiments.
4. **FastAPI & Uvicorn**: Asynchronous high-performance web framework for Python.
5. **Hugging Face Transformers & Accelerate**: Scalable model loading and multi-precision execution framework.
