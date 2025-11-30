# Multi-Persona Brainstorm Partner: Enterprise-Grade Decision Engine (ADK Project)

> **"A Boardroom in a Box"** — An intelligent, agentic system that brainstorms, debates, and synthesizes actionable strategies using a Council of AI Personas.

![ADK Powered](https://img.shields.io/badge/Powered%20by-Google%20ADK-blue?style=for-the-badge&logo=google)
![Python](https://img.shields.io/badge/Python-3.10%2B-yellow?style=for-the-badge&logo=python)
![Status](https://img.shields.io/badge/Status-Active-success?style=for-the-badge)

---

## Problem & Value Proposition

Today’s generative AI tools typically operate from a single point of view, leading to one-dimensional answers. Real expertise emerges when diverse perspectives—creativity, risk assessment, and data-driven logic—are brought together.

This project solves this by simulating a **Council of Experts** that thinks the way humans actually work in groups. It leverages four key **Google Agent Development Kit (ADK)** concepts to achieve this:

1.  **SequentialAgent**: Orchestrates the high-level flow from the Council -> Mediator -> Podcaster, ensuring a structured pipeline of thought.
2.  **ParallelAgent**: Runs the "Council" of personas (Analyst, Critic, Optimist) simultaneously, allowing for diverse, independent viewpoints to be generated in parallel.
3.  **LlmAgent**: Powers each individual persona with a distinct personality and instruction set (e.g., the "Critic" is instructed to find flaws, the "Optimist" to find benefits).
4.  **Custom Tools**: Equips the "Domain Expert" agent with a real-time **Web Search Tool**, enabling it to fetch live market data and avoid hallucinations.

By combining these, the system provides balanced perspectives, reduced hallucination, and structured decision-making that no single-prompt LLM can match.

---

## Architectural Design (ADK Flow)

The system follows a **Router-Council-Mediator** pattern with a feedback loop, designed to simulate a brainstorming session between experts.

```mermaid
flowchart TD
    User([User Input]) --> Router[🚦 Router Agent]
    
    Router -- "Selects Experts" --> Decision{Is Chitchat?}
    
    %% Path 1: Simple Chitchat
    Decision -- Yes --> Greeter[💬 Greeter Agent]
    Greeter --> Output([Final Response])
    
    %% Path 2: Brainstorming Session
    Decision -- No --> P3
    
    subgraph CouncilBox [Dynamic Council - Parallel Execution]
        direction TB
        P1[📈 Analyst]
        P2[🛑 Critic]
        P3[✨ Optimist]
        P4[🎨 Creative Thinker]
        P5[🛠️ Domain Expert]
    end
    
    P1 & P2 & P3 & P4 & P5 --> Mediator[⚖️ Mediator Agent]
    
    Mediator -- "Synthesizes Reports" --> Check{Consensus Reached?}
    
    %% Feedback Loop
    Check -- "No (Request Refinement)" --> Feedback[⚠️ Feedback Loop]
    Feedback --> P3
    
    %% Success Path
    Check -- "Yes (Ready)" --> Podcaster[🎙️ Podcaster Agent]
    Podcaster --> Output([Final Podcast Script])

    %% Styling
    classDef agent fill:#f9f,stroke:#333,stroke-width:2px;
    classDef control fill:#ffd,stroke:#333,stroke-width:2px;
    classDef storage fill:#dfd,stroke:#333,stroke-width:2px;
    
    class Router,Greeter,Mediator,Podcaster,P1,P2,P3,P4,P5 agent;
    class Decision,Check control;
```

### Workflow Steps:
1.  **Router Agent**: Analyzes the user's prompt and dynamically selects the best experts (e.g., "Creative Thinker" for abstract ideas).
2.  **Dynamic Council (Parallel Execution)**: Selected agents run simultaneously to generate independent reports.
3.  **Mediator Agent**: Synthesizes the reports, resolving conflicts between the Optimist and Critic.
4.  **Feedback Loop**: If the Mediator isn't satisfied, it requests refinement from the Council.
5.  **Podcaster Agent**: Converts the final technical plan into an engaging audio script.

---

## How to Run Locally

Follow these steps to get the project running on your local machine.

### Prerequisites
-   Python 3.10 or higher
-   A Google Cloud Project with Gemini API access

### Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/manavbhatt072/multi-persona-agent.git
    cd multi-persona-agent
    ```

2.  **Set up Virtual Environment:**

    **Mac / Linux:**
    ```bash
    python3 -m venv .venv
    source .venv/bin/activate
    ```

    **Windows:**
    ```bash
    python -m venv .venv
    .venv\Scripts\activate
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Configure Environment:**
    Create a `.env` file in the root directory and add your Google API Key:
    ```bash
    GOOGLE_API_KEY=your_api_key_here
    ```

### Usage

**Option 1: CLI (The "Hacker" Way)**
Run the full loop in your terminal.
```bash
python3 -m src.main
# Windows: python -m src.main
```

**Option 2: ADK Web Visualizer (The "Demo" Way)**
See the beautiful agent graph and trace every thought process.
```bash
adk web . --port 8000
```
Then open `http://127.0.0.1:8000`.

---

## ☁️ Deployment (Render.com)

Since this application uses `adk web` (a persistent server), it is best deployed on platforms like **Render** or **Railway** that support Docker.

1.  **Push your code** to a GitHub repository.
2.  **Sign up** for [Render.com](https://render.com).
3.  **Create a New Web Service**:
    -   Connect your GitHub repo.
    -   Select **Docker** as the Runtime.
    -   **Environment Variables**: Add `GOOGLE_API_KEY`.
4.  **Deploy**: Render will build the Docker image and start the `adk web` server.

---

## 📂 Project Structure

```
multi_personas_agent/
├── agent.py                  # ADK Web Entry Point (Root)
├── src/
│   ├── agents/
│   │   ├── personas.py       # The Council (Analyst, Critic, Optimist, etc.)
│   │   ├── router.py         # Dynamic selection logic
│   │   ├── mediator.py       # The CEO/Synthesis agent
│   │   └── podcaster.py      # 🎙️ The Scriptwriter
│   ├── data/
│   │   └── memory_bank.json  # 🧠 Shared Memory
│   ├── flows/
│   │   └── system.py         # Orchestration (Parallel -> Sequential)
│   ├── tools/
│   │   └── expert_tool.py    # 🦆 DuckDuckGo Search Tool
│   ├── main.py               # CLI Entry Point
│   └── agent.py              # Internal ADK Entry Point
├── requirements.txt          # Dependencies
├── Dockerfile                # Deployment Configuration
└── .env                      # API Keys
```
