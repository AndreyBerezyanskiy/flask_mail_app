from flask import Flask
from flask_mail import Mail
from .email import email

mail = Mail()

def create_app():
    app = Flask(__name__)

    app.config['MAIL_SERVER']='smtp.gmail.com'
    app.config['MAIL_PORT'] = 465
    app.config['MAIL_USERNAME'] = 'andrii.berezianskii@gmail.com'
    app.config['MAIL_PASSWORD'] = 'qkroxzhzlcilmkvw'
    app.config['MAIL_USE_TLS'] = False
    app.config['MAIL_USE_SSL'] = True


    mail.init_app(app)
    
    app.register_blueprint(email)

    return app