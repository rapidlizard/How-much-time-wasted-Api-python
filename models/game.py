class Game():

    def __init__(self, appid, playtime):
        self.appid = appid
        self.playtime = playtime

    def to_json(self):
        game_json = {
            'appid': self.appid,
            'playtime': self.playtime
        }

        return game_json
