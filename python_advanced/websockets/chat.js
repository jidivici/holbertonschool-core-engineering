const statusEl = document.getElementById("status");
const messages = document.getElementById("messages");
const form = document.getElementById("form");
const usernameInput = document.getElementById("username");
const input = document.getElementById("input");

const socket = new WebSocket(`ws://${window.location.host}/ws`);

function timestamp() {
    return new Date().toLocaleTimeString([], { hour: "2-digit", minute: "2-digit" });
}

function addMessage(text, kind) {
    const line = document.createElement("div");
    line.className = `message ${kind}`;
    line.textContent = text;
    messages.appendChild(line);
    messages.scrollTop = messages.scrollHeight;
}

socket.addEventListener("open", () => {
    statusEl.textContent = "Connected";
    statusEl.className = "connected";
    addMessage("Connected to server.", "system");
});

socket.addEventListener("message", (event) => {
    addMessage(`[${timestamp()}] Server: ${event.data}`, "received");
});

socket.addEventListener("close", () => {
    statusEl.textContent = "Disconnected";
    statusEl.className = "disconnected";
    addMessage("Disconnected from server.", "system");
});

form.addEventListener("submit", (event) => {
    event.preventDefault();
    const message = input.value.trim();
    if (!message || socket.readyState !== WebSocket.OPEN) return;

    const username = usernameInput.value.trim() || "Anonymous";
    addMessage(`[${timestamp()}] ${username}: ${message}`, "sent");
    socket.send(message);
    input.value = "";
    input.focus();
});
