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

![System Architecture](https://mermaid.ink/img/Zmxvd2NoYXJ0IFRECiAgICBVc2VyKFtVc2VyIElucHV0XSkgLS0+IFJvdXRlclvwn5qmIFJvdXRlciBBZ2VudF0KICAgIFJvdXRlciAtLSBTZWxlY3RzIEV4cGVydHMgLS0+IERlY2lzaW9ue0lzIENoaXRjaGF0P30KICAgIERlY2lzaW9uIC0tIFllcyAtLT4gR3JlZXRlclvwn5KsIEdyZWV0ZXIgQWdlbnRdCiAgICBHcmVldGVyIC0tPiBPdXRwdXQoW0ZpbmFsIFJlc3BvbnNlXSkKICAgIERlY2lzaW9uIC0tIE5vIC0tPiBQMwogICAgc3ViZ3JhcGggQ291bmNpbEJveCBbRHluYW1pYyBDb3VuY2lsIC0gUGFyYWxsZWwgRXhlY3V0aW9uXQogICAgICAgIGRpcmVjdGlvbiBUQgogICAgICAgIFAxW/Cfk4ggQW5hbHlzdF0KICAgICAgICBQMlvwn5uRIENyaXRpY10KICAgICAgICBQM1vinKggT3B0aW1pc3RdCiAgICAgICAgUDRb8J+OqCBDcmVhdGl2ZSBUaGlua2VyXQogICAgICAgIFA1W/Cfm6DvuI8gRG9tYWluIEV4cGVydF0KICAgIGVuZAogICAgUDEgJiBQMiAmIFAzICYgUDQgJiBQNSAtLT4gTWVkaWF0b3Jb4pqW77iPIE1lZGlhdG9yIEFnZW50XQogICAgTWVkaWF0b3IgLS0gU3ludGhlc2l6ZXMgUmVwb3J0cyAtLT4gQ2hlY2t7Q29uc2Vuc3VzIFJlYWNoZWQ/fQogICAgQ2hlY2sgLS0gTm8gKFJlcXVlc3QgUmVmaW5lbWVudCkgLS0+IEZlZWRiYWNrW+KaoO+4jyBGZWVkYmFjayBMb29wXQogICAgRmVlZGJhY2sgLS0+IFAzCiAgICBDaGVjayAtLSBZZXMgKFJlYWR5KSAtLT4gUG9kY2FzdGVyW/CfjpnvuI8gUG9kY2FzdGVyIEFnZW50XQogICAgUG9kY2FzdGVyIC0tPiBPdXRwdXQoW0ZpbmFsIFBvZGNhc3QgU2NyaXB0XSkKICAgIGNsYXNzRGVmIGFnZW50IGZpbGw6I2Y5ZixzdHJva2U6IzMzMyxzdHJva2Utd2lkdGg6MnB4OwogICAgY2xhc3NEZWYgY29udHJvbCBmaWxsOiNmZmQsc3Ryb2tlOiMzMzMsc3Ryb2tlLXdpZHRoOjJweDsKICAgIGNsYXNzRGVmIHN0b3JhZ2UgZmlsbDojZGZkLHN0cm9rZTojMzMzLHN0cm9rZS13aWR0aDoycHg7CiAgICBjbGFzcyBSb3V0ZXIsR3JlZXRlcixNZWRpYXRvcixQb2RjYXN0ZXIsUDEsUDIsUDMsUDQsUDUgYWdlbnQ7CiAgICBjbGFzcyBEZWNpc2lvbixDaGVjayBjb250cm9sOw==)

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
