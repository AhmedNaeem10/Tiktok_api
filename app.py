from flask import Flask, request, jsonify
from TikTokApi import TikTokApi
import os
from dotenv import load_dotenv
from videos_api import get_videos

load_dotenv()

app = Flask(__name__)

proxy = os.getenv("proxy")
api = TikTokApi(proxy=proxy)

@app.route('/scrape-profile', methods = ['POST'])
def scrap_profile():
    input_json = request.get_json(force=True)
    username = input_json['username']
    user = api.user(username=username)
    response = user.as_dict
    return response


@app.route('/scrape-videos', methods = ['POST'])
def scrap_videos():
    input_json = request.get_json(force=True)
    username = input_json['username']
    response = get_videos(username)
    obj = {}
    obj["videos"] = response
    return obj
    