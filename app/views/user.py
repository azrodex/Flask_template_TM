from flask import Blueprint, flash, g, redirect, render_template, request, url_for, session
from app.utils import login_required
from app.db.db import get_db, get_user_by_id

# Routes /user/...
user_bp = Blueprint('user', __name__, url_prefix='/user')

def before_request():
    g.user = None
    if 'user_id' in session:
        g.user = get_user_by_id(session['user_id'])

# Route /user/profile accessible uniquement à un utilisateur connecté grâce au décorateur @login_required
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
        new_password = request.form['password']

        # Mettez à jour les données de l'utilisateur dans la base de données
        db = get_db()
        db.execute(
            "UPDATE client SET nom = ?, prenom = ?, email_client = ?, adresse = ?, no_téléphone = ?, date_naissance = ?, sexe = ?, mdp_client = ? WHERE no_client = ?",
            (new_username, new_prenom, new_email, new_adresse, new_no_telephone, new_date_naissance, new_sexe, new_password, user_id)
        )
        db.commit()

        # Mettez à jour l'objet 'g.user' avec les nouvelles données
        g.user.nom = new_username
        g.user.prenom = new_prenom
        g.user.email_client = new_email
        g.user.adresse = new_adresse
        g.user.no_téléphone = new_no_telephone
        g.user.date_naissance = new_date_naissance
        g.user.sexe = new_sexe
        g.user.mdp_client = new_password
        # Mettez à jour d'autres attributs de 'g.user' avec les nouvelles données

        flash('Profil mis à jour avec succès', 'success')
        return redirect(url_for('user.show_profile'))

    return render_template('user/edit_profile.html')




