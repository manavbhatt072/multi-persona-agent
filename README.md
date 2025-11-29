# Multi-Persona Council Agent

**⚠️ Private Repository**

A powerful agentic AI system built with the **Google Agent Development Kit (ADK)**. This project implements a "Council of Personas" architecture where multiple specialized AI agents brainstorm on a topic in parallel, followed by a Mediator agent that synthesizes their diverse perspectives into a comprehensive action plan.

## 🚀 Features

-   **Dynamic Router**: Intelligently selects the most relevant subset of personas based on the user's specific prompt, ensuring focused and efficient brainstorming.
-   **Real-Time Web Intelligence**: The **Domain Expert** is equipped with a live web search tool (DuckDuckGo), allowing it to fetch *actual* market data, trends, and risks instead of relying on hallucinations or mock data.
-   **Multi-Persona Architecture**: Spawns distinct personas (selected by the Router) to analyze a prompt from different angles:
    -   **Analyst**: Focuses on data, feasibility, and metrics.
    -   **Critic**: Identifies weaknesses, risks, and edge cases.
    -   **Optimist**: Highlights benefits, opportunities, and best-case scenarios.
    -   **Creative Thinker**: Generates out-of-the-box ideas and metaphors.
    -   **Domain Expert**: Uses **Live Search** to provide real-world tactics.
-   **Consensus Loop**: A feedback-driven iterative process where the Mediator reviews the council's output. If the plan is insufficient, the Mediator requests refinements (up to 3 iterations) until a consensus is reached.
-   **Mediator Synthesis**: A dedicated agent that resolves conflicts and combines all reports into a final **Synthesized Action Plan**.
-   **🎙️ Podcast Mode**: Automatically converts the final action plan into an engaging, 2-minute dialogue script between the Host, Expert, and Creative, ready for TTS generation.
-   **Parallel Execution**: Uses `ParallelAgent` to run all council members simultaneously for efficiency.
-   **ADK Web Integration**: Fully compatible with `adk web` for visual debugging and trace analysis.

## 🛠️ Installation

1.  **Clone the repository:**
    *Note: You must be an added collaborator to clone this private repository.*
    ```bash
    git clone https://github.com/manavbhatt072/multi-persona-agent.git
    cd multi-persona-agent
    ```

2.  **Create and Activate Virtual Environment:**
    
    *   **macOS / Linux:**
        ```bash
        python3 -m venv venv
        source venv/bin/activate
        ```

    *   **Windows:**
        ```bash
        python -m venv venv
        .\venv\Scripts\activate
        ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Set up Environment Variables:**
    Create a `.env` file in the root directory and add your Google API Key:
    ```bash
    GOOGLE_API_KEY=your_api_key_here
    ```

## 💻 Usage

### Option 1: Command Line Interface (CLI)
Run the agent interactively in your terminal:
```bash
python3 -m src.main
```
You will be prompted to enter a topic, and the agent will display the council's process and the final plan.

### Option 2: ADK Web Visualizer
Visualize the agent's execution flow and traces using the ADK Web UI:
```bash
adk web . --port 8000
```
Then open your browser to `http://127.0.0.1:8000`.

## 📂 Project Structure

```
multi_personas_agent/
├── src/
│   ├── agents/
│   │   ├── personas.py       # Definitions of the 5 council personas
│   │   ├── router.py         # Logic for selecting relevant personas
│   │   └── mediator.py       # Definition of the Mediator agent
│   ├── flows/
│   │   └── system.py         # Orchestration logic (Parallel -> Sequential)
│   ├── tools/
│   │   └── expert_tool.py    # Tools used by the Domain Expert
│   ├── main.py               # Entry point for CLI execution
│   └── agent.py              # Entry point for ADK Web discovery
├── agent.py                  # Root agent definition
├── requirements.txt          # Python dependencies
└── .env                      # Environment variables (not committed)
```

## 🤝 Collaboration

This is a **private repository**. Access is restricted to authorized team members.
To contribute:
1.  Ensure you have been added as a collaborator.
2.  Clone the repo and create a new branch for your feature.
3.  Push your changes and open a Pull Request for review.
