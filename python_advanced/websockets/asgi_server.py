#!/usr/bin/env python3
"""ASGI application serving an HTML page and a WebSocket echo endpoint."""
import os

from starlette.applications import Starlette
from starlette.responses import FileResponse, HTMLResponse
from starlette.routing import Route, WebSocketRoute
BASE_DIR = os.path.dirname(os.path.abspath(__file__))


async def homepage(request):
    """Serve the chat page."""
    with open(os.path.join(BASE_DIR, "index.html")) as f:
        return HTMLResponse(f.read())


async def chat_js(request):
    """Serve the client-side WebSocket script."""
    return FileResponse(os.path.join(BASE_DIR, "chat.js"))


async def styles_css(request):
    """Serve the page stylesheet."""
    return FileResponse(os.path.join(BASE_DIR, "styles.css"))


async def websocket_endpoint(websocket):
    """Accept a connection and echo back every text message received."""
    await websocket.accept()
    while True:
        message = await websocket.receive_text()
        await websocket.send_text(message)


app = Starlette(routes=[
    Route("/", homepage),
    Route("/chat.js", chat_js),
    Route("/styles.css", styles_css),
    WebSocketRoute("/ws", websocket_endpoint),
])
