const chatHistory = document.getElementById('chat-history');
const userInput = document.getElementById('user-message');
const sendButton = document.getElementById('send-button');

// Replace with your actual Colab Notebook URL
const colabURL = 'https://colab.research.google.com/drive/1BSooK_kq31fOXmOHC-3AQL5kcl9jpZLp#scrollTo=OqXZIFT968lD'; // Update with your notebook path

async function sendMessage(message) {
  const response = await fetch(colabURL, {
    method: 'POST',
    body: JSON.stringify({ message }),
    headers: { 'Content-Type': 'application/json' }
  });

  const data = await response.json();
  appendMessage(data.text, 'bot-message');
}

function appendMessage(text, className) {
  const messageElement = document.createElement('div');
  messageElement.innerText = text;
  messageElement.className = `chat-message ${className}`;
  chatHistory.appendChild(messageElement);
  chatHistory.scrollTop = chatHistory.scrollHeight;
}

sendButton.addEventListener('click', () => {
  const message = userInput.value.trim();
  if (message) {
    appendMessage(message, 'user-message');
    userInput.value = '';
    sendMessage(message);
  }
});

// Initial greeting from bot (fetched from Colab output)
fetch(colabURL)
  .then(response => response.json())
  .then(data => appendMessage(data.text, 'bot-message'));
