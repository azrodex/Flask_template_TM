from flask import Blueprint, flash, g, redirect, render_template, request, url_for, session
from app.utils import login_required
from app.db.db import get_db, get_user_by_id
from app.views.auth import load_logged_in_user
from werkzeug.security import check_password_hash, generate_password_hash
from app.db.db import get_db
import os


# Routes /user/...
user_bp = Blueprint('user', __name__, url_prefix='/user')

def before_request():
    g.user = None
    if 'user_id' in session:
        g.user = get_user_by_id(session['user_id'])

@user_bp.route('/profile', methods=('GET', 'POST'))
@login_required
def show_profile():
    current_user = g.user
    return render_template('user/profile.html', user=current_user)

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