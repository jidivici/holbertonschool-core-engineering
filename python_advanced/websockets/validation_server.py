#!/usr/bin/env python3
"""Minimal WebSocket echo server."""
import asyncio
import websockets


async def connection_handler(websocket):
    """Echo back every text message received on the connection."""
    async for message in websocket:
        if message == "":
            await websocket.send("ERR:EMPTY")
        else:
            await websocket.send(f"Ok:{message}")


async def main():
    """Start the WebSocket server and run it forever."""
    async with websockets.serve(connection_handler, "localhost", 8765):
        await asyncio.Future()


if __name__ == "__main__":
    asyncio.run(main())
