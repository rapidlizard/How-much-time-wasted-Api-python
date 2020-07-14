from models.csgo_stats import Csgo_stats


class Csgo_stats_transformer():

    def transform_csgo_stats(self, csgo_stats_data):
        csgo_stats = Csgo_stats(
            hours=csgo_stats_data['total_time_played']
        )

        return csgo_stats
