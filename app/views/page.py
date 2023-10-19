# Importer les modules Flask nécessaires
from flask import Blueprint, render_template

# Créer un objet Blueprint pour les routes liées à la page de contact
page_bp = Blueprint('page', __name__, url_prefix='/page')

# Définir une route pour la page de contact
@page_bp.route('/contact', methods=['GET'])
def contact_page():
    # Afficher la page de contact
    return render_template('page/contact.html')



@page_bp.route('/sevice', methods=['GET'])
def service_page():
    return render_template('page/services.html')


@page_bp.route('/decouvrir', methods=['GET'])
def decouvrir_page():
    return render_template('page/découvrir.html')