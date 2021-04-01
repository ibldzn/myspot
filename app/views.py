from app import app
from app.utils.spotifai import get_track_data
from flask import render_template, url_for, redirect, request
from spotipy import SpotifyOAuth
from dotenv import dotenv_values


@app.route("/")
def index():
    return render_template("index.html", track_data=get_track_data())

@app.route("/redirect_auth")
def redirect_auth():
    cfg = dotenv_values(".spotify.env")
    if not cfg:
        return render_template("error/auth.html",
                            message="Unable find .spotify.env file!")

    code = request.args["code"]
    auth = SpotifyOAuth(client_id=cfg["CLIENT_ID"],
                     client_secret=cfg["CLIENT_SECRET"],
                     scope="user-read-currently-playing",
                     redirect_uri=url_for("redirect_auth", _external=True))
    auth.get_access_token(code)

    return redirect("/")
