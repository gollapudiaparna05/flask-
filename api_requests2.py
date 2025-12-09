from flask import Flask ,request
app=Flask(__name__)
@app.route('/')
def home():
    return "<h1>hello</h1>"
@app.route('/get-data')#no specifications
def data():
    return str(request.args)
@app.route('/get-data2')
def data2():
    name=request.args.get('name')#requests.args['name']
    return f'{name}'

if __name__=="__main__":
    app.run(debug=True)


