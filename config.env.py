import os

# Flask config
DEBUG = False
APP_NAME = os.environ.get('STRATIFORM_APP_NAME', 'stratiform')
IP = os.environ.get('STRATIFORM_IP', '127.0.0.1')
PORT = int(os.environ.get('STRATIFORM_PORT', '6969'))