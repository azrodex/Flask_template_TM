from flask import Blueprint, flash, g, redirect, render_template, request, url_for, session
from app.utils import login_required
from app.db.db import get_db, get_user_by_id
from app.views.auth import load_logged_in_user

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
        # Récupérez les nouvelles données du formulaire
        new_username = request.form['username']
        new_prenom = request.form['prenom']
        new_email = request.form['email']
        new_adresse = request.form['adresse']
        new_no_telephone = request.form['no_telephone']
        new_date_naissance = request.form['date_naissance']
        new_sexe = request.form['sexe']

        # Mettez à jour les données de l'utilisateur dans la base de données
        db = get_db()
        db.execute(
            "UPDATE client SET nom = ?, prenom = ?, email_client = ?, adresse = ?, no_téléphone = ?, date_naissance = ?, sexe = ? WHERE no_client = ?",
            (new_username, new_prenom, new_email, new_adresse, new_no_telephone, new_date_naissance, new_sexe, user_id)
        )
        db.commit()

        # Mettez à jour l'objet 'g.user' avec les nouvelles données
        g.user = {
            'nom': new_username,
            'prenom': new_prenom,
            'email_client': new_email,
            'adresse': new_adresse,
            'no_téléphone': new_no_telephone,
            'date_naissance': new_date_naissance,
            'sexe': new_sexe,
            # Ajoutez d'autres attributs au besoin
        }

        flash('Profil mis à jour avec succès', 'success')
        return redirect(url_for('user.show_profile'))

    return render_template('user/edit_profile.html')

