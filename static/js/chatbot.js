document.getElementById('chat-form').addEventListener('submit', async function(event) {
    event.preventDefault();
    const userInput = document.getElementById('user-input').value;
    if (userInput.trim() === '') return;
 
    // Send user input to the chatbot
    const response = await fetch('/chatbot_response', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ message: userInput })
    });
    const result = await response.json();
    const botResponse = result.response;
 
    // Display bot response only
    const chatLog = document.getElementById('chat-log');
    const botMessageDiv = document.createElement('div');
    botMessageDiv.classList.add('message', 'bot-message');
    botMessageDiv.textContent = botResponse;
    chatLog.appendChild(botMessageDiv);
 
    // Scroll to the bottom of the chat log
    chatLog.scrollTop = chatLog.scrollHeight;
 
    // Clear the input
    document.getElementById('user-input').value = '';
});
