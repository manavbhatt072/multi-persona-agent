import sys
import os

# Ensure the current directory is in the path so 'src' can be imported
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from google.adk.agents import ParallelAgent, SequentialAgent
from src.agents.personas import create_personas
from src.agents.mediator import create_mediator
from src.agents.podcaster import create_podcaster

# --- Dynamic Router Logic ---
def get_active_personas(topic: str):
    """
    Determines which personas to activate based on the topic keywords.
    """
    all_personas = create_personas()
    
    # 1. Core Personas (Always Run)
    active_names = ['Analyst', 'Critic', 'Optimist']
    
    # 2. Conditional Logic
    topic_lower = topic.lower()
    
    # Creative Trigger
    if any(kw in topic_lower for kw in ['new name', 'abstract', 'unusual', 'creative', 'idea']):
        active_names.append('Creative_Thinker')
        
    # Expert Trigger
    if any(kw in topic_lower for kw in ['market', 'cost', 'industry', 'product', 'business', 'money']):
        active_names.append('Domain_Expert')
        
    # Deduplicate and Fetch Agents
    selected_agents = []
    # Use a set to avoid duplicates if logic overlaps, though list is fine here
    unique_names = list(set(active_names))
    
    print(f"🎯 Router Decision for '{topic}': Activating {unique_names}")
    
    for name in unique_names:
        if name in all_personas:
            selected_agents.append(all_personas[name])
            
    return selected_agents

# --- Build the System ---

# For ADK Web visualization, we need a default topic to build the static graph.
# In a real dynamic app, this would be passed at runtime.
# Let's use a topic that triggers ALL personas for the best demo visualization.
DEMO_TOPIC = "Launch a new abstract product in the shoe industry"

# 1. Get Dynamically Selected Personas
selected_personas = get_active_personas(DEMO_TOPIC)

# 2. Parallel Layer (The Council)
council_layer = ParallelAgent(
    name="Council_Layer",
    sub_agents=selected_personas
)

# 3. Mediator
mediator = create_mediator()

# 4. Podcaster
podcaster = create_podcaster()

# 5. Root Agent (Sequential Flow)
root_agent = SequentialAgent(
    name="Multi_Persona_Council",
    sub_agents=[council_layer, mediator, podcaster]
)