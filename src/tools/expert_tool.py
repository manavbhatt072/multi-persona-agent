from google.adk.tools import FunctionTool
import json
import os
from duckduckgo_search import DDGS

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

def perform_web_search(topic: str) -> dict:
    """Performs a real web search to find market data."""
    print(f"[Tool]: Searching the web for '{topic}' market data...")
    
    search_data = {
        "topic": topic,
        "market_size_usd": "Unknown",
        "trend": "Unknown",
        "risk_factor": "Unknown",
        "actionable_tactic": "Unknown",
        "sources": []
    }

    try:
        # Use a context manager for DDGS
        with DDGS() as ddgs:
            # Search for market size and trends
            query = f"{topic} market size trends risks {2024}"
            # Add a timeout/retry logic implicitly by catching errors below
            results = list(ddgs.text(query, max_results=4))
            
            if results:
                # Naive extraction - in a real app, we'd use an LLM to parse this text.
                # Here we just aggregate the snippets for the Expert Agent to read.
                combined_text = " ".join([r['body'] for r in results])
                search_data["raw_search_context"] = combined_text
                search_data["sources"] = [r['href'] for r in results]
                
                # We leave the specific fields as "See Context" because the LLM (Expert) 
                # will parse the 'raw_search_context' better than regex.
                search_data["market_size_usd"] = "See raw_search_context"
                search_data["trend"] = "See raw_search_context"
                search_data["risk_factor"] = "See raw_search_context"
                search_data["actionable_tactic"] = "Derived from search context"
            else:
                print("[Tool]: No results found.")
                search_data["raw_search_context"] = "Search returned no results. Rely on general knowledge."

    except Exception as e:
        print(f"[Tool Error]: {e}")
        search_data["raw_search_context"] = f"Search failed due to error: {str(e)}. Please rely on your internal knowledge."
        # Fallback to prevent crash
        search_data["actionable_tactic"] = "Search unavailable. Providing general best practices."
    
    return search_data

# Define the function that acts as the "tool" for the Domain Expert
def get_industry_metrics(topic: str) -> str:
    """
    Retrieves current industry data, market trends, and key performance indicators (KPIs)
    related to the given business topic. Checks long-term memory first, then searches the web.
    """
    print(f"\n[Tool Called]: Searching for metrics related to '{topic}'...")

    # 1. Check Memory Bank
    memory = load_memory()
    if topic in memory:
        print(f"[Memory Bank]: Found cached data for '{topic}'.")
        return json.dumps(memory[topic])

    # 2. Real Web Search
    real_data = perform_web_search(topic)
    
    # 3. Save to Memory Bank
    memory[topic] = real_data
    save_memory(memory)
    print(f"[Memory Bank]: Saved new data for '{topic}'.")

    # The tool should return a structured string (like JSON) for the LLM to easily parse.
    return json.dumps(real_data)

# Register the tool instance
INDUSTRY_TOOL = FunctionTool(get_industry_metrics)