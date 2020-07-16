class Csgo_stats():

    def __init__(self, hours, total_kills, total_deaths, defused_bombs, planted_bombs, money_earned, mvps, total_wins, knife_kills, shots_fired, shots_hit, gun_stats, rescued_hostages, headshots, weapons_donated, dominations, revenges, broken_windows):
        self.hours = self.calc_hours(hours)
        self.total_kills = total_kills
        self.total_deaths = total_deaths
        self.defused_bombs = defused_bombs
        self.planted_bombs = planted_bombs
        self.money_earned = money_earned
        self.mvps = mvps
        self.total_wins = total_wins
        self.knife_kills = knife_kills
        self.shots_fired = shots_fired
        self.shots_hit = shots_hit
        self.accuracy = self.calc_accuracy()
        self.kd_ratio = self.calc_kd_ratio()
        self.gun_stats = gun_stats
        self.rescued_hostages = rescued_hostages
        self.headshots = headshots
        self.weapons_donated = weapons_donated
        self.dominations = dominations
        self.revenges = revenges
        self.broken_windows = broken_windows
        self.headshot_percentage = self.calc_hs_percent()

    def to_json(self):
        return {
            'hours': self.hours,
            'total_kills': self.total_kills,
            'total_deaths': self.total_deaths,
            'defused_bombs': self.defused_bombs,
            'planted_bombs': self.planted_bombs,
            'money_earned': self.money_earned,
            'mvps': self.mvps,
            'total_wins': self.total_wins,
            'knife_kills': self.knife_kills,
            'shots_fired': self.shots_fired,
            'shots_hit': self.shots_hit,
            'accuracy': self.accuracy,
            'kd_ratio': self.kd_ratio,
            'rescued_hostages': self.rescued_hostages,
            'headshots': self.headshots,
            'weapons_donated': self.weapons_donated,
            'dominations': self.dominations,
            'revenges': self.revenges,
            'broken_windows': self.broken_windows,
            'gun_stats': self.gun_stats.to_json(),
            'headshot_percentage': self.headshot_percentage
        }

    def calc_accuracy(self):
        return round((self.shots_hit / self.shots_fired) * 100, 2)

    def calc_kd_ratio(self):
        return round(self.total_kills / self.total_deaths, 2)

    def calc_hs_percent(self):
        return round((self.headshots / self.total_kills) * 100, 2)

    def calc_hours(self, hours):
        return round(hours / 60 / 24)
