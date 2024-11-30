from flask import Flask, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get-message')
def get_message():
    return jsonify({'message': 'Hello from Flask! This message was fetched from the server.'})

if __name__ == '__main__':
    app.run(debug=True)
