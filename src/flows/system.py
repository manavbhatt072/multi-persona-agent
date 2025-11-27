from google.adk.agents import ParallelAgent, SequentialAgent
from src.agents.personas import create_personas
from src.agents.mediator import create_mediator

def build_council_system():
    
    # 1. Get the LlmAgents (Personas and Mediator)
    personas_list = create_personas()
    mediator = create_mediator()

    # 2. Parallelize the Council (Concept 1: Parallel Agents)
    # This sends the prompt to all 5 personas simultaneously.
    council_layer = ParallelAgent(
        name="Council_Layer",
        sub_agents=personas_list
    )

    # 3. Sequence the Flow (Concept 2: Sequential Agents - The Root)
    # The SequentialAgent executes the flow: 
    # (Council runs in parallel) -> (Mediator synthesizes output)
    main_flow = SequentialAgent(
        name="Multi_Persona_Council",
        sub_agents=[council_layer, mediator]
    )

    return main_flow