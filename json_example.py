from flask import Flask, jsonify

app = Flask(__name__)
@app.route("/")
def hello():
    data={"message":"hello please visit give route","routes":"/api/user"}
    return jsonify(data)

@app.route("/api/user")
def user():
    data = {"name": "Aparna", "role": "Developer"}
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)
