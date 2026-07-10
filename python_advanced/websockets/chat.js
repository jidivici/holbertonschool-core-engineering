const statusEl = document.getElementById("status");
const messages = document.getElementById("messages");
const form = document.getElementById("form");
const usernameInput = document.getElementById("username");
const input = document.getElementById("input");

const socket = new WebSocket(`ws://${window.location.host}/ws`);

function timestamp() {
    return new Date().toLocaleTimeString([], { hour: "2-digit", minute: "2-digit" });
}

function addSystemMessage(text) {
    const line = document.createElement("div");
    line.className = "system";
    line.textContent = text;
    messages.appendChild(line);
    messages.scrollTop = messages.scrollHeight;
}

function addBubble(author, text, kind) {
    const bubble = document.createElement("div");
    bubble.className = `bubble ${kind}`;

    if (kind === "received") {
        const name = document.createElement("div");
        name.className = "author";
        name.textContent = author;
        bubble.appendChild(name);
    }

    const body = document.createElement("span");
    body.className = "text";
    body.textContent = text;
    bubble.appendChild(body);

    const time = document.createElement("span");
    time.className = "time";
    time.textContent = timestamp();
    bubble.appendChild(time);

    messages.appendChild(bubble);
    messages.scrollTop = messages.scrollHeight;
}

socket.addEventListener("open", () => {
    statusEl.textContent = "Connected";
    statusEl.className = "connected";
    addSystemMessage("Connected to server");
});

socket.addEventListener("message", (event) => {
    addBubble("Server", event.data, "received");
});

socket.addEventListener("close", () => {
    statusEl.textContent = "Disconnected";
    statusEl.className = "disconnected";
    addSystemMessage("Disconnected from server");
});

form.addEventListener("submit", (event) => {
    event.preventDefault();
    const message = input.value.trim();
    if (!message || socket.readyState !== WebSocket.OPEN) return;

    const username = usernameInput.value.trim() || "Anonymous";
    addBubble(username, message, "sent");
    socket.send(message);
    input.value = "";
    input.focus();
});
