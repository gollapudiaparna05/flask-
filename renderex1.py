from flask import Flask, render_template,jsonify

app = Flask(__name__)
@app.route("/")
def hello():
    data={"route":"/welcome/<name>"}
    return jsonify(data)
@app.route("/welcome/<name>")
def welcome(name):
    return render_template("index.html", name=name)

if __name__ == "__main__":
    app.run(debug=True)
