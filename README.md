# 👩🏻‍💻 AI-powered Student Support Chatbot (ALP)

This prototype is an AI-powered chatbot developed to deliver automated student support through a question-and-answer interface. It is implemented using Azure Bot Services in conjunction with QnA Maker for natural language processing and knowledge retrieval. The chatbot is fully integrated into a web-based self-service portal, enabling students to access support resources independently and efficiently.

For a lab overview: https://letisiapangataa.github.io/posts/student-support-chatbot-ai/

---

### Project Structure

```
student-support-chatbot
├── bot
│   ├── app.py                # Main app logic for the chatbot
│   └── requirements.txt      # Python dependencies
├── qna
│   └── knowledge-base.tsv     # Knowledge base for QnA Maker
├── web
│   ├── index.html            # Main HTML file for the web portal
│   ├── styles.css            # Styles for the web portal
│   └── chatbot.js            # JavaScript for chatbot interactions
└── README.md                 # Project documentation
```

### Technologies

- Azure Bot Framework
- QnA Maker
- HTML/CSS
- JavaScript

### How-To-Setup

1. **Clone the repository:**
   ```
   git clone https://github.com/letisiapangataa/student-support-chatbot.git
   cd student-support-chatbot
   ```

2. **Set up the bot:**
   - Navigate to the `bot` directory.
   - Install the required Python packages:
     ```
     pip install -r requirements.txt
     ```

3. **Configure QnA Maker:**
   - Create a QnA Maker resource in Azure.
   - Upload the `knowledge-base.tsv` file to set up your knowledge base.

4. **Run the chatbot:**
   - Execute the `app.py` file to start the bot.

5. **Access the web portal:**
   - Open `index.html` in a web browser to interact with the chatbot.

### Guide

- Use the chatbot to ask frequently asked questions related to student support.
- The chatbot will respond based on the knowledge base provided in the `knowledge-base.tsv` file.

### Contributors

Feel free to submit issues or pull requests to improve the chatbot and its functionalities.

---

## Disclaimer

This project was developed using a combination of publicly available learning resources, reference books, open source projects, and artificial intelligence tools. All efforts have been made to attribute and comply with relevant licenses. Contributions and insights from the broader open source and educational communities are gratefully acknowledged. This software is provided as-is, without warranty of any kind, express or implied. The author assumes no responsibility for any loss, damage, or disruption caused by the use of this code. It is intended for educational and experimental purposes only and may not be suitable for production environments.
