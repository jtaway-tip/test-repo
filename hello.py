import flask

app = flask.Flask(__name__)

@app.route('/', methods=['GET'])

def home():
    return "<h1> Hello DevOps </h1>"

if __name__ == '__main__':
    app.run() #run our Flask app

