from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/booking")
def booking():
    return render_template("booking.html")


@app.route("/success", methods=["POST"])
def success():

    name = request.form.get("name")
    email = request.form.get("email")
    phone = request.form.get("phone")
    event = request.form.get("event")
    date = request.form.get("date")
    location = request.form.get("location")

    return render_template(
        "success.html",
        name=name,
        email=email,
        phone=phone,
        event=event,
        date=date,
        location=location
    )


if __name__ == "__main__":
    app.run(debug=True)