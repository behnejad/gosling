TEMPLATE_DEBUG = DEBUG = True
from os.path import dirname
PROJECT_DIRS = dirname(dirname(__file__)).replace('\\', '/')
MANAGERS = ADMINS = (
    ('Hooman Behnejad', 'hoomanbehnejad@gmail.com'),
)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': PROJECT_DIRS + '/db.sqlite3'
    },
}
MEDIA_URL = '/media/'
MEDIA_ROOT = PROJECT_DIRS + MEDIA_URL
STATIC_ROOT = STATIC_URL = '/statics/'
STATIC_SERVER = ''
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST = 'localhost'
# EMAIL_PORT = '8025'
# EMAIL_HOST_USER = ''
# EMAIL_HOST_PASSWORD = ''
EMAIL_USE_TLS = True
# EMAIL_USE_SSL = False
ATOMIC_REQUESTS = True
ROOT_URLCONF = 'gosling.urls'
WSGI_APPLICATION = 'gosling.wsgi.application'
ALLOWED_HOSTS = ('*')
APPEND_SLASH = True
TIME_ZONE = 'Asia/Tehran'
LANGUAGE_CODE = 'en-us'
TEST_RUNNER = 'django.test.runner.DiscoverRunner'
SECRET_KEY = 'ekio2*kn65@yaijb8vli-)z%6n#!a7*)n%zv)c#3&&0@q-7eyg'
SITE_ID = 1
USE_I18N = True
USE_L10N = True
USE_TZ = False
LANGUAGES = (('en', 'English'), )
INTERNAL_IPS = ('127.0.0.1', )
SESSION_COOKIE_AGE = 60 * 60 * 8
CSRF_COOKIE_AGE = 60 * 60 * 8
# SESSION_ENGINE = "django.contrib.sessions.backends.signed_cookies"
# MESSAGE_STORAGE = 'django.contrib.messages.storage.cookie.CookieStorage'
STATICFILES_DIRS = (
    '/'.join((PROJECT_DIRS, "statics")),
)
TEMPLATE_DIRS = (
    '/'.join((PROJECT_DIRS, 'templates')),
)
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'django.contrib.staticfiles.finders.DefaultStorageFinder',
    'dajaxice.finders.DajaxiceFinder',
)
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    'django.template.loaders.eggs.Loader',
)
TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.request',
    'django.core.context_processors.csrf',
    'django.contrib.messages.context_processors.messages'
)
MIDDLEWARE_CLASSES = (
    # 'django.middleware.cache.UpdateCacheMiddleware',
    # 'django.middleware.cache.FetchFromCacheMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)
PASSWORD_HASHERS = (
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
    'django.contrib.auth.hashers.BCryptSHA256PasswordHasher',
    'django.contrib.auth.hashers.BCryptPasswordHasher',
    'django.contrib.auth.hashers.SHA1PasswordHasher',
    'django.contrib.auth.hashers.MD5PasswordHasher',
    'django.contrib.auth.hashers.UnsaltedSHA1PasswordHasher',
    'django.contrib.auth.hashers.UnsaltedMD5PasswordHasher',
    'django.contrib.auth.hashers.CryptPasswordHasher',
)
INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'django.contrib.admindocs',
    'dajaxice',
    'user',
)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        },
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        },
        'console': {
            'level': 'INFO',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
        },
        'null': {
            'class': 'logging.NullHandler',
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['console'],
            'level': 'ERROR',
            'propagate': True,
        },
        'dajaxice': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
        'django': {
            'handlers': ['console'],
        },
        'django.security': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': False,
        },
        'py.warnings': {
            'handlers': ['console'],
        },
    }
}
