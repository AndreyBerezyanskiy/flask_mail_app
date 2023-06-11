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
        home_blueprint,
    )

    app = Flask(__name__)

    app.config["SECRET_KEY"] = "3000a5aa-103e-4744-a12e-5333e0f672d9"

    app.config["MAIL_SERVER"] = "smtp.gmail.com"
    app.config["MAIL_PORT"] = 465
    app.config["MAIL_USERNAME"] = "andrii.berezianskii@gmail.com"
    app.config["MAIL_PASSWORD"] = "qkroxzhzlcilmkvw"
    app.config["MAIL_USE_TLS"] = False
    app.config["MAIL_USE_SSL"] = True

    mail.init_app(app)

    app.register_blueprint(email_blueprint)
    app.register_blueprint(main_blueprint)
    app.register_blueprint(home_blueprint)

    return app
