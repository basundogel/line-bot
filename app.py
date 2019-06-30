from flask import Flask, request, abort  # flask. django 架設伺服器
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, StickerSendMessage
)
app = Flask(__name__)
line_bot_api = LineBotApi('EkWWIL0CK1DOkF0QmVht754ngW4bmC+N92qEfKeB1rngGpBA+0UdFW9E86NOFZH9VLMqk/EfpBds8/0fBJecDlbFvGi4zJQAhC3UxOwBXBxi7j775Zye/t5Fq1QZq7yCkBSH0We6qbJUQKrw+VsZCgdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('b04b21306fefa94452472329612c83df')

@app.route("/callback", methods=['POST'])   # 接收line傳來的訊息
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

@handler.add(MessageEvent, message=TextMessage) # 處理訊息
def handle_message(event):
    msg = event.message.text
    s = '你說什麼'

    if '貼圖' in msg:
        sticker_message = StickerSendMessage(
            package_id='11538',
            sticker_id='51626498'
        )    

        line_bot_api.reply_message(
            event.reply_token,
            sticker_message)
        return # return結束function

    if msg in ['hi', 'Hi', 'HI']:
        s = '你好'
    elif msg == '你幾歲':
        s = '我1歲'
    elif msg == '你是誰':
        s = '我是機器人'
    elif '訂位' in msg:
        s = '你要訂位嗎?'

    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=s))

if __name__ == "__main__":
    app.run()