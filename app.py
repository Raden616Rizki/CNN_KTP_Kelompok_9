from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return jsonify({'message': 'success'})

@app.route('/post_citra', methods=['POST'])
def post_citra():
    return jsonify({'message': 'success'})

if (__name__ == '__main__'):
    app.run('0.0.0.0', port=5000, debug=True)