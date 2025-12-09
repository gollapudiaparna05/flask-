from flask import Flask
app=Flask(__name__)
@app.route('/')
def hello():
    return "<h1>hello</h1>"
@app.route('/greet/<name>')
def hi(name):
    return f"hello {name}"
@app.route('/add/<int:n1>/<int:n2>')
def add(n1,n2):
    return f'{n1+n2}'
if __name__ == "__main__":
    app.run(debug=True)
