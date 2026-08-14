import asyncio
import json
import websockets

async def mock_dealer(websocket):
    print("Platform: A bot connected. Waiting for registration...")
    
    # 1. Receive registration
    reg_message = await websocket.recv()
    print(f"Platform: Received -> {reg_message}")
    
    # 2. Send lifecycle event
    await websocket.send(json.dumps({
        "type": "lifecycle",
        "message": "Tournament starting. Blinds are 100/200."
    }))
    
    await asyncio.sleep(2) # Pause for dramatic effect
    
    # 3. Send a fake turn (Pre-flop, dealt Ace-King)
    fake_turn = {
        "type": "turn",
        "round": "pre-flop",
        "hole_cards": [["A", "Spades"], ["K", "Hearts"]],
        "community_cards": [],
        "pot": 300,
        "call_amount": 200,
        "stack": 1860,
        "active_players": 4
    }
    print("Platform: Sending turn to bot...")
    await websocket.send(json.dumps(fake_turn))
    
    # 4. Wait for the bot's decision
    decision = await websocket.recv()
    print(f"Platform: Bot decided -> {decision}")
    
    print("Platform: Closing connection.")

async def main():
    print("Starting mock dealer server on ws://localhost:8765...")
    async with websockets.serve(mock_dealer, "localhost", 8765):
        await asyncio.Future()  # run forever

if __name__ == "__main__":
    asyncio.run(main())