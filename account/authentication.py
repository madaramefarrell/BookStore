from django.contrib.auth.models import User
from django.contrib.auth.backends import BaseBackend


class EmailAuthBackend((BaseBackend)):
    """
    Authenticate against the settings ADMIN_LOGIN and ADMIN_PASSWORD.

    Use the login name and a hash of the password. For example:

    ADMIN_LOGIN = 'admin'
    ADMIN_PASSWORD = 'pbkdf2_sha256$30000$Vo0VlMnkR4Bk$qEvtdyZRWTcOsCnI/oQ7fVOu1XAURIZYoOZ3iq8Dr4M='
    """
    print('hello')

    def authenticate(self, request, username=None, password=None):
        try:
            print('username is {}'.format(username))
            user = User.objects.get(email=username)
            print('user is {}'.format(user))
            if user.check_password(password):
                return user
            return None
        except User.DoesNotExist:
            return None


    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
