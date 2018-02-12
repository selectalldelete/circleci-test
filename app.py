from flask import Flask
from redis import Redis

app = Flask(__name__)
redis = Redis(host='127.0.0.1')

@app.route('/', methods=['GET'])
def index():
    visits = redis.incr('counter')
    html = '<h3>Hello World!</h3>' \
           '<b>Vists:</b> {visits}' \
           '<br/>'
    return html.format(visits=visits)

if __name__ == '__main__':
    app.debug = True
    app.run(port=5000,host='0.0.0.0')