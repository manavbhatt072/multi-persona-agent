from google.adk.agents import ParallelAgent, SequentialAgent
from src.agents.personas import create_personas
from src.agents.mediator import create_mediator
from src.agents.router import create_router

def get_router():
    return create_router()

def build_dynamic_council(selected_persona_names):
    """
    Builds a ParallelAgent containing only the selected personas.
    """
    all_personas = create_personas() # Returns a dict now
    
    selected_agents = []
    for name in selected_persona_names:
        if name in all_personas:
            selected_agents.append(all_personas[name])
        else:
            print(f"Warning: Persona '{name}' not found.")
            
    if not selected_agents:
        # Fallback if something goes wrong
        print("Warning: No valid personas selected. Using all.")
        selected_agents = list(all_personas.values())

    # Parallelize the Council
    council_layer = ParallelAgent(
        name="Council_Layer",
        sub_agents=selected_agents
    )
    
    return council_layer

def build_council_system():
    """
    Builds the full council system with all personas (for ADK Web visualization).
    """
    # 1. Get all personas
    all_personas_dict = create_personas()
    all_personas_list = list(all_personas_dict.values())
    
    # 2. Parallel Layer
    council_layer = ParallelAgent(
        name="Council_Layer",
        sub_agents=all_personas_list
    )
    
    # 3. Mediator
    mediator = create_mediator()

    # 4. Podcaster
    from src.agents.podcaster import create_podcaster
    podcaster = create_podcaster()
    
    # 5. Sequential Flow
    return SequentialAgent(
        name="Multi_Persona_Council",
        sub_agents=[council_layer, mediator, podcaster]
    )

def get_mediator():
    return create_mediator()