from flask import Flask, request, jsonify
from botbuilder.core import BotFrameworkAdapter, BotFrameworkAdapterSettings
from botbuilder.schema import Activity
from qna import QnAMaker, QnAMakerEndpoint

app = Flask(__name__)

# Azure Bot Framework settings
APP_ID = "YOUR_APP_ID"
APP_PASSWORD = "YOUR_APP_PASSWORD"
adapter_settings = BotFrameworkAdapterSettings(APP_ID, APP_PASSWORD)
adapter = BotFrameworkAdapter(adapter_settings)

# QnA Maker settings
qna_endpoint = QnAMakerEndpoint(
    knowledge_base_id="YOUR_KB_ID",
    endpoint_key="YOUR_ENDPOINT_KEY",
    host="YOUR_HOST"
)
qna_maker = QnAMaker(qna_endpoint)

@app.route("/api/messages", methods=["POST"])
def messages():
    body = request.json
    activity = Activity().deserialize(body)

    async def handle_message():
        if activity.type == "message":
            response = await qna_maker.get_answers_async(activity)
            if response:
                await adapter.send_activity(Activity(type="message", text=response[0].answer))
            else:
                await adapter.send_activity(Activity(type="message", text="Sorry, I don't have an answer for that."))
    
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(handle_message())
    return jsonify({"status": "message processed"})

if __name__ == "__main__":
    app.run(port=3978)