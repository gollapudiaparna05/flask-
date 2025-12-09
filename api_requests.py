from flask import Flask, request, session

app = Flask(__name__)
app.secret_key = "mysecret"  
@app.route("/")
def home():
    return "welcome"


@app.route("/get-data")
def get_data():
    name = request.args.get("name")
    session["saved_name"] = name  
    return f"Name '{name}' saved successfully!"

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
