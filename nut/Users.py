import json
import os
from nut import Config
from nut import Print

users = {}

def load():
    global users
    try:
        with open(os.path.join(Config.paths.conf, 'users.conf'), 'r') as f:
            users = json.load(f)
        Print.info("Loaded users.conf")
    except FileNotFoundError:
        Print.info("users.conf not found, running without authentication.")
        users = {}
    except Exception as e:
        Print.error(f"Error loading users.conf: {e}")
        users = {}

def auth(username, password, ip):
    load()
    if username in users and users[username] == password:
        Print.info(f"User {username} authenticated from {ip}")
        return username
    Print.info(f"Authentication failed for user {username} from {ip}")
    return None
