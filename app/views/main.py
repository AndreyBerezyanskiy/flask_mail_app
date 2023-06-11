from flask import Blueprint, render_template
from app import mail
from flask_mail import Message
from app.forms import EmailForm


main_blueprint = Blueprint("main", __name__)


@main_blueprint.route("/main", methods=["GET", "POST"])
def main():
    form = EmailForm()

    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data.lower()

        if name and email:
            msg = Message(
                "Hello",
                sender="andrii.berezyanskii@gmail.com",
                recipients=[f"{email}"],
            )
            # msg.body = "Hello Flask message sent from Flask-Mail"
            msg.html = render_template("email-layout.html", name=name)
            mail.send(msg)
            return render_template("success.html")

    return render_template("home.html", form=form)
