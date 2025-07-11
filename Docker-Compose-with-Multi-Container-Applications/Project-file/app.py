from flask import Flask, request, jsonify, render_template
from redis import Redis

app = Flask(__name__)
redis = Redis(host="redis", db=0, socket_timeout=5, charset="utf-8", decode_responses=True)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/animals', methods=['POST', 'GET'])
def animals():
    if request.method == 'POST':
        data = request.get_json()
        names = data.get('names')
        if isinstance(names, list):
            redis.rpush('animals', *names)
        else:
            redis.rpush('animals', names)
        return jsonify({'status': 'success'})

    if request.method == 'GET':
        return jsonify(redis.lrange('animals', 0, -1))
    
@app.route('/animals/<int:index>', methods=['DELETE'])
def delete_animal(index):
    redis.lset('animals', index, '__TO_DELETE__')
    redis.lrem('animals', 1, '__TO_DELETE__')
    return jsonify({'status': 'deleted'})
 
