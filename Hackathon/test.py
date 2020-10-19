from flask import Flask, request
from pymessenger.bot import Bot
from random import choice

app = Flask(__name__)

ACCESS_TOKEN = "EAAMNcc7EHe4BAGf4LMt9PomKcRy8ggmOorGTCCZBHkrfiXJViMbKeAhySBZBG75BPuJ4bokiZB2SrmVQGr6j9MZC9vWBARc07gArZBq4lgtZB7gXTp5ur4IH7rEZAz78nJjZCH7nsTQIZC5Pv9adoWZCRBnCioZAwxcYX6yO127VCKRqcgM1hLqwEyZBsY1DP3gI9IIZD"
VERIFY_TOKEN = "c2b834b6-110f-11eb-adc1-0242ac120002"
bot = Bot(ACCESS_TOKEN)


@app.route("/", methods=['GET', 'POST'])
def hello():
    if request.method == 'GET':
        if request.args.get("hub.verify_token") == VERIFY_TOKEN:
            return request.args.get("hub.challenge")
        else:
            return 'Token invalido'
        print(hola)

    if request.method == 'POST':
        mensaje = ["Bienvenido!", "Hola", "¿Cómo estas", "¿Qué tal?", "¿Te ayudo en algo?", "¿Qué tal tu día", "¿Primera vez por acá?", "Te invitamos a seguirnos", "Ya le diste like a la página?"]
        mensaje = choice(mensaje)
        output = request.get_json()
        for event in output['entry']:
            messaging = event['messaging']
            for x in messaging:
                if x.get('message'):
                    recipient_id = x['sender']['id']
                    if x['message'].get('text'):
                        message = x['message']['text']
                        bot.send_text_message(recipient_id, mensaje)
                    if x['message'].get('attachments'):
                        for att in x['message'].get('attachments'):
                            bot.send_attachment_url(recipient_id, att['type'], att['payload']['url'])
                else:
                    pass
        return "Success"


if __name__ == "__main__":
    app.run(port=5000, debug=True)