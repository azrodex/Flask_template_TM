from flask import Blueprint, flash, g, redirect, render_template, request, url_for, session
from app.utils import login_required
from app.db.db import get_db, get_user_by_id
from app.views.auth import load_logged_in_user
from werkzeug.security import check_password_hash, generate_password_hash
from app.db.db import get_db
import os
from email.message import EmailMessage
import smtplib
from datetime import datetime
import calendar
from flask import flash, get_flashed_messages
from app.config import mdp_google


# Routes /user/...
user_bp = Blueprint('user', __name__, url_prefix='/user')

def before_request():
    g.user = None
    if 'user_id' in session:
        g.user = get_user_by_id(session['user_id'])

@user_bp.route('/profile', methods=('GET', 'POST'))
@login_required
def show_profile():
    if request.method == 'GET':
        current_user = g.user
        client_id = session.get('user_id')
        db = get_db()
        comments = db.execute('SELECT rdv.date, rdv.heure, prestation.nom_prestation, rdv.bilan FROM rdv INNER JOIN composition ON rdv.no_rdv = composition.no_rdv INNER JOIN prestation ON composition.id_prestation = prestation.id_prestation WHERE rdv.no_client = ?', (client_id,)).fetchall()
        return render_template('user/profile.html', user=current_user, comments=comments )

@user_bp.route('/edit_profile', methods=('GET', 'POST'))
@login_required
def edit_profile():
    user_id = session.get('user_id')

    if request.method == 'POST':
        new_username = request.form['username']
        new_prenom = request.form['prenom']
        new_email = request.form['email']
        new_adresse = request.form['adresse']
        new_no_telephone = request.form['no_telephone']
        new_date_naissance = request.form['date_naissance']
        new_sexe = request.form['sexe']
        new_mdp = request.form['password']

        if new_mdp:
            db = get_db()
            db.execute(
                "UPDATE client SET nom = ?, prenom = ?, email_client = ?, adresse = ?, no_téléphone = ?, date_naissance = ?, sexe = ?, mdp_client = ? WHERE no_client = ?",
                (new_username, new_prenom, new_email, new_adresse, new_no_telephone, new_date_naissance, new_sexe, generate_password_hash(new_mdp), user_id)
            )
            db.commit()

            g.user = {
                'nom': new_username,
                'prenom': new_prenom,
                'email_client': new_email,
                'adresse': new_adresse,
                'no_téléphone': new_no_telephone,
                'date_naissance': new_date_naissance,
                'sexe': new_sexe,
                'password' : new_mdp,
            }

        else:
            db = get_db()
            db.execute(
                "UPDATE client SET nom = ?, prenom = ?, email_client = ?, adresse = ?, no_téléphone = ?, date_naissance = ?, sexe = ? WHERE no_client = ?",
                (new_username, new_prenom, new_email, new_adresse, new_no_telephone, new_date_naissance, new_sexe, user_id)
            )
            db.commit()
            g.user = {
                'nom': new_username,
                'prenom': new_prenom,
                'email_client': new_email,
                'adresse': new_adresse,
                'no_téléphone': new_no_telephone,
                'date_naissance': new_date_naissance,
                'sexe': new_sexe,
            }

        flash('Profil mis à jour avec succès', 'success')
        return redirect(url_for('user.show_profile'))

    return render_template('user/edit_profile.html')


@user_bp.route('/logout_and_delete', methods=('GET', 'POST'))
@login_required
def logout_and_delete():
    user_id = session.get('user_id')
    if request.method == 'POST':
        db = get_db()
        g.user = db.execute('DELETE FROM client WHERE no_client = ?', (user_id)).fetchone()
        flash('Compte supprimé avec succès')
        session.clear()
        return redirect(url_for('home.home_page'))
    return render_template('user/profile.html')


@user_bp.route('/check-date-profile', methods=('GET', 'POST'))
@login_required

def check_date_profile():
    if request.method == 'GET':
        return render_template('user/profile.html')

    elif request.method == 'POST':
        date = request.form['date']
        day_of_week = get_day(date)
        return render_template('user/profile.html', date=date, day_of_week=day_of_week)
    else:
        return render_template('home/404.html')

def get_day(date):
    day = datetime.strptime(date, '%Y-%m-%d').weekday()
    return calendar.day_name[day]

@user_bp.route('/check-booking-profile', methods=('GET', 'POST'))
@login_required

def check_booking_profile():
    if request.method == 'GET':
        return render_template('user/profile.html')

    elif request.method == 'POST':

        date = request.form['date']
        time = request.form['time']

        db = get_db()
        
        RDV = db.execute("SELECT * FROM rdv WHERE date = ? AND heure = ?", (date, time,)).fetchone()

        if RDV is None : 
            flash("Cette tranche horaire est disponible", "success") 
            return render_template('user/profile.html', date=date, time=time, day_of_week=get_day(date))

        else : 
            flash("Cette tranche horaire est déjà prise. Veuillez en choisir une autre.", "error")
            return redirect(url_for('home.check_date_profile')) 


@user_bp.route('/confirm-booking-profile', methods=('POST',))
@login_required

def confirm_booking_profile():
    if request.method == 'POST':
        date = request.form['date']
        time = request.form['time']
        type_rdv = request.form['type_rdv']

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
        client_id = g.user['no_client']

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

    return render_template('user/profile.html', comments=comments, prestation=prestations)


@user_bp.route('/vérif_changer_mdp', methods=('POST', 'GET'))
def changer_mdp():
    if request.method == 'POST':
        email = request.form['email']
        new_password = request.form['password']
        date_naissance = request.form['date_naissance']

        db = get_db()
        result = db.execute('SELECT date_naissance FROM client WHERE email_client = ?', (email,)).fetchone()

        if result:
            date_naissance_db = result['date_naissance']
            if date_naissance_db == date_naissance:
                db.execute('UPDATE client SET mdp_client = ? WHERE email_client = ?', (generate_password_hash(new_password), email))
                db.commit()
                flash('Le mot de passe a été changé avec succès.')
                return redirect(url_for('auth.login'))
            else:
                flash('La date de naissance est incorrecte.')
        else:
            flash("Aucun utilisateur trouvé avec cette adresse e-mail.")
            
    return render_template('user/forget_mdp.html')