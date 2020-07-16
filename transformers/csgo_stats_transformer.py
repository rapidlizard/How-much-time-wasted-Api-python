from models.csgo_stats import Csgo_stats


class Csgo_stats_transformer():

    def transform_csgo_stats(self, csgo_stats_data, gun_stats):
        csgo_stats = Csgo_stats(
            hours=csgo_stats_data['total_time_played'],
            total_kills=csgo_stats_data['total_kills'],
            defused_bombs=csgo_stats_data['total_defused_bombs'],
            planted_bombs=csgo_stats_data['total_planted_bombs'],
            money_earned=csgo_stats_data['total_money_earned'],
            mvps=csgo_stats_data['total_mvps'],
            total_wins=csgo_stats_data['total_wins'],
            knife_kills=csgo_stats_data['total_kills_knife'],
            shots_fired=csgo_stats_data['total_shots_fired'],
            shots_hit=csgo_stats_data['total_shots_hit'],
            total_deaths=csgo_stats_data['total_deaths'],
            rescued_hostages=csgo_stats_data['total_rescued_hostages'],
            headshots=csgo_stats_data['total_kills_headshot'],
            weapons_donated=csgo_stats_data['total_weapons_donated'],
            dominations=csgo_stats_data['total_dominations'],
            revenges=csgo_stats_data['total_revenges'],
            broken_windows=csgo_stats_data['total_broken_windows'],
            gun_stats=gun_stats
        )

        return csgo_stats
