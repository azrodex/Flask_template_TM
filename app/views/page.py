from flask import Blueprint, request, render_template
import secrets
import smtplib
from email.mime.text import MIMEText
from app.db.db import get_db, get_user_by_id
from app.views.auth import load_logged_in_user


auth_bp = Blueprint('auth', __name__, url_prefix='/auth')

# Simulated database of users and their email addresses
users = g.user

@auth_bp.route('/forgot_password', methods=['GET', 'POST'])
def forgot_password():
    if request.method == 'POST':
        email = request.form['email']
        if email in users:
            # Generate a unique token
            token = secrets.token_urlsafe(20)
            # Store the token in the user's data for verification later
            users[email]['token'] = token
            # Send email with reset link
            send_reset_email(email, token)
            return "An email with instructions to reset your password has been sent."
        else:
            return "Email address not found."
    return render_template('forgot_password.html')

def send_reset_email(email, token):
    # Send an email with the reset link
    msg = MIMEText(f"Click the following link to reset your password: http://yourwebsite.com/auth/reset_password?token={token}")
    msg['Subject'] = 'Password Reset Request'
    msg['From'] = 'your@example.com'
    msg['To'] = email

    # Replace SMTP settings with your email provider's settings
    smtp_server = 'smtp.example.com'
    smtp_port = 587
    smtp_username = 'your_username'
    smtp_password = 'your_password'

    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(smtp_username, smtp_password)
    server.sendmail(msg['From'], msg['To'], msg.as_string())
    server.quit()

@auth_bp.route('/reset_password', methods=['GET', 'POST'])
def reset_password():
    token = request.args.get('token')
    if request.method == 'POST':
        new_password = request.form['new_password']
        # Update the password in the database
        # For simplicity, let's assume we're updating the password for the user associated with the token
        # In a real application, you'd want to verify the token's validity first
        if 'token' in users.get(email, {}):
            users[email]['password'] = new_password
            del users[email]['token']
            return "Your password has been reset successfully."
        else:
            return "Invalid or expired token."
    return render_template('reset_password.html', token=token)




