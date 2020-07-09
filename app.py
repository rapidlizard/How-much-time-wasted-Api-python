from flask import Flask, jsonify
from models.user import User

app = Flask(__name__)

@app.route('/howmuchtimehaveiwasted')
def get_user():
    new_user = User('lizard', 'img', 'url', 'now')
    
    return jsonify(new_user.to_json())

if __name__ == '__main__':
    app.run()
