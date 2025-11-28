import os
import json
import re
from dotenv import load_dotenv
from google.adk.runners import InMemoryRunner, types, print_event
from src.flows.system import get_router, build_dynamic_council, get_mediator
from google.adk.agents import SequentialAgent

# Load environment variables
load_dotenv()

def parse_router_output(output_text):
    """Extracts the JSON list of personas from the Router's output."""
    try:
        # Attempt to find a JSON list in the text
        match = re.search(r'\[.*\]', output_text, re.DOTALL)
        if match:
            json_str = match.group(0)
            return json.loads(json_str)
        return json.loads(output_text)
    except Exception as e:
        print(f"Error parsing Router output: {e}")
        # Fallback
        return ["Analyst", "Optimist", "Domain_Expert"]

if __name__ == "__main__":
    
    # ⚠️ Environment Check
    if not os.getenv("GOOGLE_API_KEY"):
        print("ERROR: GOOGLE_API_KEY not found in .env file.")
        exit()

    print("--- Initializing Multi-Persona Agent with Routing & Loop ---")
    
    user_prompt = input("Enter the topic/prompt for the Council: ")
    
    # --- Step 1: Router Agent ---
    print("\n--- 1. 🚦 Router Agent: Selecting Experts... ---")
    router = get_router()
    router_runner = InMemoryRunner(agent=router, app_name="router_app")
    
    # Run Router
    router_runner.session_service.create_session_sync(
        app_name="router_app",
        user_id="user_1",
        session_id="session_router"
    )
    
    events = router_runner.run(
        user_id="user_1",
        session_id="session_router",
        new_message=types.Content(parts=[types.Part(text=user_prompt)], role="user")
    )
    
    # Capture Router Output
    router_output = ""
    for event in events:
        # print_event(event) # Optional: print router steps
        if hasattr(event, 'content') and event.content and event.content.parts:
             router_output = event.content.parts[0].text

    print(f"Router Decision: {router_output}")
    selected_personas = parse_router_output(router_output)
    print(f"Selected Personas: {selected_personas}")

    # --- Step 2: Build Dynamic Council ---
    print("\n--- 2. 🏗️ Building Council... ---")
    council_layer = build_dynamic_council(selected_personas)
    mediator = get_mediator()
    
    # Create the Iteration Unit (Council -> Mediator)
    iteration_agent = SequentialAgent(
        name="Council_Iteration",
        sub_agents=[council_layer, mediator]
    )
    
    # --- Step 3: The Consensus Loop ---
    print("\n--- 3. 🔁 Entering Consensus Loop... ---")
    
    # We use a new runner for the main loop
    main_runner = InMemoryRunner(agent=iteration_agent, app_name="council_app")
    session_id = "session_main"
    user_id = "user_1"
    
    # Initialize Session
    main_runner.session_service.create_session_sync(
        app_name="council_app",
        user_id=user_id,
        session_id=session_id
    )

    current_input = user_prompt
    max_loops = 3
    
    for i in range(max_loops):
        print(f"\n--- Loop {i+1}/{max_loops} ---")
        
        # Run the iteration
        events = main_runner.run(
            user_id=user_id,
            session_id=session_id,
            new_message=types.Content(parts=[types.Part(text=current_input)], role="user")
        )
        
        # Capture Mediator's Output
        last_response = ""
        for event in events:
            print_event(event)
            if hasattr(event, 'content') and event.content and event.content.parts:
                last_response = event.content.parts[0].text
        
        # Check for Stop Condition
        if "READY_FOR_SYNTHESIS" in last_response:
            print("\n✅ Mediator is satisfied. Consensus reached!")
            break
        else:
            print("\n⚠️ Mediator requested refinement. Looping back...")
            # Prepare input for next loop (Feedback)
            current_input = "The Mediator has provided feedback. Council, please update your reports based on the feedback above."

    print("\n" + "="*50)
    print("🏁 FINAL OUTCOME")
    print("="*50)
    # The last response from the loop IS the final plan (or the critique if it failed)
    print(last_response)
    print("="*50)
