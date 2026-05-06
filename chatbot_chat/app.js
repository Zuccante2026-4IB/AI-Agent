document.addEventListener("DOMContentLoaded", function(){
    const SERVER_URL = "http://host.docker.internal:1865"; // <-- change this to your server URL

const messagingArea = document.querySelector(".messaging_area");
const input = document.querySelector(".input_area input");
const sendButton = document.querySelector(".input_area button");


function appendBubble(text, type) {
    const bubble = document.createElement("div");
    bubble.classList.add(type === "user" ? "user_message" : "ai_message");
    bubble.textContent = text;
    messagingArea.appendChild(bubble);
    messagingArea.scrollTop = messagingArea.scrollHeight;
}


async function loadGreeting() {
    try {
        const response = await fetch(SERVER_URL + "/greeting");
        if(!response.ok) throw new Error;
        const data = await response.json();
        appendBubble(data.message, "ai");
    } catch (error) {
        appendBubble("Ciao! Come posso aiutarti?", "ai"); 
        console.error("Errore nel caricamento del saluto:", error);
    }
}


async function sendMessage() {
    const userText = input.value.trim();
    if (!userText) return;

    appendBubble(userText, "user");
    input.value = "";

    try {
        const response = await fetch(SERVER_URL + "/message", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ message: userText })
        });
        const data = await response.json();
        appendBubble(data.message, "ai");
    } catch (error) {
        appendBubble("Errore: impossibile contattare il server.", "ai");
        console.error("Errore nell'invio del messaggio:", error);
    }
}


sendButton.addEventListener("click", sendMessage);

input.addEventListener("keydown", function (event) {
    if (event.key === "Enter") sendMessage();
});


loadGreeting();


});