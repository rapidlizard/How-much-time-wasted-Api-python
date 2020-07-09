from flask import Flask, jsonify
from models.user import User
from models.api_client import Steam
from models.transformers import User_transformer

app = Flask(__name__)

@app.route('/howmuchtimehaveiwasted/')
def no_steamid():
    return jsonify('Please provide a steamid'), 400

@app.route('/howmuchtimehaveiwasted/<steamid>')
def get_user(steamid):
    try:
        data = Steam.get_user_data(steamid)
    except:
        return jsonify('There was a problem finding that user'), 400

    user = User_transformer().transform(data)

    return jsonify(user.to_json())

if __name__ == '__main__':
    app.run()
