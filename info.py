import re
from os import environ

id_pattern = re.compile(r'^.\d+$')

# Bot information
SESSION = environ.get('SESSION', 'Fair033838')
API_ID = int(environ.get('API_ID', '29608422'))
API_HASH = environ.get('API_HASH', '3db2f8e109301f02f5d9c8f10dd79244')
BOT_TOKEN = environ.get('BOT_TOKEN', "8227731967:AAEmgSiywxmGfe1GYhj9RSqaOtMvaAgS99k")

# Bot settings
PORT = environ.get("PORT", "8080")

# Online Stream and Download
MULTI_CLIENT = False
SLEEP_THRESHOLD = int(environ.get('SLEEP_THRESHOLD', '60'))
PING_INTERVAL = int(environ.get("PING_INTERVAL", "1200"))  # 20 minutes
if 'DYNO' in environ:
    ON_HEROKU = True
else:
    ON_HEROKU = False
URL = environ.get("URL", "")

# Admins, Channels & Users
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', '-1004450462812'))
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '8056243176').split()]

# MongoDB information
DATABASE_URI = environ.get('DATABASE_URI', "mongodb+srv://mdohidh20:emETBcodRUOnB69C@movienamerequest.smfx6uk.mongodb.net/?retryWrites=true&w=majority&appName=Movienamerequest")
DATABASE_NAME = environ.get('DATABASE_NAME', "sabbir51bot")

# Shortlink Info
SHORTLINK = bool(environ.get('SHORTLINK', True)) # Set True Or False
SHORTLINK_URL = environ.get('SHORTLINK_URL', 'api.gplinks.co')
SHORTLINK_API = environ.get('SHORTLINK_API', 'e6fd3314b0a682a4af45850e2d1b825678530078')
