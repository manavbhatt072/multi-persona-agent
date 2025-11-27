from google.adk.agents import LlmAgent
# Using Pro for complex reasoning and synthesis
PRO_MODEL = "gemini-2.5-pro" 

def create_mediator():
    return LlmAgent(
        name="The_Mediator",
        model=PRO_MODEL, 
        instruction="""
        Your role is the final synthesist. You must read all reports from the council (Analyst, Critic, Optimist, Creative, Expert).
        1. **Resolve Conflicts:** Directly address the Critic's risks and integrate the Optimist's benefits.
        2. **Synthesize:** Combine all data into a single, comprehensive strategy.
        3. **Final Output:** Produce a detailed, step-by-step **Synthesized Action Plan**. 
        """
    )