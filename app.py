from flask import Flask, request, abort  # flask. django 架設伺服器

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

line_bot_api = LineBotApi('EkWWIL0CK1DOkF0QmVht754ngW4bmC+N92qEfKeB1rngGpBA+0UdFW9E86NOFZH9VLMqk/EfpBds8/0fBJecDlbFvGi4zJQAhC3UxOwBXBxi7j775Zye/t5Fq1QZq7yCkBSH0We6qbJUQKrw+VsZCgdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('b04b21306fefa94452472329612c83df')


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    msg = event.message.text
    s = '我看不懂耶'

    if msg in ['hi', 'Hi', 'HI']:
        s = '哈囉'
    elif msg == '你幾歲':
        s = '我6歲'
    elif '訂位' in msg:
        S = '你想訂位嗎?'
    ELIF msg == '你是誰':
        S = '我是機器人'


    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=s))


if __name__ == "__main__":
    app.run()