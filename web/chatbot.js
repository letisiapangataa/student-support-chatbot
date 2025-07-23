const botFrameworkWebChat = require('botframework-webchat');

const directLine = botFrameworkWebChat.createDirectLine({ token: 'YOUR_DIRECT_LINE_SECRET' });

const chatContainer = document.getElementById('chatbot');

botFrameworkWebChat.renderWebChat({
    directLine: directLine,
    userID: 'USER_ID',
    username: 'Student Support Bot',
    botAvatarInitials: 'SB',
    userAvatarInitials: 'U',
}, chatContainer);

directLine.activity$.subscribe(activity => {
    if (activity.type === 'message' && activity.from.id === 'YOUR_BOT_ID') {
        // Handle bot messages here
        console.log('Bot says:', activity.text);
    }
});

// Send a message to the bot when the user submits the form
document.getElementById('user-input-form').addEventListener('submit', function(event) {
    event.preventDefault();
    const userInput = document.getElementById('user-input').value;
    directLine.postActivity({
        from: { id: 'USER_ID' },
        type: 'message',
        text: userInput
    }).subscribe(
        id => console.log(`Message sent with id ${id}`),
        error => console.error('Error sending message:', error)
    );
    document.getElementById('user-input').value = ''; // Clear input field
});