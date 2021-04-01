import spotipy
from flask import url_for
from dotenv import dotenv_values
from spotipy.oauth2 import SpotifyOAuth


def get_track_data():
    try:
        cfg = dotenv_values(".spotify.env")
        sp = spotipy.Spotify(auth_manager=
                            SpotifyOAuth(
                                client_id=cfg["CLIENT_ID"],
                                client_secret=cfg["CLIENT_SECRET"],
                                scope="user-read-currently-playing",
                                redirect_uri=url_for("redirect_auth", _external=True))
                            )
        current_track = sp.currently_playing()
        if current_track is None:
            return None

        if current_track["item"]["type"] != "track":
            return None

        artists = current_track["item"]["artists"]
        track_data = {
            "artists": artists[0]["name"] +
                        (f" ft {', '.join(a['name'] for a in artists[1:])}"
                        if len(artists) > 1 else ""),
            "title": current_track["item"]["name"],
            "sp_uri": current_track["item"]["external_urls"]["spotify"],
            "img": current_track["item"]["album"]["images"][0]["url"]
        }

        return track_data

    except Exception:
        return None

