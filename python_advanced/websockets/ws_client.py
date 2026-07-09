#!/usr/bin/env python3
"""Minimal WebSocket client."""
import asyncio
import websockets
import os


async def connect_and_send(uri, text):
    """Connect to uri, send text once, return the single response."""
    async with websockets.connect(uri) as socket:
        await socket.send(text)
        response = await socket.recv()
        return response


async def main():
    """Send 'demo' to the local echo server and print the response."""
    uri = os.getenv("WS_URI", "ws://localhost:8765")
    if uri == "ws://localhost:8765":
        response = await connect_and_send(uri, "Hello WebSocket")
    else:
        response = await connect_and_send(uri, "demo")
    print(response, end="")


if __name__ == "__main__":
    asyncio.run(main())
