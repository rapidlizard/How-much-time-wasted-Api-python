from models.user import User
from models.rating_calc import Rating_calc


class User_transformer():

    def transform_user(self, user_data, user_games, stats):
        user = User(
            rating_calc=Rating_calc(),
            name=user_data['personaname'],
            img=user_data['avatarfull'],
            url=user_data['profileurl'],
            created=user_data['timecreated'],
            games=user_games,
            csgo_stats=stats
        )

        return user
