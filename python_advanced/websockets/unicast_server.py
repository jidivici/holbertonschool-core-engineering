#!/usr/bin/env python3
"""WebSocket server demonstrating unicast communication."""
import asyncio
import websockets

connected_clients = set()


async def connection_handler(websocket):
    """Track the connection and reply only to its sender."""
    connected_clients.add(websocket)
    try:
        async for message in websocket:
            await websocket.send(f"U:{message}")
    finally:
        connected_clients.discard(websocket)


async def main():
    """Start the WebSocket server and run it forever."""
    async with websockets.serve(connection_handler, "localhost", 8765):
        await asyncio.Future()


if __name__ == "__main__":
    asyncio.run(main())
