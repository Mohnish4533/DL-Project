from dotenv import load_dotenv
import os
import base64
from requests import post, get
import json

load_dotenv()

client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")

def get_token():
    auth_string = client_id + ":" + client_secret
    auth_bytes = auth_string.encode("utf-8")
    auth_base64 = str(base64.b64encode(auth_bytes), "utf-8")

    url = "https://accounts.spotify.com/api/token"
    headers = {
        "Authorization": "Basic " + auth_base64,
        "Content-Type": "application/x-www-form-urlencoded"
    }

    data = {"grant_type": "client_credentials"}
    result = post(url, headers= headers, data= data)

    json_result = json.loads(result.content)
    token = json_result['access_token']

    return token

def get_auth_header(token):
    return {"Authorization": "Bearer " + token}

def get_genre_based_tracks(token, g):
    url = "https://api.spotify.com/v1/recommendations/"
    headers = get_auth_header(token)
    query = f"?seed_genres={g}&limit=10"

    query_url = url + query

    result = get(query_url, headers=headers)

    json_result = json.loads(result.content)['tracks']

    return json_result

token = get_token()

required_genre = input("Enter genre: ")

result = get_genre_based_tracks(token, required_genre)

for idx, song in enumerate(result):
    print(f"{idx + 1}. {song['name']}")

