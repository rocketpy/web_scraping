#  WebSocket Docs:  https://websockets.readthedocs.io/en/stable/

# client sends and receives messages:
import asyncio
import websockets

async def hello():
    uri = "ws://localhost:8765"
    async with websockets.connect(uri) as websocket:
        await websocket.send("Hello world!")
        await websocket.recv()

asyncio.get_event_loop().run_until_complete(hello())

