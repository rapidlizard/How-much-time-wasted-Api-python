class Csgo_stats():

    def __init__(self, hours: int):
        self.hours = hours

    def to_json(self):
        return {
            'hours': self.hours
        }
