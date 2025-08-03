import json
import os
from nut import Config
from nut import Print

users = {}

def _load_users():
    global users
    try:
        with open(Config.paths.users, 'r') as f:
            users = json.load(f)
        Print.info("Loaded users.conf")
    except FileNotFoundError:
        Print.info("users.conf not found, running without authentication.")
        users = {}
    except Exception as e:
        Print.error(f"Error loading users.conf: {e}")
        users = {}

_load_users() # Load users when the module is imported

def auth(username, password, ip):
    if username in users and users[username] == password:
        Print.info(f"User {username} authenticated from {ip}")
        return username
    Print.info(f"Authentication failed for user {username} from {ip}")
    return None
