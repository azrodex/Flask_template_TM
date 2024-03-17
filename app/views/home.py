from app.db.db import getlast_client_no
from flask import Blueprint, flash, g, redirect, render_template, request, url_for, session
from app.utils import login_required
from app.db.db import get_db, get_user_by_id
from app.views.auth import load_logged_in_user
from werkzeug.security import check_password_hash, generate_password_hash

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
    prestations = db.execute("SELECT nom_prestation FROM prestation").fetchall()

    if request.method == 'POST':
        comment = request.form.get('comment')
        date = request.form.get('date_rdv')
        heure = request.form.get('heure_rdv')
        type_rdv = request.form.get('type_rdv')

        db.execute('INSERT INTO rdv (no_client, bilan, date, heure) VALUES (?, ?, ?, ?)', (client_id, comment, date, heure))
        db.commit()

        presta_cursor = db.execute('SELECT id_prestation FROM prestation WHERE nom_prestation = ?', (type_rdv,))
        presta = presta_cursor.fetchone()

        rdv_cursor = db.execute('SELECT no_rdv FROM rdv WHERE date = ? and heure =?', (date, heure,))
        rdv = rdv_cursor.fetchone()

        no_presta = db.execute('INSERT INTO composition (id_prestation, no_rdv) VALUES (?, ?)', (presta['id_prestation'], rdv['no_rdv']))
        db.commit()

        nom_prestation_cursor = db.execute('SELECT prestation.nom_prestation FROM prestation INNER JOIN composition ON prestation.id_prestation = composition.id_prestation WHERE composition.no_rdv = ?', (rdv['no_rdv'],))
        nom_prestation = nom_prestation_cursor.fetchone()['nom_prestation']
        print(nom_prestation)


        flash("Rendez-vous ajouté avec succès", "success")

    # Récupérer l'historique des rendez-vous pour ce client avec le nom de la prestation associée
    comments = db.execute('SELECT rdv.date, rdv.heure, prestation.nom_prestation, rdv.bilan FROM rdv INNER JOIN composition ON rdv.no_rdv = composition.no_rdv INNER JOIN prestation ON composition.id_prestation = prestation.id_prestation WHERE rdv.no_client = ?', (client_id,)).fetchall()

    return render_template('page/client_details.html', client=client_data, comments=comments, prestation=prestations)

# Gestionnaire d'erreur 404 pour toutes les routes inconnues
@home_bp.route('/<path:text>', methods=['GET', 'POST'])
def not_found_error(text):
    return render_template('home/404.html'), 404
