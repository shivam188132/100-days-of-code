import spotipy
from spotipy.oauth2 import SpotifyOAuth

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://localhost:8080/callback",
        client_id="3d656f74af9feffe8ccbe9f",
        client_secret="3b5605f679aeeb1598",
        show_dialog=True,
        cache_path="token.txt",
        username="Raja Billa",
    )
)
user_id = sp.current_user()["id"]