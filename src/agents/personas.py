from google.adk.agents import LlmAgent
from src.tools.expert_tool import INDUSTRY_TOOL
# Using Flash for speed and cost-efficiency in parallel execution
FLASH_MODEL = "gemini-2.5-flash" 

def create_personas():
    # --- 1. Analyst: Data and Feasibility ---
    analyst = LlmAgent(
        name="Analyst",
        model=FLASH_MODEL,
        instruction="You are a meticulous Analyst. Focus strictly on data, feasibility, metrics, and quantifiable risks. Provide supporting evidence."
    )

    # --- 2. Critic: Weaknesses and Pitfalls ---
    critic = LlmAgent(
        name="Critic",
        model=FLASH_MODEL,
        instruction="You are the Critic. Your sole goal is to find weaknesses, edge cases, vulnerabilities, and potential disasters. Be highly skeptical."
    )

    # --- 3. Optimist: Benefits and Motivation ---
    optimist = LlmAgent(
        name="Optimist",
        model=FLASH_MODEL,
        instruction="You are the unwavering Optimist. Highlight only the benefits, potential upsides, best-case scenarios, and motivational factors. Be inspiring."
    )

    # --- 4. Creative Thinker: Out-of-the-Box Ideas ---
    creative = LlmAgent(
        name="Creative_Thinker",
        model=FLASH_MODEL,
        instruction="You are a Creative Thinker. Give three out-of-the-box ideas, metaphors, or unusual, non-obvious approaches to the topic."
    )

    # --- 5. Domain Expert: Practical Tactics (uses Tool) ---
    expert = LlmAgent(
        name="Domain_Expert",
        model=FLASH_MODEL,
        instruction="You are a Domain Expert. You MUST use your available tool to retrieve practical, domain-specific tactics and market data.",
        tools=[INDUSTRY_TOOL] # <--- Attaching the Tool
    )

    return [analyst, critic, optimist, creative, expert]