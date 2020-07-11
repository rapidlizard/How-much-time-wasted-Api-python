from models.user import User


class User_transformer():

    def transform_user(self, user_data):
        user = User(
            name=user_data['personaname'],
            img=user_data['avatarfull'],
            url=user_data['profileurl'],
            created=user_data['timecreated'],
            games=[],
            total_playtime=0
        )

        return user
