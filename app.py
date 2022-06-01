from flask import Flask, request, jsonify
from TikTokApi import TikTokApi
import asyncio
from videos_api import get_videos
app = Flask(__name__)

proxy = "http://213.137.240.243:81"
api = TikTokApi(proxy=proxy)

@app.route('/scrap-profile', methods = ['POST'])
def scrap_profile():
    input_json = request.get_json(force=True)
    username = input_json['username']
    user = api.user(username=username)
    response = user.as_dict
    return response


@app.route('/scrap-videos', methods = ['POST'])
def scrap_videos():
    input_json = request.get_json(force=True)
    username = input_json['username']
    response = get_videos(username)
    obj = {}
    obj["videos"] = response
    return obj
    