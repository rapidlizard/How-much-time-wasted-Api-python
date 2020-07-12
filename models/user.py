class User():

    def __init__(self, name: str, img: str, url: str, created: int, games: list):
        self.name = name
        self.img = img
        self.url = url
        self.created = created
        self.games = games
        self.total_hours = self.calc_total_hours()

    def to_json(self):
        json_games = []
        for game in self.games:
            json_games.append(game.to_json())

        return {
            'name': self.name,
            'img': self.img,
            'url': self.url,
            'created': self.created,
            'games': json_games,
        }

    def calc_total_hours(self):
        total_minutes = 0

        for game in self.games:
            total_minutes += game.playtime

        total_hours = int(total_minutes / 60)

        return total_hours
