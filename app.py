from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = "supersecretkey"  # needed for flash messages

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        message = request.form.get("message")

        # For now, just display a success message
        flash(f"Thanks {name}! Your message has been received.", "success")
        return redirect(url_for("contact"))

    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True)
