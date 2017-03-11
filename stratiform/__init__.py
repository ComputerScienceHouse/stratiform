import os
import sys

from flask import Flask

app = Flask(__name__)

root_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
config_file = os.path.join(root_dir, "config.py")
env_config_file = os.path.join(root_dir, "config.env.py")

if os.path.exists(config_file):
    app.config.from_pyfile(config_file)
elif os.path.exists(env_config_file):
    app.config.from_pyfile(env_config_file)
else:
    print("Unable to load configuration, please make sure config.py or config.env.py exists and is readable.")
    sys.exit(1)


@app.route("/api/hello")
def index():
    return "Hello world!"
