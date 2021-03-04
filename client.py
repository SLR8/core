import asyncio
import websockets

async def client():
    uri = "ws://localhost:8765"

    async with websockets.connect(uri) as websocket:
        name = input("Whats your name sir ? ")

        await websocket.send(name)
        print(f"< {name}")

        greeting = websocket.recv()
        print(f"> {greeting}")

asyncio.get_event_loop().run_until_complete(client())