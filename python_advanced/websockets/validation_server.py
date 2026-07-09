#!/usr/bin/env python3
"""WebSocket server with basic message validation."""
import asyncio
import websockets


async def connection_handler(websocket):
    """Validate each incoming message and reply OK: or ERR:EMPTY."""
    try:
        async for message in websocket:
            if len(message.strip()) == 0:
                await websocket.send("ERR:EMPTY")
            else:
                await websocket.send(f"OK:{message}")
    except websockets.exceptions.ConnectionClosed:
        pass


async def main():
    """Start the WebSocket server and run it forever."""
    async with websockets.serve(connection_handler, "localhost", 8765):
        await asyncio.Future()


if __name__ == "__main__":
    asyncio.run(main())
