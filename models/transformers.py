from models.user import User

class User_transformer():
    
    def transform(self, data):
        user = User(
            name= data['personaname'],
            img= data['avatarfull'],
            url= data['profileurl'],
            created= str(data['timecreated'])
        )
        return user 