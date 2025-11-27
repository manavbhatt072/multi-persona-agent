from google.adk.tools import FunctionTool
import json

# Define the function that acts as the "tool" for the Domain Expert
def get_industry_metrics(topic: str) -> str:
    """
    Retrieves current industry data, market trends, and key performance indicators (KPIs)
    related to the given business topic. Use this when asked for practical,
    real-world, or numerical domain-specific advice.
    """
    print(f"\n[Tool Called]: Searching for metrics related to '{topic}'...")

    # *** IMPORTANT: Replace this with a real API call or database query ***
    mock_data = {
        "topic": topic,
        "market_size_usd": "2.5 billion",
        "trend": "5% growth forecast next year, driven by sustainability.",
        "risk_factor": "Regulatory changes in Europe are a high risk.",
        "actionable_tactic": "Focus marketing efforts on Gen Z through short-form video content."
    }
    
    # The tool should return a structured string (like JSON) for the LLM to easily parse.
    return json.dumps(mock_data)

# Register the tool instance
INDUSTRY_TOOL = FunctionTool(get_industry_metrics)