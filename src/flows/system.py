from google.adk.agents import ParallelAgent, SequentialAgent
# --- ADK PRIMITIVES: ParallelAgent & SequentialAgent ---
# ParallelAgent: Executes multiple sub-agents simultaneously. We use this for the "Council"
# so that the Analyst, Critic, and Optimist can "think" at the same time, reducing total wait time.
#
# SequentialAgent: Executes sub-agents in a strict order, passing the output of one as input to the next.
# We use this for the high-level flow: Council (Parallel) -> Mediator (Sequential) -> Podcaster (Sequential).
from src.agents.personas import create_personas
from src.agents.mediator import create_mediator
from src.agents.router import create_router

def get_router():
    return create_router()

def build_dynamic_council(selected_persona_names):
    """
    Builds a ParallelAgent containing only the selected personas.
    
    --- ROUTING / FILTERING LOGIC ---
    This function implements the dynamic selection logic.
    1. It receives a list of 'selected_persona_names' from the Router Agent.
    2. It filters the master list of personas to include ONLY those requested.
    3. It constructs a new ParallelAgent on the fly with this custom subset.
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