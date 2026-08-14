"""
AI Poker Agent - Real-Time WebSocket Client
Author: Hakob Nahapetyan
Event Context: Built during The AI Collective Yerevan Hackathon
"""

import asyncio
import json
import websockets
from game_state import parse_game_state
from strategy import decide_action

async def poker_client(server_uri, bot_name, invite_code):
    """Establishes persistent connection to the platform host."""
    
    async with websockets.connect(server_uri) as websocket:
        print(f"Connected to {server_uri}. Registering as {bot_name}...")
        
        # 1. Register with the platform
        register_payload = {
            "type": "register",
            "bot_name": bot_name,
            "invite_code": invite_code
        }
        await websocket.send(json.dumps(register_payload))
        
        # 2. Listen to the event stream
        try:
            async for message in websocket:
                data = json.loads(message)
                event_type = data.get("type")
                
                # Handle game lifecycle events
                if event_type == "lifecycle":
                    print(f"Game Status: {data.get('message')}")
                    
                # Handle actionable turns within the 30s auto-fold window
                elif event_type == "turn":
                    print("\n--- Action Required ---")
                    
                    # Parse state and calculate strategy
                    current_state = parse_game_state(data)
                    action = decide_action(current_state)
                    
                    # Dispatch action to server
                    print(f"Dispatching Action: {action}")
                    await websocket.send(json.dumps(action))
                    
        except websockets.exceptions.ConnectionClosed:
            print("Connection to the dealer server was closed.")

if __name__ == "__main__":
    # Example ngrok endpoint provided by platform admins
    SERVER_URI = "wss://crushing-swear-unseen.ngrok-free.dev"
    asyncio.run(poker_client(SERVER_URI, "MaratBot", "POKER-TEST"))