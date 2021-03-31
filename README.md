# myspot

A web app that show what song you're listening in spotify
![Screenshot](https://i.imgur.com/7YONKBn.png)

# Running the app

## With Docker

1. Clone this repo by typing `git clone https://github.com/ibldzn/myspot.git` in your terminal
2. Create your own [Spotify App](https://developer.spotify.com/)
3. Make a file named `.spotify.env` in the root folder of this project
4. Insert your Spotify App's client secret and client id in the `.spotify.env` file you just created like this:

```
CLIENT_ID=<your_client_id>
CLIENT_SECRET=<your_client_secret>
```

5. Run `docker build -t myspot .` in your terminal. _Make sure to [install](https://docs.docker.com/get-docker/) it first if you don't have docker installed in your machine_
6. Run `docker run -p 5000:5000 myspot` in your terminal
7. Visit http://127.0.0.1:5000/ in your browser
8. Done, I guess.

## Without Docker

1. Do step 1-4 like explained above
2. Run `cd myspot` in your terminal
3. Run `pip install -r requirements.txt` in your terminal
4. Run `python3 run.py` in your terminal
5. Visit http://127.0.0.1:5000/ in your browser
6. Done, I guess.

# Why?

I just wanted to learn [Docker](https://www.docker.com/), and can't think of any other project to make. Also, yes, I realize how sometimes song's cover image takes up the whole screen but because I can't _unf\*ck_ things without _f\*cking up the other things_ I decided to leave it like that.
