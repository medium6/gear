from .base import *

INSTALLED_APPS += ['storages',]


# False if not in os.environ
DEBUG = env('DEBUG_PRO')
ALLOWED_HOSTS = ALLOWED_HOSTS

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': env('ENGINE_PRO'),
        'NAME': env('NAME_PRO'),
        'USER': env('USER_PRO'),
        'PASSWORD': env('PASSWORD_PRO'),
        'HOST': env('HOST_PRO'),
        'Port': env('Port_PRO'),        
    }
}

MEDIA_ROOT = os.path.join(BASE_DIR, '')


AWS_ACCESS_KEY_ID = 'AKIAXTYJAYMTEVL3ESFI'
AWS_SECRET_ACCESS_KEY = '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'
AWS_STORAGE_BUCKET_NAME = 'gear-bucket'
AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
AWS_S3_OBJECT_PARAMETERS = {
    'CacheControl': 'max-age=86400',
}
AWS_LOCATION = 'static'
STATIC_URL = '/static/'

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, '')

STATIC_URL = 'https://%s/%s/' % (AWS_S3_CUSTOM_DOMAIN, AWS_LOCATION)
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

DEFAULT_FILE_STORAGE = 'src.settings.storage_backends.MediaStorage'