

@app.route('/webhook/calendly', methods=['POST'])
def calendly_webhook():
    date = request.form['date']
    name = request.form['name']
    email = request.form['email']
    try:
        db = get_db()
        cursor = db.cursor()
        cursor.execute("INSERT INTO rdv (date, name, email, ...) VALUES (?, ?, ?, ...)", (date, name, email, ...))
        db.commit()
        return "Données de rendez-vous enregistrées avec succès."
    except Exception as e:
        return f"Erreur lors de l'enregistrement des données de rendez-vous : {e}", 500