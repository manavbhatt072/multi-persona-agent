# Multi-Persona Council Agent

A powerful agentic AI system built with the **Google Agent Development Kit (ADK)**. This project implements a "Council of Personas" architecture where multiple specialized AI agents brainstorm on a topic in parallel, followed by a Mediator agent that synthesizes their diverse perspectives into a comprehensive action plan.

## 🚀 Features

-   **Multi-Persona Architecture**: Spawns 5 distinct personas to analyze a prompt from different angles:
    -   **Analyst**: Focuses on data, feasibility, and metrics.
    -   **Critic**: Identifies weaknesses, risks, and edge cases.
    -   **Optimist**: Highlights benefits, opportunities, and best-case scenarios.
    -   **Creative Thinker**: Generates out-of-the-box ideas and metaphors.
    -   **Domain Expert**: Provides practical, domain-specific tactics using tools.
-   **Mediator Synthesis**: A dedicated agent that resolves conflicts and combines all reports into a final **Synthesized Action Plan**.
-   **Parallel Execution**: Uses `ParallelAgent` to run all council members simultaneously for efficiency.
-   **ADK Web Integration**: Fully compatible with `adk web` for visual debugging and trace analysis.

## 🛠️ Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/manavbhatt072/multi-persona-agent.git
    cd multi-persona-agent
    ```

2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Set up Environment Variables:**
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

This project is open for collaboration! Feel free to fork the repository, submit Pull Requests, or open Issues for improvements.
