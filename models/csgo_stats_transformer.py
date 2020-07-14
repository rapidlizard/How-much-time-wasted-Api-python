from models.csgo_stats import Csgo_stats


class Csgo_stats_transformer():

    def transform_csgo_stats(self, csgo_stats_data):
        stats_list = {}
        for stat in csgo_stats_data:
            stats_list[stat['name']] = stat['value']

        csgo_stats = Csgo_stats(
            hours=stats_list['total_time_played']
        )

        return csgo_stats
