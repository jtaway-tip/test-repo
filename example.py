from flask import Flask

app = Flask(__name__)

@app.route('/')

def getRoute():
    return {'R1': '192.168.5.10'}

if __name__ == '__main__':
    app.run() #run our Flask app