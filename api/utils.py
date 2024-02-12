def get_url_patterns(urlconf=None):
    from django.conf import settings
    from django.urls import get_resolver

    if urlconf is None:
        urlconf = settings.ROOT_URLCONF
    return get_resolver(urlconf).url_patterns