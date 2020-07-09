from flask import Flask

app = Flask(__name__)

@app.route('/howmuchtimehaveiwasted/<steam_id>')
def get_user(steam_id):
    return 'Your steam id is:' + steam_id

if __name__ == '__main__':
    app.run()
