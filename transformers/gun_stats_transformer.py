from models.gun_stats import Gun_stats


class Gun_stats_transformer():

    def transform_gun_stats(self, data):
        gun_stats = Gun_stats(
            glock=data["total_kills_glock"],
            deagle=data["total_kills_deagle"],
            elite=data["total_kills_elite"],
            fiveseven=data["total_kills_fiveseven"],
            xm10=data["total_kills_xm1014"],
            mac10=data["total_kills_mac10"],
            ump=data["total_kills_ump45"],
            p90=data["total_kills_p90"],
            awp=data["total_kills_awp"],
            ak47=data["total_kills_ak47"],
            aug=data["total_kills_aug"],
            famas=data["total_kills_famas"],
            g3sg1=data["total_kills_g3sg1"],
            m249=data["total_kills_m249"],
            p2000=data["total_kills_hkp2000"],
            p250=data["total_kills_p250"],
            sg556=data["total_kills_sg556"],
            scar20=data["total_kills_scar20"],
            scout=data["total_kills_ssg08"],
            mp7=data["total_kills_mp7"],
            mp9=data["total_kills_mp9"],
            nova=data["total_kills_nova"],
            negev=data["total_kills_negev"],
            sawedoff=data["total_kills_sawedoff"],
            bizon=data["total_kills_bizon"],
            tec9=data["total_kills_tec9"],
            mag7=data["total_kills_mag7"],
            m4a1=data["total_kills_m4a1"],
            galil=data["total_kills_galilar"],
        )

        return gun_stats
