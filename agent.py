# multi_personas_agent/agent.py

from src.flows.system import build_council_system

# ADK requires the final orchestrating agent to be named 'root_agent'
# This assigns your complete SequentialAgent flow to that required variable.
root_agent = build_council_system()