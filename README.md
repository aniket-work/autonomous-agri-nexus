# AgriNexus-AI: Autonomous Precision Agriculture Consultant 🌾🤖

![AgriNexus Core](https://raw.githubusercontent.com/aniket-work/agri-nexus-ai/main/agrinexus_core/images/title-animation.gif)

> **How I Built an Autonomous Agent that Combines IoT Soil Sensors with Search-Based Reasoning to Rescue Crops.**

## 📖 Introduction
AgriNexus-AI is an experimental autonomous agent designed to solve a critical problem in modern agriculture: **Information Overload**. 

Farmers have access to millisecond-latency sensor data (Nitrogen, Moisture, pH), but correlating that data with hyper-localized weather forecasts and the latest agronomic research requires hours of manual analysis. 

This project demonstrates a **"Search-First" Agentic Architecture** that:
1. **Ingests** real-time telemetry from a simulated IoT Sensor Mesh.
2. **Detects** anomalies (e.g., Nitrogen deficiency exacerbated by heavy rainfall).
3. **Autonomously Researches** remediation strategies using live web search.
4. **Synthesizes** a strategic, citation-backed advisory report for the farmer.

![Architecture](https://raw.githubusercontent.com/aniket-work/agri-nexus-ai/main/agrinexus_core/images/architecture_diagram.png)

## 🏗️ Architecture
The system follows a modular composed architecture:

- **IoT Layer**: Simulates Zigbee-connected soil sensors generating noisy, realistic data.
- **Analysis Engine**: Statistical anomaly detection to flag zones requiring attention.
- **Research Agent**: A specialized sub-agent that formulates multi-hop search queries to find context-specific solutions.
- **Synthesis Core**: Combines sensor data, weather context, and research findings into actionable advice.

![Flow](https://raw.githubusercontent.com/aniket-work/agri-nexus-ai/main/agrinexus_core/images/flow_diagram.png)

## 🚀 Getting Started

### Prerequisites
- Python 3.10+
- `pip`

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/aniket-work/agri-nexus-ai.git
   cd agri-nexus-ai
   ```

2. **Install Dependencies**
   ```bash
   pip install -r agrinexus_core/requirements.txt
   ```

3. **Run the Simulation**
   ```bash
   python -m agrinexus_core.src.main
   ```

## 📊 Sample Output
When an anomaly (e.g., "Nitrogen Deficiency" + "High Moisture") is detected, the agent triggers a research workflow:

```text
[AI AGENT] Phase 1: Analyzing Sensor Stream...
  > Field Average N: 115.4 mg/kg (Low)
  > Field Average Moisture: 68.2 % (High)
  
[AI AGENT] Phase 2: Formulating Research Strategy...
  > Query: 'Corn nitrogen deficiency high moisture treatment'
  > Found: 'Rescue Nitrogen Applications in Wet Soils'

[AI AGENT] Phase 3: Synthesizing Recommendation...
  > Recommendation: Switch to a side-dress application of UAN-28...
```

## 🛠️ Technology Stack
- **Python**: Core logic and orchestration.
- **Rich**: For the high-fidelity terminal user interface.
- **DuckDuckGo Search**: For autonomous web research.
- **Matplotlib/NumPy**: For sensor data simulation and heatmap generation.
- **Mermaid.js**: For architectural diagrams.

## 🤝 Contribution
This is an experimental PoC. Suggestions and PRs are welcome!

## 📄 License
MIT License.
