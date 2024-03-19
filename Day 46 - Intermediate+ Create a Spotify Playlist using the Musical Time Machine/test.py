import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# Replace 'your_client_id' and 'your_client_secret' with your actual Spotify API credentials
client_id = '3d656f9feffe8ccbe9f'
client_secret = "3b5605f67c83aeeb1598"

# Initialize the Spotify client with the credentials
client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

def search_song(song_name):
    results = sp.search(q=song_name, type='track', limit=1)
    if results['tracks']['items']:
        track = results['tracks']['items'][0]
        track_name = track['name']
        artist_name = track['artists'][0]['name']
        album_name = track['album']['name']
        preview_url = track['preview_url']

        print(f"Track Name: {track_name}")
        print(f"Artist: {artist_name}")
        print(f"Album: {album_name}")
        print(f"Preview URL: {preview_url}")
    else:
        print(f"No results found for '{song_name}'.")

if __name__ == "__main__":
    song_name_to_search = input("enter the song name: ")  # Replace with the song you want to search for
    search_song(song_name_to_search)
user_id = sp.current_user()["id"]
playlist = sp.user_playlist_create(user=user_id, name=" Billboard 100", public=False)
print(playlist)
