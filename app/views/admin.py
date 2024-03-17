from flask import (Blueprint, flash, g, redirect, render_template, request, session, url_for)
from werkzeug.security import check_password_hash, generate_password_hash
from app.db.db import get_db
import os

admin_bp = Blueprint('admin', __name__, url_prefix='/admin')
@admiin_bp.route('/', methods=('GET', 'POST'))
def register():
# faire route comme d'hab
# 1.requete sql client 
# (SELECT * FROM client)

# 2. mettre dans une liste
# 3. lire et afficher les noms de la liste via une boucle
# 4. selection client pour ajouter un bilan (possible suppression)
