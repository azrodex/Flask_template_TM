import sqlite3
import os
from flask import current_app, g

def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(os.path.join(current_app.root_path, "db", current_app.config['DATABASE']), detect_types=sqlite3.PARSE_DECLTYPES)
        g.db.row_factory = sqlite3.Row
    return g.db

def close_db():
    db = g.pop('db', None)
    if db is not None:
        db.close()

def get_user_by_id(user_id):
    db = get_db()
    user = db.execute("SELECT * FROM client WHERE no_client = ?", (user_id,)).fetchone()

    if user is not None:
        return dict(user)
    else:
        return None

