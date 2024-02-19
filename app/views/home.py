from flask import Blueprint, render_template
from app.db.db import getlast_client_no

# (Blueprint, flash, g, redirect, render_template, request, session, url_for)

# Routes /...
home_bp = Blueprint('home', __name__)

@home_bp.route('/', methods=('GET', 'POST'))
def home_page():
    last_client_no = getlast_client_no()  # Appel de la fonction pour obtenir le dernier numéro de client
    return render_template('home/index.html', last_client_no=last_client_no)


@home_bp.route('/contact')
def contact():
    return render_template('page/contact.html')

@home_bp.route('/services')
def services():
    return render_template('page/services.html')

@home_bp.route('/decouvrir')
def decouvrir():
    return render_template('page/découvrir.html')

@home_bp.route('/rendez-vous')
def rdv():
    return render_template('page/rdv.html')

# Gestionnaire d'erreur 404 pour toutes les routes inconnues
@home_bp.route('/<path:text>', methods=['GET', 'POST'])
def not_found_error(text):
    return render_template('home/404.html'), 404
