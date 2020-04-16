from api_auth.models import User

from decouple import config
import requests
import json

def exchangeGrantCode(code, role):
  url = 'https://www.linkedin.com/oauth/v2/accessToken'
  data = {
    'grant_type': 'authorization_code',
    'code': code,
    'redirect_uri': f'http://localhost:3000/login/linkedin{"?role="+role if role else ""}',
    'client_id': config('LINKEDIN_CLIENT_ID'),
    'client_secret': config('LINKEDIN_CLIENT_SECRET')
  }
  print(data)
  resp = requests.post(url, data = data)
  resp.raise_for_status()
  resp = json.loads(resp.content)

  return resp['access_token']

def getName(nameObj):
  locale = nameObj['preferredLocale']['language'] + '_' + nameObj['preferredLocale']['country']
  return nameObj['localized'][locale]
def getProfilePicture(user, field):
  if not field in user:
    return ''
  
  profilePictureObj = user[field]

  for pics in profilePictureObj['displayImage~']['elements']:
    if pics['authorizationMethod'] == 'PUBLIC':
      return pics['identifiers'][0]['identifier']
  
  return ''

def getUserFromAccessToken(accessToken, role):
  '''
    Fetches or creates the User in the DB
    using the LinkedIn response
  '''

  url = 'https://api.linkedin.com/v2/me'
  params = {
    'projection': '(id,vanityName,firstName,lastName,maidenName,profilePicture(displayImage~:playableStreams))'
  }
  headers = {
    'Authorization': f'Bearer {accessToken}'
  }
  respUser = requests.get(url, headers = headers, params = params)
  print(respUser.content)
  respUser.raise_for_status()
  respUser = json.loads(respUser.content)

  url = 'https://api.linkedin.com/v2/emailAddress'
  params = {
    'q': 'members',
    'projection': '(elements*(handle~))'
  }
  respEmail = requests.get(url, headers = headers, params = params)
  respEmail.raise_for_status()
  respEmail = json.loads(respEmail.content)

  # TODO: fix fetching user
  email = respEmail['elements'][0]['handle~']['emailAddress']
  user, created = User.objects.get_or_create(
    email = email,
    defaults={
      'first_name': getName(respUser['firstName']),
      'last_name': getName(respUser['lastName']),
      'email': email,
      'username': respUser['id'],
      'photo': getProfilePicture(respUser, 'profilePicture'),
      'role': role or 'seeker'
    }
  )

  return user
