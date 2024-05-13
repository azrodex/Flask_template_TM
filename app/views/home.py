from app.db.db import getlast_client_no
from flask import Blueprint, flash, g, redirect, render_template, request, url_for, session
from app.utils import login_required
from app.db.db import get_db, get_user_by_id
from app.views.auth import load_logged_in_user
from werkzeug.security import check_password_hash, generate_password_hash
from email.message import EmailMessage
import smtplib
from datetime import datetime
import calendar
from flask import flash, get_flashed_messages
from app.config import mdp_google




# Routes /...
home_bp = Blueprint('home', __name__)

@home_bp.route('/', methods=('GET', 'POST'))
def home_page():
    last_client_no = getlast_client_no()  # Appel de la fonction pour obtenir le dernier numéro de client
    return render_template('home/index.html', last_client_no=last_client_no)


# route formulaire de contact

@home_bp.route('/submit_contact_form', methods=['POST'])
def submit_contact_form():
    nom = request.form['nom']
    prenom = request.form['prenom']
    email = request.form['_replyto']
    sujet = request.form['sujet']
    message = request.form['message']

    sender = "rotene06@gmail.com"
    recipient = "rotene06@gmail.com"
    content = f"Nom: {nom}\nPrénom: {prenom}\nEmail: {email}\nMessage: {message}"

    email = EmailMessage()
    email['From'] = sender
    email['To'] = recipient
    email['Subject'] = sujet
    email.set_content(content)

    smtp = smtplib.SMTP_SSL("smtp.gmail.com", port=465)

    smtp.login(sender, mdp_google)
    smtp.sendmail(sender, recipient, email.as_string())
    smtp.quit()

    return redirect(url_for('home.success'))

# routes des différentes pages

@home_bp.route('/success')
def success():
    return render_template('page/success.html')


@home_bp.route('/contact', methods=['GET'])
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


# route administrateur

@home_bp.route('/admin')
@login_required
def admin():
    user_id = session.get('user_id')
    if user_id == 25:
        db = get_db()
        all_data = db.execute('SELECT no_client, nom, prenom, date_naissance, no_téléphone, email_client, adresse, sexe FROM client').fetchall()
        return render_template('page/admin.html', client_data = all_data)
    else :
        return render_template('home/404.html')

@home_bp.route('/admin/<int:client_id>', methods=['GET', 'POST'])
@login_required
def client_details(client_id):
    db = get_db()
    client_data = db.execute('SELECT no_client, nom, prenom, date_naissance, no_téléphone, email_client, adresse, sexe FROM client WHERE no_client = ?', (client_id,)).fetchone()
    prestations = db.execute("SELECT nom_prestation FROM prestation").fetchall()
    user_id = session.get('user_id')
    
    if user_id == 25:
        if request.method == 'POST':
            comment = request.form.get('comment')
            date = request.form.get('date_rdv')
            heure = request.form.get('heure_rdv')
            type_rdv = request.form.get('type_rdv')

            rdv_amodif = db.execute('SELECT no_rdv FROM rdv WHERE no_client = ? AND date = ? AND heure = ?', (client_id, date, heure)).fetchone()

            if rdv_amodif:
                rdv_id = rdv_amodif['no_rdv']
                db.execute('UPDATE rdv SET bilan = ? WHERE no_rdv = ?', (comment, rdv_id))
                comments = db.execute('SELECT rdv.date, rdv.heure, prestation.nom_prestation, rdv.bilan FROM rdv INNER JOIN composition ON rdv.no_rdv = composition.no_rdv INNER JOIN prestation ON composition.id_prestation = prestation.id_prestation WHERE rdv.no_client = ?', (client_id,)).fetchall()
                db.commit()
                flash("Rendez-vous ajouté avec succès", "success")
                return render_template('page/client_details.html', client=client_data, comments=comments)
                
            else:
                flash("Aucun rendez-vous trouvé")
                return render_template('page/client_details.html', client=client_data, comments=[])

        elif request.method == 'GET':
            comments = db.execute('SELECT rdv.date, rdv.heure, prestation.nom_prestation, rdv.bilan FROM rdv INNER JOIN composition ON rdv.no_rdv = composition.no_rdv INNER JOIN prestation ON composition.id_prestation = prestation.id_prestation WHERE rdv.no_client = ?', (client_id,)).fetchall()
            return render_template('page/client_details.html', client=client_data, comments=comments)
    else:
        return render_template('home/404.html')


# Gestionnaire d'erreur 404 pour toutes les routes inconnues
@home_bp.route('/<path:text>', methods=['GET', 'POST'])
def not_found_error(text):
    return render_template('home/404.html'), 404



# route pour la page rdv (formulaire de rdv)

@home_bp.route('/check-date', methods=('GET', 'POST'))
def check_date():
    if request.method == 'GET':
        return render_template('page/rdv.html')

    elif request.method == 'POST':
        date = request.form['date']
        day_of_week = get_day(date)
        return render_template('page/rdv.html', date=date, day_of_week=day_of_week)
    else:
        return render_template('home/404.html')

def get_day(date):
    day = datetime.strptime(date, '%Y-%m-%d').weekday()
    return calendar.day_name[day]

@home_bp.route('/check-booking', methods=('GET', 'POST'))
def check_booking():
    if request.method == 'GET':
        return render_template('page/rdv.html')

    elif request.method == 'POST':

        date = request.form['date']
        time = request.form['time']

        db = get_db()
        
        RDV = db.execute("SELECT * FROM rdv WHERE date = ? AND heure = ?", (date, time,)).fetchone()

        if RDV is None : 
            flash("Cette tranche horaire est disponible", "success") 
            return render_template('page/rdv.html', date=date, time=time, day_of_week=get_day(date))

        else : 
            flash("Cette tranche horaire est déjà prise. Veuillez en choisir une autre.", "error")
            return redirect(url_for('home.check_date')) 

@home_bp.route('/confirm-booking', methods=('POST',))
def confirm_booking():
    if request.method == 'POST':
        date = request.form['date']
        time = request.form['time']
        type_rdv = request.form['type_rdv']

        if g.user is None:
            no_client = 0
            nom = request.form['nom']
            prenom = request.form['prenom']
            num_tel = request.form['no_telephone']
            email = request.form['email']

        else:
            no_client = g.user['no_client']
            nom = g.user['nom']
            prenom = g.user['prenom']
            num_tel = g.user['no_téléphone']
            email = g.user['email_client']

        sender = "rotene06@gmail.com"
        recipient = "rotene06@gmail.com"
        content = f"Nom: {nom}\nPrénom: {prenom}\nNuméro de téléphone: {num_tel}\nEmail: {email}\nHeure: {time}\nDate: {date}\nType rendez-vous: {type_rdv}"

        email = EmailMessage()
        email['From'] = sender
        email['To'] = recipient
        email['Subject'] = type_rdv
        email.set_content(content)

        smtp = smtplib.SMTP_SSL("smtp.gmail.com", port=465)

        smtp.login(sender, mdp_google)
        smtp.sendmail(sender, recipient, email.as_string())
        smtp.quit()

        db = get_db()

        prestations = db.execute("SELECT nom_prestation FROM prestation").fetchall()
        client_id = no_client

        db.execute("INSERT INTO rdv (date, heure, no_client) VALUES (?, ?, ?)",(date, time, no_client))
        db.commit()

        presta_cursor = db.execute('SELECT id_prestation FROM prestation WHERE nom_prestation = ?', (type_rdv,))
        presta = presta_cursor.fetchone()

        rdv_cursor = db.execute('SELECT no_rdv FROM rdv WHERE date = ? and heure =?', (date, time,))
        rdv = rdv_cursor.fetchone()

        no_presta = db.execute('INSERT INTO composition (id_prestation, no_rdv) VALUES (?, ?)', (presta['id_prestation'], rdv['no_rdv']))
        db.commit()

        nom_prestation_cursor = db.execute('SELECT prestation.nom_prestation FROM prestation INNER JOIN composition ON prestation.id_prestation = composition.id_prestation WHERE composition.no_rdv = ?', (rdv['no_rdv'],))
        nom_prestation = nom_prestation_cursor.fetchone()['nom_prestation']

        comments = db.execute('SELECT rdv.date, rdv.heure, prestation.nom_prestation, rdv.bilan FROM rdv INNER JOIN composition ON rdv.no_rdv = composition.no_rdv INNER JOIN prestation ON composition.id_prestation = prestation.id_prestation WHERE rdv.no_client = ?', (client_id,)).fetchall()


    if g.user is None: 
        return render_template('page/success.html')
    else: 
        return render_template('user/profile.html', comments=comments, prestation=prestations)





