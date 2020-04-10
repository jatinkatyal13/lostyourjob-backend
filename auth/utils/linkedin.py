from decouple import config
import requests
import json

def exchangeGrantCode(code):
  url = 'https://www.linkedin.com/oauth/v2/accessToken'
  data = {
    'grant_type': 'authorization_code',
    'code': code,
    'redirect_uri': 'http://localhost:3000/auth/linkedin',
    'client_id': config('LINKEDIN_CLIENT_ID'),
    'client_secret': config('LINKEDIN_CLIENT_SECRET')
  }

  resp = requests.post(url, data = data)
  resp = json.loads(resp.content)

  return resp['access_token']

def getUserFromAccessToken(accessToken):
  url = 'https://api.linkedin.com/v2/me'
  headers = {
    'Authorization': f'Bearer ${accessToken}'
  }

  return requests.get(url, headers = headers)
