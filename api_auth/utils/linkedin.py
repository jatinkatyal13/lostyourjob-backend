from api_auth.models import User

from decouple import config
import requests
import json

def exchangeGrantCode(code):
  url = 'https://www.linkedin.com/oauth/v2/accessToken'
  data = {
    'grant_type': 'authorization_code',
    'code': code,
    'redirect_uri': 'http://localhost:3000/login/linkedin',
    'client_id': config('LINKEDIN_CLIENT_ID'),
    'client_secret': config('LINKEDIN_CLIENT_SECRET')
  }

  resp = requests.post(url, data = data)
  resp.raise_for_status()
  resp = json.loads(resp.content)

  return resp['access_token']

def getName(nameObj):
  locale = nameObj['preferredLocale']['language'] + '_' + nameObj['preferredLocale']['country']
  return nameObj['localized'][locale]
def getProfilePicture(profilePictureObj):
  if not profilePictureObj:
    return ''

  for pics in profilePictureObj['displayImage~']['elements']:
    if pics['authorizationMethod'] == 'PUBLIC':
      return pics['identifiers'][0]['identifier']
  
  return ''

def getUserFromAccessToken(accessToken):
  '''
    Fetches or creates the User in the DB
    using the LinkedIn response
  '''

  url = 'https://api.linkedin.com/v2/me'
  params = {
    'projection': '(id,firstName,lastName,maidenName,profilePicture(displayImage~:playableStreams))'
  }
  headers = {
    'Authorization': f'Bearer {accessToken}'
  }
  respUser = requests.get(url, headers = headers, params = params)
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
      'photo': getProfilePicture(respUser['profilePicture']),
      'role': 'seeker'
    }
  )

  return user
