from flask import Flask

app = Flask(__name__)

@app.route('/index', methods=['GET'])
def index():
    return 'Well hello there'

if __name__ == '__main__':
    app.debug = True
    app.run(port=5000)