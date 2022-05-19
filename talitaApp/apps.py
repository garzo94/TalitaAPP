from django.apps import AppConfig
from django.contrib.auth import logout


class TalitaappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'talitaApp'

    def ready(self):
        import talitaApp.signals 

    

def social_user(backend, uid, user=None, *args, **kwargs):
    provider = backend.name
    social = backend.strategy.storage.user.get_social_auth(provider, uid)
    if social:
        if user and social.user != user:
            logout(backend.strategy.request)
        elif not user:
            user = social.user
    return {'social': social,
            'user': user,
            'is_new': user is None,
            'new_association': False}

