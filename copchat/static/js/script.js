document.getElementById("send-btn").addEventListener("click", sendMessage);

function sendMessage() {
    const userInput = document.getElementById("user-input").value;
    if (userInput.trim() === "") return;

    appendMessage(userInput, "user");


    fetch("http://127.0.0.1:5000/chat", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ mensagem: userInput.toLowerCase() })
    })
    .then(response => response.json())
    .then(data => {
        appendMessage(data.resposta, "bot");
    })
    .catch(error => {
        console.error("Erro:", error);
        appendMessage("Desculpe, ocorreu um erro. Tente novamente.", "bot");
    });


    document.getElementById("user-input").value = "";
}

function appendMessage(message, sender) {
    const chatBox = document.getElementById("chat-box");

    const messageElement = document.createElement("div");
    messageElement.classList.add("message", sender === "user" ? "user-message" : "bot-message");
    messageElement.textContent = message;

    chatBox.appendChild(messageElement);
    chatBox.scrollTop = chatBox.scrollHeight;


}
