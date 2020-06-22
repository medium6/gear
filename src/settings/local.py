from .base import *

# False if not in os.environ
DEBUG = env('DEBUG_LOCAL')

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': env('ENGINE_LOCAL'),
        'NAME': env('NAME_LOCAL'),
        'USER': env('USER_LOCAL'),
        'PASSWORD': env('PASSWORD_LOCAL'),
        'HOST': env('HOST_LOCAL'),
        'Port': env('Port_LOCAL'),        
    }
}