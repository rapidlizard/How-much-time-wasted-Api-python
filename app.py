from flask import Flask, jsonify
from models.user import User

app = Flask(__name__)

@app.route('/howmuchtimehaveiwasted')
def get_user():
    new_user = User('lizard', 'img', 'url', 'now')
    json_user = {
        'name': new_user.name,
        'img': new_user.img,
        'url': new_user.url,
        'created': new_user.created
    }
    return jsonify(json_user)

if __name__ == '__main__':
    app.run()
