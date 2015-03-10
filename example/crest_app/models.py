from django.contrib.auth.models import AbstractUser
from django.utils.functional import cached_property

import dateutil.parser
import time


class EveUser(AbstractUser):
    """custom User class to work with django-social-auth"""

    @cached_property
    def _eve_auth(self):
        """shortcut to python-social-auth's EVE-related extra data for this user"""
        return self.social_auth.get(provider='eveonline').extra_data

    def _get_crest_tokens(self):
        """get tokens for authenticated CREST"""
        expires_in = time.mktime(
            dateutil.parser.parse(
                self._eve_auth['expires']  # expiration time string
            ).timetuple()                             # expiration timestamp
        ) - time.time()                               # seconds until expiration
        return {
            'access_token': self._eve_auth['access_token'],
            'refresh_token': self._eve_auth['refresh_token'],
            'expires_in': expires_in
        }

    @property
    def character_id(self):
        """get CharacterID from authentification data"""
        return self._eve_auth['id']

    def get_portrait_url(self, size=128):
        """returns URL to Character portrait from EVE Image Server"""
        return "https://image.eveonline.com/Character/{0}_{1}.jpg".format(self.character_id, size)
