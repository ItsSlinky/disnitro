import pymongo
import requests
from pymongo import MongoClient

cluster = MongoClient("mongodb+srv://disinvi:Khgg2JJwS5Aq201o@cluster0.yu7kv.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

db1 = cluster["disnitro"]
refresh_tokensdb = db1["refresh_tokens"]


API_ENDPOINT = 'https://discord.com/api/v8'
CLIENT_ID = '951169249269911582'
CLIENT_SECRET = 'xjZyYB1KeUlUaN1bxa5D9JYTUbhqOFXH'
REDIRECT_URI = 'https://google.com'

def exchange_code(code):
  data = {
    'client_id': CLIENT_ID,
    'client_secret': CLIENT_SECRET,
    'grant_type': 'authorization_code',
    'code': code,
    'redirect_uri': REDIRECT_URI
  }
  headers = {
    'Content-Type': 'application/x-www-form-urlencoded'
  }
  r = requests.post('%s/oauth2/token' % API_ENDPOINT, data=data, headers=headers)
  r.raise_for_status()
  return r.json()
