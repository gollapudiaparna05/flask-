from flask import Flask, request, session

app = Flask(__name__)
app.secret_key = "mysecret"  # Required for session storage

@app.route("/")
def home():
    return "welcome"

# ---- GET request stores data ----
@app.route("/get-data")
def get_data():
    name = request.args.get("name")
    session["saved_name"] = name  # store in session
    return f"Name '{name}' saved successfully!"

# ---- POST Form Request reads saved data ----
@app.route("/post-data", methods=["POST"])
def post_data():
    form_name = request.form.get("name")   
    saved_name = session.get("saved_name") 
    return {
        "form_received": form_name,
        "saved_from_get": saved_name
    }

@app.route("/test-post")
def test_post():
    return '''
    <form action="/post-data" method="POST">
        <input name="name" placeholder="Enter name">
        <button type="submit">Send</button>
    </form>
    '''

if __name__ == "__main__":
    app.run(debug=True)
