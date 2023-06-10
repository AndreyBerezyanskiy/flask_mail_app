from flask import Blueprint, render_template
from app import mail
from flask_mail import Message

main_blueprint = Blueprint("main", __name__)


@main_blueprint.route("/main")
def main():
    msg = Message(
        "Hello",
        sender="andrii.berezyanskii@gmail.com",
        recipients=["lokotey.yana@gmail.com", "andrey.berezyanskiy@gmail.com"],
    )
    msg.body = "Hello Flask message sent from Flask-Mail"
    msg.html = render_template("email-layout.html")
    mail.send(msg)

    return render_template("email-layout.html", name="Andrii")
