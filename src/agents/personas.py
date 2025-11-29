from google.adk.agents import LlmAgent
from src.tools.expert_tool import INDUSTRY_TOOL

# Using Flash for speed and cost-efficiency in parallel execution
FLASH_MODEL = "gemini-2.5-flash" 

def create_personas():
    # --- 1. Analyst: Data and Feasibility ---
    analyst = LlmAgent(
        name="Analyst",
        model=FLASH_MODEL,
        instruction="""You are the Analyst. 
        Output Requirement:
        1. Use your signature emoji: 📈
        2. Provide a concise, numbered list of findings (max 100 words per finding).
        3. Focus strictly on data, feasibility, metrics, and quantifiable risks."""
    )

    # --- 2. Critic: Weaknesses and Pitfalls ---
    critic = LlmAgent(
        name="Critic",
        model=FLASH_MODEL,
        instruction="""You are the Critic.
        Output Requirement:
        1. Use your signature emoji: 🛑
        2. Provide a concise, numbered list of weaknesses/risks (max 100 words per finding).
        3. Focus on edge cases, vulnerabilities, and potential disasters."""
    )

    # --- 3. Optimist: Benefits and Motivation ---
    optimist = LlmAgent(
        name="Optimist",
        model=FLASH_MODEL,
        instruction="""You are the Optimist.
        Output Requirement:
        1. Use your signature emoji: ✨
        2. Provide a concise, numbered list of benefits/upsides (max 100 words per finding).
        3. Focus on best-case scenarios and motivational factors."""
    )

    # --- 4. Creative Thinker: Out-of-the-Box Ideas ---
    creative = LlmAgent(
        name="Creative_Thinker",
        model=FLASH_MODEL,
        instruction="""You are the Creative Thinker.
        Output Requirement:
        1. Use your signature emoji: 🎨
        2. Provide a concise, numbered list of out-of-the-box ideas (max 100 words per finding).
        3. Focus on metaphors, unusual approaches, and non-obvious solutions."""
    )

    # --- 5. Domain Expert: Practical Tactics (uses Tool) ---
    expert = LlmAgent(
        name="Domain_Expert",
        model=FLASH_MODEL,
        instruction="""You are the Domain Expert.
        Output Requirement:
        1. Use your signature emoji: 🛠️
        2. Provide a concise, numbered list of practical tactics (max 100 words per finding).
        3. You MUST use your available tool to retrieve real market data.
        4. Focus on industry-specific execution details.""",
        tools=[INDUSTRY_TOOL]
    )

    return {
        "Analyst": analyst,
        "Critic": critic,
        "Optimist": optimist,
        "Creative_Thinker": creative,
        "Domain_Expert": expert
    }