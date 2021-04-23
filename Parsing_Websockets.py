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


# one more example
"""
def on_message(ws, message):
    print(message)

def on_error(ws, error):
    print(error)

def on_close(ws):
    print("Is closed !")

def on_open(ws):
    def run(*args):
        for i in range(3):
            time.sleep(1)
            ws.send(data_orig)

"""
