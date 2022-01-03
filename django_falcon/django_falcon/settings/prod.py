from .dev import *
from dotenv import find_dotenv
load_dotenv(find_dotenv('.env.prod'), override=True)

DEBUG = False
DATABASES['default']['NAME'] = os.getenv('DB_NAME')
DATABASES['default']['USER'] = os.getenv('DB_USER')
DATABASES['default']['PASSWORD'] = os.getenv('DB_PASSWORD')
DATABASES['default']['HOST'] = os.getenv('DB_HOST')
ALLOWED_HOSTS = ['*']
