#
# Для конфигурирования в ходе разработки используйте dev.py, а не этот файл.
#
from os.path import dirname


PATH_PROJECT = dirname(dirname(__file__))
PATH_DATA = '%s/data' % PATH_PROJECT

####################################################################

SITE_URL = 'http://pythonz.net'

PROJECT_SOURCE_URL = 'https://github.com/idlesign/pythonz'
DEBUG = True

PATH_CERTIFICATE = None
CERTIFICATE_SELF_SIGNED = False

PATH_DEBUG_LOG = '/tmp/pythonz_debug.log'

SECRET_KEY = 'not_a_secret'
ADMINS = ()

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': '%s/db/data.db' % PATH_DATA,
    }
}

SERVER_EMAIL = 'some@email.com'
EMAIL_HOST = 'some.host.com'
EMAIL_HOST_USER = 'some@email.com'
EMAIL_HOST_PASSWORD = 'not_a_secret'
EMAIL_USE_TLS = True


# Здесь указываются партнёрские идентификаторы.
PARTNER_IDS = {}


GOOGLE_API_KEY = 'not_a_secret'
YANDEX_SEARCH_ID = 'not_a_secret'

TELEGRAM_BOT_TOKEN = 'not_a_secret'
TELEGRAM_BOT_URL = 'not_a_secret'
TELEGRAM_GROUP = 'group_id or @channel_name'

VK_ACCESS_TOKEN = 'not_a_secret'
VK_GROUP = 'group id prefixed with -'

FB_ACCESS_TOKEN = 'not_a_secret'

# Сюда помещаются реквизиты для пользования соответствующими службами доставки сообщений (cм. sitemessages.py).
SITEMESSAGES_SETTINGS = {
    'twitter': [],
    'smtp': [
        SERVER_EMAIL,
        EMAIL_HOST_USER,
        EMAIL_HOST_PASSWORD,
        EMAIL_HOST,
        None,
        EMAIL_USE_TLS
    ],
    'telegram': [TELEGRAM_BOT_TOKEN],
    'fb': [FB_ACCESS_TOKEN],
    'vk': [VK_ACCESS_TOKEN],
}

# Переводит проект в агрессивный режим: задействует различную машинерию для привлечения внимания к проекту.
AGRESSIVE_MODE = False

####################################################################

SITEMESSAGE_INIT_BUILTIN_MESSAGE_TYPES = False
SITEMESSAGE_DEFAULT_SHORTCUT_EMAIL_MESSAGES_TYPE = 'simple'
ROBOTS_CACHE_TIMEOUT = 24 * 60 * 60

MANAGERS = ADMINS

SITE_ID = 1

AUTH_USER_MODEL = 'apps.User'

TIME_ZONE = 'Asia/Novosibirsk'
LANGUAGE_CODE = 'ru'
ROOT_URLCONF = 'urls'
WSGI_APPLICATION = 'wsgi.application'

TEST_RUNNER = 'django.test.runner.DiscoverRunner'

USE_I18N = True
USE_L10N = True
USE_TZ = True

ADMIN_URL = 'admin'

MEDIA_ROOT = '%s/media/' % PATH_DATA
MEDIA_URL = '/media/'

STATIC_ROOT = '%s/static/' % PATH_DATA
STATIC_URL = '/static/'
STATICFILES_DIRS = ('%s/static_src/' % PATH_DATA,)
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)
STATIC_URL_FULL = SITE_URL + STATIC_URL


MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'apps.middleware.TimezoneMiddleware',
    'simple_history.middleware.HistoryRequestMiddleware',
)


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'debug': DEBUG,
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]


INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',

    'apps',

    'admirarchy',
    'sitecats',
    'siteflags',
    'sitetree',
    'siteblocks',
    'sitegate',
    'sitemetrics',
    'siteprefs',
    'sitemessage',
    'xross',
    'etc',

    'datetimewidget',
    'simple_history',
    'robots',
)


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'simple': {
            'format': '%(asctime)s %(levelname)s %(name)s: %(message)s'
        },
        'verbose': {
            'format': '%(asctime)s %(levelname)s %(name)s (%(module)s) (%(process)d / %(thread)d): %(message)s'
        },
    },
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
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': PATH_DEBUG_LOG,
            'formatter': 'verbose'
        },
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
        'pythonz': {
            'level': 'DEBUG',
            'filters': ['require_debug_true'],
            'handlers': ['console'],
            'propagate': True,
        },
    }
}
LOGGERS = LOGGING['loggers']


if DEBUG:
    # Обход ошибки импорта - ручное конфигурирование отладочной панели.
    # https://github.com/django-debug-toolbar/django-debug-toolbar/issues/521.
    DEBUG_TOOLBAR_PATCH_SETTINGS = False
    MIDDLEWARE_CLASSES = ('debug_toolbar.middleware.DebugToolbarMiddleware',) + MIDDLEWARE_CLASSES
    INSTALLED_APPS += ('debug_toolbar',)
    # INSTALLED_APPS += ('debug_toolbar.apps.DebugToolbarConfig',)
    INTERNAL_IPS = ['127.0.0.1']
