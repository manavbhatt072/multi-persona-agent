from google.adk.agents import LlmAgent
from src.tools.expert_tool import INDUSTRY_TOOL

# Using Flash for speed and cost-efficiency in parallel execution
# --- HYBRID MODEL STRATEGY ---
# We use Gemini 1.5 Flash for the "Worker" personas (Analyst, Critic, etc.).
# Flash is optimized for speed and lower latency, which is crucial when running
# multiple agents in parallel. It provides high-quality output for specific,
# narrow tasks without the higher cost/latency of the Pro model.
FLASH_MODEL = "gemini-2.5-flash" 

# --- ADK PRIMITIVE: LlmAgent ---
# The LlmAgent is the fundamental building block of the Google Agent Development Kit.
# It wraps a Gemini model with specific instructions (system prompt) and optional tools.
# Each persona below is an instance of LlmAgent with a unique "personality" and cognitive style. 

def create_personas():
    # --- 1. Analyst: Data and Feasibility ---
    analyst = LlmAgent(
        name="Analyst",
        model=FLASH_MODEL,
        instruction="""You are the Analyst. 
        Output Requirement:
        1. Use your signature emoji: 📈
        2. Provide a concise, numbered list of max 3 findings (max 20 words per finding).
        3. Focus strictly on data, feasibility, metrics, and quantifiable risks.
        4. CRITICAL: If the user input is a simple greeting (e.g. 'hi', 'hello') or chitchat, output ONLY the string 'SKIP'."""
    )

    # --- 2. Critic: Weaknesses and Pitfalls ---
    critic = LlmAgent(
        name="Critic",
        model=FLASH_MODEL,
        instruction="""You are the Critic.
        Output Requirement:
        1. Use your signature emoji: 🛑
        2. Provide a concise, numbered list of max 3 weaknesses/risks (max 20 words per finding).
        3. Focus on edge cases, vulnerabilities, and potential disasters.
        4. CRITICAL: If the user input is a simple greeting (e.g. 'hi', 'hello') or chitchat, output ONLY the string 'SKIP'."""
    )

    # --- 3. Optimist: Benefits and Motivation ---
    optimist = LlmAgent(
        name="Optimist",
        model=FLASH_MODEL,
        instruction="""You are the Optimist.
        Output Requirement:
        1. Use your signature emoji: ✨
        2. Provide a concise, numbered list of max 3 benefits/upsides (max 20 words per finding).
        3. Focus on best-case scenarios and motivational factors.
        4. CRITICAL: If the user input is a simple greeting (e.g. 'hi', 'hello') or chitchat, output ONLY the string 'SKIP'."""
    )

    # --- 4. Creative Thinker: Out-of-the-Box Ideas ---
    creative = LlmAgent(
        name="Creative_Thinker",
        model=FLASH_MODEL,
        instruction="""You are the Creative Thinker.
        Output Requirement:
        1. Use your signature emoji: 🎨
        2. Provide a concise, numbered list of max 3 out-of-the-box ideas (max 20 words per finding).
        3. Focus on metaphors, unusual approaches, and non-obvious solutions.
        4. CRITICAL: If the user input is a simple greeting (e.g. 'hi', 'hello') or chitchat, output ONLY the string 'SKIP'."""
    )

    # --- 5. Domain Expert: Practical Tactics (uses Tool) ---
    expert = LlmAgent(
        name="Domain_Expert",
        model=FLASH_MODEL,
        instruction="""You are the Domain Expert.
        Output Requirement:
        1. Use your signature emoji: 🛠️
        2. Provide a concise, numbered list of max 3 practical tactics (max 20 words per finding).
        3. You MUST use your available tool to retrieve real market data.
        4. Focus on industry-specific execution details.
        5. CRITICAL: If the user input is a simple greeting (e.g. 'hi', 'hello') or chitchat, output ONLY the string 'SKIP'.""",
        tools=[INDUSTRY_TOOL]
    )

    # --- 6. Greeter: Simple Chitchat ---
    greeter = LlmAgent(
        name="Greeter",
        model=FLASH_MODEL,
        instruction="""You are a friendly AI assistant.
        Output Requirement:
        1. Reply naturally, briefly, and politely to the user's greeting or simple question.
        2. Do NOT generate long lists or complex analysis.
        3. Keep it under 2 sentences.
        4. Ask if they have a specific topic to brainstorm about."""
    )

    return {
        "Analyst": analyst,
        "Critic": critic,
        "Optimist": optimist,
        "Creative_Thinker": creative,
        "Domain_Expert": expert,
        "Greeter": greeter
    }