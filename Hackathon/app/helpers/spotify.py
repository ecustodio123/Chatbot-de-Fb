from requests import get

AUTH_ENDPOINT = 'https://accounts.spotify.com/authorize'
SEARCH_ENDPOINT = 'https://api.spotify.com/v1/search'
GET_ARTIST_ENDPOINT = '	https://api.spotify.com/v1/artists/{id}'
RELATED_ARTIST_ENDPOINT = 'https://api.spotify.com/v1/artists/{id}/related-artists'
TOP_TRACKS_ENDPOINT = 'https://api.spotify.com/v1/artists/{id}/top-tracks'
TOKEN_FIELD = 'BQBxShMjnduLGtmgQ2ygDKBkrIt59xC4YrT2XrjPuqfGPmGLywwt5LmTKVopa1Y51XI_UZUfyWy9UKEBtgn_V89h_C30SfdOU-703vrFjiTty_DGLClqGIiX0C0w_Sq2--2akarM1_UmZjWbmAINHS6PIB2C0Zc2VnB4QvvBwfpoupk-NHGXRxWRRkEBk_kk3J7XpTkffKMdnf18xffeXmz3qfincHbvUP8O8iBmU34SCzBNh7s8r_wOMi9lFfmwg0xeSOtL66rBGaF5vJ-s'

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