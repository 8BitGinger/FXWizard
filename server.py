import obspython as obs
import asyncio
import threading
import sys

# Attempt to import the library and report failure to the log
try:
    import websockets
    HAS_WEBSOCKETS = True
except ImportError:
    HAS_WEBSOCKETS = False

clients = set()

async def socket_handler(websocket):
    clients.add(websocket)
    try:
        async for message in websocket:
            # Broadcast to all connected clients (Controller and Display)
            if clients:
                # Filter for open connections only
                active_clients = [c for c in clients if c.open]
                if active_clients:
                    await asyncio.gather(*[c.send(message) for c in active_clients])
    except Exception as e:
        print(f"FXWizard Connection Error: {e}")
    finally:
        if websocket in clients:
            clients.remove(websocket)

def run_server(loop):
    asyncio.set_event_loop(loop)
    try:
        # Binding to 0.0.0.0 is often more reliable than localhost in local networks
        start_server = websockets.serve(socket_handler, "0.0.0.0", 8080)
        loop.run_until_complete(start_server)
        print("FXWizard: Server listening on port 8080...")
        loop.run_forever()
    except Exception as e:
        print(f"FXWizard Server Failed to Start: {e}")

def script_description():
    return "FXWizard Internal WebSocket Server (Port 8080)"

def script_load(settings):
    if not HAS_WEBSOCKETS:
        print("CRITICAL ERROR: 'websockets' library not found!")
        print(f"OBS is looking in: {sys.path[0]}")
        print("Try: 'python -m pip install websockets' in the environment linked to OBS.")
        return

    # Start the server in a background thread
    loop = asyncio.new_event_loop()
    t = threading.Thread(target=run_server, args=(loop,), daemon=True)
    t.start()
    print("FXWizard: Python Server Thread Initiated.")