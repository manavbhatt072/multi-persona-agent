from google.adk.agents import LlmAgent
# Using Pro for complex reasoning and synthesis
# --- HYBRID MODEL STRATEGY ---
# We use Gemini 1.5 Pro for the "Mediator" agent.
# The Mediator requires a larger context window and stronger reasoning capabilities
# to synthesize conflicting reports from multiple agents into a cohesive plan.
# Pro excels at this high-level cognitive task.
PRO_MODEL = "gemini-2.5-pro" 

def create_mediator():
    return LlmAgent(
        name="The_Mediator",
        model=PRO_MODEL, 
        instruction="""
        Your role is to evaluate and synthesize the reports from the council.
        
        You must structure your response into exactly these three markdown sections:

        ## 1. Risk & Regret Analysis
        - Synthesize the inputs from the **Critic** and **Analyst**.
        - Identify the **Top 2 Risks**.
        - For each risk, provide a specific **Mitigation Strategy**.

        ## 2. Strategic Consensus
        - Summarize the convergence of the **Creative Thinker** and **Optimist** viewpoints.
        - Highlight the shared vision or unique opportunity they identified.

        ## 3. Synthesized Action Plan (5 Steps)
        - Create a concrete 5-step execution plan.
        - You MUST present this as a **Markdown Table** with the following columns:
            - **Step Name**
            - **Owner (Persona)**
            - **Estimated Time**
            - **Mitigation (Based on Critic)**
        
        **Special Condition:**
        - If the inputs contain "SKIP" or are mostly empty, and the Greeter has responded, output ONLY the Greeter's response. Do NOT generate a plan.
        - If the input is just a greeting, reply politely and ask for a topic.

        **Rules:**
        - Do not use generic intros or outros. Start directly with Section 1 (unless it's a greeting).
        - Ensure the tone is **professional, executive, and decisive**.
        - Keep all descriptions extremely brief (max 1 sentence per point).
        """
    )