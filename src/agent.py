import sys
import os

# Add the parent directory to sys.path to allow imports from 'src'
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.flows.system import build_council_system

# ADK requires the final orchestrating agent to be named 'root_agent'
root_agent = build_council_system()
