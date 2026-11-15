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
  - [NASA-STD-3001 Periodic Human Performance Subsystem](#nasa-std-3001-periodic-human-performance-subsystem)
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

### NASA-STD-3001 Periodic Human Performance Subsystem

Directly integrated into the measurements interface, this subsystem enables crewmembers to record in-flight fitness-for-duty metrics derived from cycle ergometers, resistive load cells, and biochemical assays, cross-referencing them against active mission environment standards:

- **Aerobic Capacity ($VO_{2\max}$)** (`vo2Input`): Evaluated against microgravity EVA baseline ($\ge 32.9\text{ ml/min/kg}$, `[V1 4001]`) or planetary surface locomotion baseline ($\ge 36.5\text{ ml/min/kg}$, `[V1 4002]`). Sub-nominal values trigger heart triage pulse and countermeasure recommendations.
- **ARED Muscular Strength Retention** (`strengthInput`): Monitored against the 80% baseline limit (`[V1 4024]`); flags musculoskeletal deconditioning and alerts the crew to increase resistive loading.
- **Bone Mineral Density (BMD) Retention** (`bmdInput`): Monitored against the 95% hip/spine retention limit (`[V1 4027]`).
- **Urinary Calcium Demineralization Index** (`calciumInput`): Detects acute hypercalciuria ($> 300\text{ mg/24h}$ stone risk, $> 400\text{ mg/24h}$ severe risk), immediately dispatching critical emergency alerts to the Flight Surgeon / CMO and pulsing the abdominal zone red.

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
| **Musculoskeletal & Bone** | `bone`, `kidney`, `stone`, `flank`, `back pain`, `calcium` | Accelerated bone mineral loss & hypercalciuria-induced nephrolithiasis (`[V1 4027]`). | Immediate ultrasound, aggressive hydration (>2.5 L/day), verify ARED resistive countermeasure completion. |
| **Telemetry Hypoxia** | `spo2 < 92%` (critical) or `spo2 < 96%` (sub-nominal) | Critical cabin hypoxia, suit scrubber anomaly, ambient hypercapnia. | Critical alert: assess ECLSS scrubbers, verify suit pressure, administer supplemental O2. |
| **Telemetry Circulatory** | `hr > 110`, `hr < 45`, `sys > 135`, `sys < 85` | Tachycardia, bradycardia, or circulatory instability from microgravity unloading. | Cease physical workloads; re-measure vitals; notify Crew Medical Officer. |
| **Telemetry Systemic** | `temp > 38.0C` (fever) or `glu < 55 mg/dL` | Active systemic inflammatory response or acute hypoglycemia. | Prioritize clinical evaluation, isolate infectious contact, provide acute carbohydrate feed. |

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
├── TEAM_EXPLANATION_AR.md      # Arabic team briefing & NASA-STD-3001 operational handbook
└── Images/                     # Visual assets and anatomical diagrams
    ├── human_figure.png        # Anatomical vector mapping overlay
    └── nasa_logo.png           # Official NASA insignia emblem
```

---

## NASA Data & Spaceflight Standards Alignment

This project directly aligns with space medicine research, operational guidelines, and engineering standards published by NASA:

### 1. Calibrated Physiological Telemetry Reference (NASA-STD-3001 Vol 1)

The console implements flight-calibrated physiological envelopes derived from NASA-STD-3001 Volume 1 (Crew Health):

| Metric | Nominal Range (Planetary/1g) | Microgravity Adaptation (ISS/Transit) | Clinical Attention Boundary | Critical Medical Emergency | Clinical Rationale & Spaceflight Dynamics |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Heart Rate** | 50 – 90 bpm | 50 – 90 bpm | < 45 or > 110 bpm | < 40 or > 120 bpm | Rest resting bradycardia/tachycardia; arrhythmia risk exacerbated by autonomic and electrolyte shifts. |
| **Systolic BP** | 90 – 125 mmHg | 85 – 120 mmHg | < 80 or > 140 mmHg | < 75 or > 160 mmHg | Cephalad fluid shift reduces lower-extremity hydrostatic pooling; resting arterial pressure runs slightly lower. |
| **Diastolic BP** | 60 – 80 mmHg | 55 – 80 mmHg | < 50 or > 90 mmHg | < 45 or > 100 mmHg | Central vascular compliance adaptation and altered baroreceptor reflex sensitivity. |
| **Blood Oxygen (SpO₂)** | 96 – 100% | 96 – 100% | 92 – 95% | < 92% | Evaluates tissue hypoxia; sub-nominal values indicate cabin scrub malfunction or suit pressure compromise. |
| **Core Body Temp** | 36.5 – 37.5 °C | 36.6 – 37.6 °C | < 35.8 or > 38.0 °C | < 35.0 or > 38.5 °C | Microgravity "space fever" caused by reduced convective heat transfer and chronic low-grade inflammation. |
| **Blood Glucose** | 70 – 100 mg/dL | 70 – 100 mg/dL | < 60 or > 140 mg/dL | < 55 or > 180 mg/dL | Fasting baseline monitoring; acute hypoglycemia severely degrades fine-motor piloting and EVA performance. |

---

### 2. NASA-STD-3001 Section 4.0 Human Performance Compliance Matrix

The following matrix documents direct compliance with the technical requirements and Permissible Outcome Limits (POLs) established in NASA-STD-3001 Section 4.0 (Human Performance):

| Standard Code | Standard Title | NASA Threshold & Permissible Limit | CelestCare Technical Implementation |
| :--- | :--- | :--- | :--- |
| **[V1 4001]** | Microgravity EVA Aerobic Capacity | In-mission $VO_{2\max} \ge 32.9 \text{ ml/min/kg}$ for microgravity EVAs. | Interactive logging (`vo2Input`) and automated evaluation; triggers cardiovascular warning and CEVIS countermeasure guidance if sub-nominal. |
| **[V1 4002]** | Extraterrestrial Surface EVA Aerobic Capacity | In-mission $VO_{2\max} \ge 36.5 \text{ ml/min/kg}$ for lunar/Martian surface EVAs. | Dynamic surface EVA threshold validation; elevates aerobic cutoff to $36.5\text{ ml/min/kg}$ on Moon or Mars surface environments. |
| **[V1 4003]** | In-Mission Aerobic Retention | Maintain aerobic capacity at or above **80% of pre-mission baseline**. | 12-day longitudinal SVG trend charts (`renderCharts()`) alerting if estimated cardiovascular work output drops below 80%. |
| **[V1 4007]** | In-Mission Sensorimotor Metrics | Task-specific functional assessment of motor control, eye-hand coordination, and gaze. | **Asteroid Psychomotor Vigilance Test** (`initGame()`, `gameLoop()`) measuring reaction latency and motor interception precision. |
| **[V1 4011]** | Behavioral Health & Cognitive Status | Maintain behavioral and cognitive status within clinically accepted ranges. | **Neural Matrix Working Memory Test** (`buildGrid()`, `cardClick()`) and daily subjective mood/stress scoring. |
| **[V1 4014]** | Critical Tasks & Planned Sleep Period | Establish strict limits on work, physical activity, and protected sleep periods. | **Circadian Sleep Engine** (`applyMode()`, `sleepGo()`, `wake()`) with red-amber spectrum lighting and sleep-debt triage. |
| **[V1 4016]** | Hematology & Immunology Countermeasures | In-mission countermeasures to sustain immune parameters outside critical morbidity levels. | Automated triage for dermatological lesions and latent viral reactivation (EBV / VZV) in `medgemma_server.py`. |
| **[V1 4020]** | In-Mission Nutrient Intake | Provide 100% of calculated nutrient and caloric energy requirements. | Daily nutritional monitoring module checking caloric frequency and hydration intake (> 2.5 L/day). |
| **[V1 4023]** | Pre-Mission Muscle Strength | Meet baseline strength: Deadlift $\ge 1.0 - 1.6\times$ BW; Bench Press $\ge 0.7 - 1.0\times$ BW. | Astronaut personalized profile setup (`enter()`) incorporating physical baseline capabilities into monitoring models. |
| **[V1 4024]** | In-Mission Skeletal Muscle Strength | Maintain skeletal muscle strength at or above **80% of baseline**. | Interactive logging (`strengthInput`) from ARED telemetry; triggers musculoskeletal alerts and pulses leg/spine zones if $< 80\%$. |
| **[V1 4027]** | Microgravity Bone Mineral Density (BMD) Loss | Maintain hip and spine BMD $\ge 95\%$ of pre-mission values; femoral neck $\ge 90\%$. | Interactive logging (`bmdInput`, `calciumInput`); automated triage for hypercalciuria-induced renal stone formation and emergency surgeon alert. |
| **[V1 4030]** | Career Space Permissible Exposure Limit (SPEL) | Total career effective radiation dose $< 600 \text{ mSv}$ universal across all ages/sexes. | Dosimetry logging module integrating ionizing radiation telemetry against the 3% cancer mortality risk ceiling. |
| **[V1 4031]** | Solar Particle Event (SPE) Limit | Protect crew from design reference SPE to $< 250 \text{ mSv}$ effective dose. | Real-time cabin radiation spike alerts and automated emergency storm-shelter notifications. |
| **[V1 4033]** | Galactic Cosmic Radiation (GCR) Limits | Habitable volume protection: $< 1.3 \text{ mSv/day}$ (free space), $< 0.9 \text{ mSv/day}$ (surface). | Continuous ECLSS radiation gauge (`renderEnv()`) displaying environment-specific GCR permissible ceilings. |

---

### 3. NASA Human Research Program (HRP) Evidence Books
The diagnostic logic and health check-ins address core spaceflight physiological risks:
- **Risk of Spaceflight-Associated Neuro-Ocular Syndrome (SANS)**: Ocular flattening, optic disc edema, and hyperopic shifts from sustained cephalad venous fluid redistribution.
- **Risk of Space Motion Sickness (SMS)**: Neurovestibular conflict between semicircular canals and otolith organs during gravity transitions.
- **Risk of Adverse Cognitive and Behavioral Conditions**: Sleep loss, circadian disruption, and operational isolation during long-duration exploration.
- **Risk of Immune System Dysregulation**: Subclinical latent herpesvirus reactivation (Epstein-Barr, Varicella-Zoster) and skin barrier compromise.
- **Risk of Bone and Muscle Deconditioning**: Microgravity-induced muscle atrophy and bone mineral loss mitigated by scheduled resistance training.

---

### 4. Operational Exercise Countermeasures
- Automated scheduling for the mandatory **2-hour daily exercise prescription**:
  - Advanced Resistive Exercise Device (ARED) for axial skeleton bone retention and spinal support.
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
