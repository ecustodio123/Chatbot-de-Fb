from flask import Flask, request
from pymessenger.bot import Bot
from random import choice
# from app.helpers.spotify import search_by_artist_name, get_artist, get_artist_top_tracks, get_related_artists
from app.routes.index import search_post
from requests import get


############################################################
############################################################

AUTH_ENDPOINT = 'https://accounts.spotify.com/authorize'
SEARCH_ENDPOINT = 'https://api.spotify.com/v1/search'
GET_ARTIST_ENDPOINT = '	https://api.spotify.com/v1/artists/{id}'
RELATED_ARTIST_ENDPOINT = 'https://api.spotify.com/v1/artists/{id}/related-artists'
TOP_TRACKS_ENDPOINT = 'https://api.spotify.com/v1/artists/{id}/top-tracks'
TOKEN_FIELD = 'BQBnrrrOTmaiW4WpJ0jTRSrrQcRrMwv3pzTOVOikqhak9_qHGa_guVQ9ODLQs3vRLLrFlLS1MsH-kAWqCIXikOi0evl6JFpk6IcCFRgq5VmysxcHaTRXvmNJ8U5Qq46QoIYzRfVSa7TBC3pxpFnig-65aCjkeuwDo9kgjv9-xVhPkIlwmyTzMOTsjqq6ctLHzHuLr5ZiEjEtXMjj_El2MHVI7u3VByGExSXwZ6m3ok0rdpdbX8w8xzs5GFRvQ0h6X97B4xH5Fe9rdcxM70E1'

def auth_token():
    return TOKEN_FIELD

def search_by_artist_name(name):
    params = { 'type': 'artist' }
    params['q'] = name
    token = auth_token()
    headers = {
        "Authorization" : f"Bearer {token}"
    }
    response = get(SEARCH_ENDPOINT, params=params, headers=headers)
    return response.json()

def get_artist(artist_id):
    url = GET_ARTIST_ENDPOINT.format(id=artist_id)
    token = auth_token()
    headers = {
        "Authorization" : f"Bearer {token}"
    }
    response = get(url, headers=headers)
    return response.json()

def get_related_artists(artist_id):
    url = RELATED_ARTIST_ENDPOINT.format(id=artist_id)
    token = auth_token()
    headers = {
        "Authorization" : f"Bearer {token}"
    }
    response = get(url, headers=headers)
    return response.json()

def get_artist_top_tracks(artist_id, market='US'):
    url = TOP_TRACKS_ENDPOINT.format(id=artist_id)
    params = {'market' : market}
    token = auth_token()
    headers = {
        "Authorization" : f"Bearer {token}"
    }
    response = get(url, params=params, headers=headers)
    return response.json()

##################################################################
##################################################################


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
                        data = search_by_artist_name(message)
                        print(data)
                        api_url = data['external_urls']['spotify']
                        # items = data['artists']['items']
                        bot.send_text_message(recipient_id, api_url)

                    if x['message'].get('attachments'):
                        for att in x['message'].get('attachments'):
                            bot.send_attachment_url(recipient_id, att['type'], att['payload']['url'])
                else:
                    pass
        return "Success"


if __name__ == "__main__":
    app.run(port=5000, debug=True)