from flask import Flask, request, flash
from pymessenger.bot import Bot
from random import choice

app = Flask(__name__)

ACCESS_TOKEN = "EAAMNcc7EHe4BAGf4LMt9PomKcRy8ggmOorGTCCZBHkrfiXJViMbKeAhySBZBG75BPuJ4bokiZB2SrmVQGr6j9MZC9vWBARc07gArZBq4lgtZB7gXTp5ur4IH7rEZAz78nJjZCH7nsTQIZC5Pv9adoWZCRBnCioZAwxcYX6yO127VCKRqcgM1hLqwEyZBsY1DP3gI9IIZD"
VERIFY_TOKEN = "c2b834b6-110f-11eb-adc1-0242ac120002"
bot = Bot(ACCESS_TOKEN)


@app.route("/", methods=['GET', 'POST'])
def verificar_token():
    if request.method == 'GET':
        if request.args.get("hub.verify_token") == VERIFY_TOKEN:
            return request.args.get("hub.challenge")
        else:
            return 'Token invalido'

    if request.method == 'POST':
        output = request.get_json()
        for event in output['entry']:
            messaging = event['messaging']
            for mensaje in messaging:
                if mensaje.get('message'):
                    recipient_id = mensaje['sender']['id']
                    btn_payload1 = [
                        {
                            "type":"web_url",
                            "url" : "https://github.com/",
                            "title":"Github"
                        },
                        {
                            "type":"web_url",
                            "url" : "https://www.google.com/",
                            "title":"Google"
                        },
                        {
                            "type":"web_url",
                            "url" : "https://www.facebook.com/",
                            "title":"Facebook"
                        }
                    ]
                    bot.send_button_message(recipient_id = recipient_id,
                        text = "¿Qué página desea ingresar?",
                        buttons = btn_payload1
                    )

                    btn_payload2 = [
                        {
                            "type":"phone_number",
                            "title":"👨‍💻☎️",
                            "payload":"988776655"
                        },
                        {
                            "type":"phone_number",
                            "title":"👨‍🔧📞",
                            "payload":"944332211"
                        }
                    ]
                    bot.send_button_message(recipient_id = recipient_id,
                        text = "¿Con quién desea hablar?",
                        buttons = btn_payload2
                    )

                    btn_payload3 = [
                        {
                            "type":"postback",
                            "title":"--Opción 3--",
                            "payload":"USER_DEFINED_PAYLOAD"
                        },
                    ]
                    bot.send_button_message(recipient_id = recipient_id,
                        text = "Selecc. la opción 3",
                        buttons = btn_payload3
                    )
                        
        return "Success"

if __name__ == "__main__":
    app.run(port=5000, debug=True)