from models.game import Game


class Game_transformer():
    def transform_game(self, data):
        game = Game(
            appid=data['appid'],
            playtime=data['playtime_forever']
        )

        return game

    def transform_games_list(self, data):
        games_list = []

        for game_data in data:
            game = self.transform_game(game_data)
            games_list.append(game)

        return games_list
