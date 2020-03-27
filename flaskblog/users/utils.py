import os
import secrets
from PIL import Image
from flask import url_for, current_app
from flask_mail import Message
from flaskblog import mail

def save_picture(form_picture):
    """Function to randomize a picture name then save it"""
    random_hex = secrets.token_hex(8) # Generate a random sequence
    _, f_ext = os.path.splitext(form_picture.filename) # Get the picture exntension
    picture_fn = random_hex + f_ext # Create a new name with the random and extension
    picture_path = os.path.join(current_app.root_path,
                                'static/profile_pics', picture_fn) # Create the path to the picture
    output_size = (250, 250) # Size of the new picture
    i = Image.open(form_picture) # Opening the picture
    i.thumbnail(output_size) # Resizing
    i.save(picture_path) # Save the picture at the path
    return picture_fn

def send_reset_email(user):
    """To send a cofrimation email to reset pass"""
    token = user.get_reset_token()
    msg = Message('Password Reset Request',
                  sender='noreply@fluxoblog.com',
                  recipients=[user.email])
    msg.body = f"""To reset your password, visit the following link:
{url_for('users.reset_token', token=token, _external=True)}

If you did not make this request then simply ignore this email and no changes will be made.
"""
    mail.send(msg)
