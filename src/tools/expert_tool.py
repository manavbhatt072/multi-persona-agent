from google.adk.tools import FunctionTool
import json
import os

# Define the path to the memory bank
MEMORY_FILE = "src/data/memory_bank.json"

def load_memory():
    if not os.path.exists(MEMORY_FILE):
        return {}
    with open(MEMORY_FILE, "r") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return {}

def save_memory(memory):
    with open(MEMORY_FILE, "w") as f:
        json.dump(memory, f, indent=4)

# Define the function that acts as the "tool" for the Domain Expert
def get_industry_metrics(topic: str) -> str:
    """
    Retrieves current industry data, market trends, and key performance indicators (KPIs)
    related to the given business topic. Checks long-term memory first.
    """
    print(f"\n[Tool Called]: Searching for metrics related to '{topic}'...")

    # 1. Check Memory Bank
    memory = load_memory()
    if topic in memory:
        print(f"[Memory Bank]: Found cached data for '{topic}'.")
        return json.dumps(memory[topic])

    # 2. If not in memory, generate mock data (Simulating API call)
    mock_data = {
        "topic": topic,
        "market_size_usd": "2.5 billion",
        "trend": "5% growth forecast next year, driven by sustainability.",
        "risk_factor": "Regulatory changes in Europe are a high risk.",
        "actionable_tactic": "Focus marketing efforts on Gen Z through short-form video content."
    }
    
    # 3. Save to Memory Bank
    memory[topic] = mock_data
    save_memory(memory)
    print(f"[Memory Bank]: Saved new data for '{topic}'.")

    # The tool should return a structured string (like JSON) for the LLM to easily parse.
    return json.dumps(mock_data)

# Register the tool instance
INDUSTRY_TOOL = FunctionTool(get_industry_metrics)