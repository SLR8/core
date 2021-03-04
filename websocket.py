import asyncio
import websockets
import socket
import time

def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # doesn't even have to be reachable
        s.connect(('10.255.255.255', 1))
        IP = s.getsockname()[0]
    except Exception:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP


async def server(websocket, path):
    print(path)
    await websocket.send("Hello there")
   
    while True:
        message = await websocket.recv()
        print(message)

        await websocket.send(f"Command {message}, was done succesfully")




ip_addr = get_ip()
port = 8000
start_server = websockets.serve(server, ip_addr, port)
print(f"Starting server on host:{ip_addr}  port:{port}")

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()