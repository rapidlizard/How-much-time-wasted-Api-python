from models.user import User

class User_transformer():
    
    def transform(self, data):
        return User('jeff', 'img', 'url', 'now')