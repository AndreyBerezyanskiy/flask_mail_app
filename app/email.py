from flask import Blueprint, render_template
from flask_mail import Message
from app import mail

email = Blueprint("email", __name__, url_prefix="/email")


@email.route("/")
def send_email():
    name = "Andrii"

    msg = Message(
        "Hello",
        sender="no-replye@gmail.com",
        recipients=["andrey.berezyanskiy@gmail.com"],
    )
    # msg.body = "Hello Flask message sent from Flask-Mail"
    msg.html = render_template("email-layout.html")
    mail.send(msg)

    return render_template("email-layout.html", name=name)
