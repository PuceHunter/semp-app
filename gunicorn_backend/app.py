from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Configure route to /
@app.route('/')
def get_data_index_route():
    return "Hello World, from Rikin Zala! \n Search for `/message` route"

# Configure route to /message
@app.route('/message')
def get_data_message_route():
    data = "This is message route"
    response_data = {"message": data}
    return jsonify(response_data)

if __name__ == '__main__':
    app.run()