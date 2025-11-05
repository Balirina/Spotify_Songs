import os
import spotipy
import pandas as pd
from variables import id, secret, uri
import sys

from spotipy.oauth2 import SpotifyOAuth

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=id,
    client_secret=secret,
    redirect_uri=uri
))

mis_tracks = []

# Search for a singer
artista = input('Introduce el nombre de un cantante: ')
try:
    results = sp.search(q=f'artist:{artista}', type='artist', limit=1)
except:
    sys.exit()
mi_artista = results['artists']['items'][0]
mi_artista_name = mi_artista['name']
mi_artista_id = mi_artista['id']

# Get albums
albums = sp.artist_albums(mi_artista['id'], album_type='album')
for album in albums['items']:
    
    # Get tracks for this album
    tracks = sp.album_tracks(album['id'])
    
    for track in tracks['items']:
        mis_tracks.append({
            'artist_id': mi_artista_id,
            'artist_name': mi_artista_name,
            'album_name': album['name'],
            'album_release_date': album['release_date'],
            'track_name': track['name']
        })

df = pd.DataFrame(mis_tracks)

#Save the tracks into a json file
df.to_json(f'canciones_{mi_artista_name}.json', orient='records', indent=2)

#Save the tracks into a csv file
df.to_csv(f'canciones_{mi_artista_name}.csv')