from models.user import User


class User_transformer():

    def transform_user(self, data):
        user = User(
            name=data['personaname'],
            img=data['avatarfull'],
            url=data['profileurl'],
            created=data['timecreated'],
            games=[]
        )

        return user
