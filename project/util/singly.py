import simplejson
import requests
from django.conf import settings


class Singly(object):

    api_base = 'https://api.singly.com'

    def __init__(self, client_id=None, client_secret=None, access_token=None):
        self.client_id = client_id
        self.client_secret = client_secret
        self.access_token = access_token

    def make_request(self, endpoint, method='GET', request={}):
        url = self.api_base + endpoint

        if method == 'GET':
            if self.access_token is not None:
                request['access_token'] = self.access_token
            response = requests.get(url, params=request)

        elif method == 'POST':
            response = requests.post(url, request)

        else:
            raise ApiError("Unsupported protocol")

        if response.status_code == 200:
            return simplejson.loads(response.content)
        else:
            if settings.DEBUG:
                raise ApiError("%s: %s" % (response.status_code, response.content))
            else:
                raise ApiError("Error returned from API")

    def authorize(self, code):
        endpoint = '/oauth/access_token'
        request = {
            'client_id': self.client_id,
            'client_secret': self.client_secret,
            'code': code
        }
        content = self.make_request(endpoint, 'POST', request)
        return content


class SinglyHelper(object):

    @classmethod
    def get_authorize_url(cls, service, redirect_uri=None):
        if not redirect_uri:
            redirect_uri = settings.SINGLY_REDIRECT_URI
        url = '%s/oauth/authorize?client_id=%s&redirect_uri=%s&service=%s' % (
            Singly.api_base, settings.SINGLY_CLIENT_ID, redirect_uri, service
        )
        return url

    @classmethod
    def get_access_token(cls, code):
        api = Singly(settings.SINGLY_CLIENT_ID, settings.SINGLY_CLIENT_SECRET)
        content = api.authorize(code)
        print content
        "ebf2d584f31ad79130f80eb662d5a012"
        return content


class ApiError(Exception):
    pass