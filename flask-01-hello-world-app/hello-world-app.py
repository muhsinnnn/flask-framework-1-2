from flask import Flask 
app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello, Flask!"

@app.route('/second')
def second_page():
    return "Hello, Flask222222222222222222!"

if __name__ == '__main__':

    app.run(debug=True, port=30000)
    # app.run(host= '0.0.0.0', port=8081)