from base import *
import dj_database_url

DEBUG = False

DATABASES = {
    'default': dj_database_url.config('CLEARDB_DATABASE_URL')
}

# Stripe environment variables
STRIPE_PUBLISHABLE = os.getenv('STRIPE_PUBLISHABLE', 'pk_test_FGFeav0Qyh7EWFOE5tjhvUXG')
STRIPE_SECRET = os.getenv('STRIPE_SECRET', 'sk_test_eNJCMyNYFWAKhYekmVjdAI2E')

# Paypal environment variables
PAYPAL_NOTIFY_URL = 'http://b82e1155.ngrok.io/a-very-hard-to-guess-url/'
PAYPAL_RECEIVER_EMAIL = 'renandias@yahoo.com.br'

SITE_URL = 'https://git.heroku.com/renantry.git'
ALLOWED_HOSTS.append('renantry.herokuapp.com')

# Log DEBUG information to the console
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': os.getenv('DJANGO_LOG_LEVEL', 'DEBUG'),
        },
    },
}