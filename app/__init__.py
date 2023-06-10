from dotenv import load_dotenv

from flask import Flask
from flask_mail import Mail


load_dotenv()


# app = Flask(__name__)


mail = Mail()


def create_app():
    from app.views import (
        email_blueprint,
        main_blueprint,
    )

    app = Flask(__name__)

    app.config["MAIL_SERVER"] = "smtp.gmail.com"
    app.config["MAIL_PORT"] = 465
    app.config["MAIL_USERNAME"] = "andrii.berezianskii@gmail.com"
    app.config["MAIL_PASSWORD"] = "qkroxzhzlcilmkvw"
    app.config["MAIL_USE_TLS"] = False
    app.config["MAIL_USE_SSL"] = True

    mail.init_app(app)

    app.register_blueprint(email_blueprint)
    app.register_blueprint(main_blueprint)

    return app
