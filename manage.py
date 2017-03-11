import os
import sys

from flask_script import Manager, Server
from stratiform import app

root_dir = os.path.dirname(os.path.abspath(__file__))
config_file = os.path.join(root_dir, "config.py")
env_config_file = os.path.join(root_dir, "config.env.py")

if os.path.exists(config_file):
    app.config.from_pyfile(config_file)
elif os.path.exists(env_config_file):
    app.config.from_pyfile(env_config_file)
else:
    print("Unable to load configuration, please make sure config.py or config.env.py exists and is readable.")
    sys.exit(1)

manager = Manager(app)
manager.add_command("runserver", Server(host=app.config.get('IP', '127.0.0.1'), port=app.config.get('PORT', 5000)))

if __name__ == "__main__":
    manager.run()
