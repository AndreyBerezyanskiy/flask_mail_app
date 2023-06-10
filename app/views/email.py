from app import mail
from flask_mail import Message
from flask import Blueprint, render_template

email_blueprint = Blueprint("email", __name__)


@email_blueprint.route("/email")
def send_email():
    # msg = Message(
    #     "Hello",
    #     sender="andrii.berezyanskii@gmail.com",
    #     recipients=["andrey.berezyanskiy@gmail.com"],
    # )
    # msg.body = "Hello Flask message sent from Flask-Mail"
    # msg.html = render_template("email-layout.html")
    # mail.send(msg)

    return render_template("email-layout.html", name="Andrii")
