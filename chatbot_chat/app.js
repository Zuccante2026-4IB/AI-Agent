document.addEventListener("DOMContentLoaded", function () {
    const SERVER_URL = "http://host.docker.internal:1865"; // <-- change this to your server URL

    const chatarea = document.querySelector(".chatarea");
    const input = document.querySelector(".inputarea input");
    const sendButton = document.querySelector(".inputarea button");


    function appendBubble(text, type) {
        const messageRow = document.createElement("div");
        messageRow.classList.add(type === "user" ? "messagerow-user" : "messagerow-ai");
        
        if (type === "ai") {
            const messageRowAi = document.createElement("div");
            messageRowAi.classList.add("messagerow-ai");
            let s = '';
            s += '<img src="background.jpg" alt="AI Avatar">';
            s += '<div class="message-ai">' + text + '</div>';
            messageRowAi.innerHTML = s;
            chatarea.appendChild(messageRowAi);
        } else {
            const messageRow = document.createElement("div");
            messageRow.classList.add("messagerow-user");
            let s = '';
            s += '<div class="message-user">' + text + '</div>';
            s += '<img src="background.jpg" alt="User Avatar">';
            messageRow.innerHTML = s;
            chatarea.appendChild(messageRow);
        }
        
        chatarea.scrollTop = chatarea.scrollHeight;
    }


    async function loadGreeting() {
        try {
            const response = await fetch(SERVER_URL + "/greeting");
            if (!response.ok) throw new Error;
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