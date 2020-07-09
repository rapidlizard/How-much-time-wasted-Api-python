from models.user import User

class Transformer():
    
    def transform_user(self, data):
        user = User(
            name= data['personaname'],
            img= data['avatarfull'],
            url= data['profileurl'],
            created= str(data['timecreated'])
        )
        return user 