from app import app
from flask import render_template, request
from app.helpers.spotify import search_by_artist_name, get_artist, get_artist_top_tracks, get_related_artists

@app.route('/')
@app.route('/home')
@app.route('/search', methods=['GET'])
def index():
    return render_template('views/home.html')

@app.route('/search', methods=['POST'])
def search_post():
    artista = request.values.get('artista')
    data = search_by_artist_name(artista)
    api_url = data['artists']['href']
    items = data['artists']['items']
    return render_template('views/search.html', artist_name=artista, results=items, api_url=api_url)

@app.route('/artist/<id>')
def artist(id):
    artist = get_artist(id)

    if artist['images']:
        image_url = artist['images'][0]['url']
    else:
        image_url = 'http://via.placeholder.com/600'

    tracksdata = get_artist_top_tracks(id)
    tracks = tracksdata['tracks']

    artistsdata = get_related_artists(id)
    relateds = artistsdata['artists']

    return render_template('views/artist.html', artist=artist, related_artists=relateds, image_url=image_url, tracks=tracks)