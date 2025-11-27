# from google.adk.agents.llm_agent import Agent

# root_agent = Agent(
#     model='<FILL_IN_MODEL>',
#     name='root_agent',
#     description='A helpful assistant for user questions.',
#     instruction='Answer user questions to the best of your knowledge',
# )

import os
from dotenv import load_dotenv
from src.flows.system import build_council_system # <-- Import the full flow

# Load environment variables from .env file
load_dotenv()

# Define agent_app at module level for adk web
agent_app = build_council_system()

if __name__ == "__main__":
    
    # ⚠️ Environment Check
    if not os.getenv("GOOGLE_API_KEY"):
        print("ERROR: GOOGLE_API_KEY not found in .env file.")
        exit()

    print("--- Initializing Multi-Persona Council Agent ---")
    
    # 1. Build the full agent system (SequentialAgent wrapping ParallelAgent)
    # agent_app is already defined above
    
    user_prompt = input("Enter the topic/prompt for the Council: ")
    
    print("\n--- Running Council Layers (Parallel Execution)... ---")
    
    # 2. Run the system using InMemoryRunner
    from google.adk.runners import InMemoryRunner, types, print_event
    
    APP_NAME = "multi_persona_agent"
    runner = InMemoryRunner(agent=agent_app, app_name=APP_NAME)
    
    # Create a session first
    session_id = "session_1"
    user_id = "user_1"
    runner.session_service.create_session_sync(
        app_name=APP_NAME,
        user_id=user_id,
        session_id=session_id
    )
    
    # Construct the content
    content = types.Content(parts=[types.Part(text=user_prompt)], role="user")
    
    # Run the agent
    events = runner.run(
        user_id=user_id,
        session_id=session_id,
        new_message=content
    )
    
    print("\n" + "="*50)
    print("FINAL SYNTHESIZED ACTION PLAN")
    print("="*50)
    
    # Iterate over events and print them
    for event in events:
        # We only want to print the final response from the model, or meaningful events.
        # print_event(event) prints everything which is good for debugging but maybe too much for the user.
        # Let's print everything for now to ensure we see the output.
        print_event(event)
        
    print("="*50)
