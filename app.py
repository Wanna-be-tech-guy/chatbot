from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/do_something', methods=['POST'])
def do_something():
    return jsonify(message="I totally did something")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
