from app.db.db import getlast_client_no
from flask import Blueprint, flash, g, redirect, render_template, request, url_for, session
from app.utils import login_required
from app.db.db import get_db, get_user_by_id
from app.views.auth import load_logged_in_user
from werkzeug.security import check_password_hash, generate_password_hash

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

@home_bp.route('/admin')
@login_required
def admin():
    user_id = session.get('user_id')
    if user_id == 25:
        db = get_db()
        all_data = db.execute('SELECT no_client, nom, prenom, date_naissance, no_téléphone, email_client, adresse, sexe FROM client').fetchall()
        return render_template('page/admin.html', client_data = all_data)

    else :
        return redirect (url_for ('home.home_page'))

@home_bp.route('/admin/<int:client_id>', methods=['GET', 'POST'])
@login_required
def client_details(client_id):
    db = get_db()
    client_data = db.execute('SELECT no_client, nom, prenom, date_naissance, no_téléphone, email_client, adresse, sexe FROM client WHERE no_client = ?', (client_id,)).fetchone()

    if request.method == 'POST':
        comment = request.form['comment']
        date = request.form['date_rdv']
        heure = request.form['heure_rdv']
        # Insérer le commentaire dans la base de données
        db.execute('INSERT INTO rdv (no_client, bilan, date, heure) VALUES (?, ?, ?, ?)', (client_id, comment, date, heure))
        db.commit()  # Confirmer la transaction après l'insertion
        flash("Comment added successfully", "success")

    # Récupérer l'historique des commentaires pour ce client
    comments = db.execute('SELECT * FROM rdv WHERE no_client = ?', (client_id,)).fetchall()

    return render_template('page/client_details.html', client=client_data, comments=comments)



# Gestionnaire d'erreur 404 pour toutes les routes inconnues
@home_bp.route('/<path:text>', methods=['GET', 'POST'])
def not_found_error(text):
    return render_template('home/404.html'), 404
