class User():

    def __init__(self, rating_calc, name: str, img: str, url: str, created: int, games: list):
        self.rating_calc = rating_calc
        self.name = name
        self.img = img
        self.url = url
        self.created = created
        self.games = games
        self.total_hours = self.calc_total_hours()
        self.score = self.calc_score()
        self.rating = self.calc_rating()

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
            'total_hours': self.total_hours,
            'score': self.score,
            'rating': self.rating.to_json()
        }

    def calc_total_hours(self):
        total_minutes = 0

        for game in self.games:
            total_minutes += game.playtime

        total_hours = int(total_minutes / 60)

        return total_hours

    def calc_score(self):
        return int(self.total_hours * (self.total_hours * 0.5))

    def calc_rating(self):
        return self.rating_calc.get_rating(self.total_hours)
