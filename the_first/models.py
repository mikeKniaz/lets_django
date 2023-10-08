from django.db import models
from django.contrib.auth.models import User
import requests
from django.core.cache import cache
from encrypted_secrets import get_secret

class Track(models.Model):
    name = models.CharField()
    artist = models.CharField()
    spotify_id = models.CharField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    image_url = models.CharField()

    @classmethod
    def spotify_track_search(cls, text):
        access_token = Track.spotify_access_token()
        headers = { 'Authorization': f'Bearer {access_token}', 'Content-Type': 'application/x-www-form-urlencoded' }
        payload = { 'q': text, 'type': 'track'}
        r = requests.get('https://api.spotify.com/v1/search', params=payload, headers=headers)
        return map(Track.build, r.json()['tracks']['items'])
    
    
    def spotify_access_token():
        spotify_access_token = cache.get('spotify_access_token')
        if not spotify_access_token:
            auth = requests.auth.HTTPBasicAuth(get_secret("spotify_client_id"),get_secret("spotify_client_secret"))
            data = { 'grant_type': 'client_credentials' }
            rjson = requests.post('https://accounts.spotify.com/api/token', data=data, auth=auth).json()
            cache.set('spotify_access_token', rjson['access_token'], rjson['expires_in'])
            spotify_access_token = cache.get('spotify_access_token')
        return spotify_access_token
    
    def build(tjson):
        print(tjson)
        return Track(name=tjson['name'],
                     artist=tjson['artists'][0]['name'],
                     spotify_id=tjson['id'],
                     image_url=tjson['album']['images'][0]['url'])