function sendMessage() {
    var userInput = document.getElementById("user-input").value;
    // Add user's message to the chat history
    addMessage("user", userInput);
    // Send the message to your backend logic.py for processing
    // Update chat history with the response
}

function addMessage(sender, message) {
    var chatHistory = document.getElementById("chat-history");
    var messageElement = document.createElement("div");
    messageElement.className = sender === "user" ? "message user-message" : "message bot-message";
    messageElement.innerText = message;
    chatHistory.appendChild(messageElement);
}
