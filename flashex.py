from flask import Flask, flash, render_template_string, redirect, url_for

app = Flask(__name__)
app.secret_key = "secret"

@app.route("/")
def home():
    flash("You have successfully logged in!")
    return redirect(url_for("dashboard"))

@app.route("/dashboard")
def dashboard():
    # Flash messages displayed in template using Jinja
    template = """
    {% with messages = get_flashed_messages() %}
        {% for msg in messages %}
            <p>{{ msg }}</p>
        {% endfor %}
    {% endwith %}
    """
    return render_template_string(template)

if __name__ == "__main__":
    app.run(debug=True)
