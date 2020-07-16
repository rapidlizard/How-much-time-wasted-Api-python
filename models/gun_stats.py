class Gun_stats():

    def __init__(self, glock, deagle, elite, fiveseven, xm10, mac10, ump, p90, awp, ak47, aug, famas, g3sg1, m249, p2000, p250, sg556, scar20, scout, mp7, mp9, nova, negev, sawedoff, bizon, tec9, mag7, m4a1, galil):
        self.glock = glock
        self.deagle = deagle
        self.elite = elite
        self.fiveseven = fiveseven
        self.xm10 = xm10
        self.mac10 = mac10
        self.ump = ump
        self.p90 = p90
        self.awp = awp
        self.ak47 = ak47
        self.aug = aug
        self.famas = famas
        self.g3sg1 = g3sg1
        self.m249 = m249
        self.p2000 = p2000
        self.p250 = p250
        self.sg556 = sg556
        self.scar20 = scar20
        self.scout = scout
        self.mp7 = mp7
        self.mp9 = mp9
        self.nova = nova
        self.negev = negev
        self.sawedoff = sawedoff
        self.bizon = bizon
        self.tec9 = tec9
        self.mag7 = mag7
        self.m4a1 = m4a1
        self.galil = galil

    def to_json(self):
        json_game_stats = {
            'glock': self.glock,
            'deagle': self.deagle,
            'elite': self.elite,
            'fiveseven': self.fiveseven,
            'xm10': self.xm10,
            'mac10': self.mac10,
            'ump': self.ump,
            'p90': self.p90,
            'awp': self.awp,
            'ak47': self.ak47,
            'aug': self.aug,
            'famas': self.famas,
            'g3sg1': self.g3sg1,
            'm249': self.m249,
            'p2000': self.p2000,
            'p250': self.p250,
            'sg556': self.sg556,
            'scar20': self.scar20,
            'scout': self.scout,
            'mp7': self.mp7,
            'mp9': self.mp9,
            'nova': self.nova,
            'negev': self.negev,
            'sawedoff': self.sawedoff,
            'bizon': self.bizon,
            'tec9': self.tec9,
            'mag7': self.mag7,
            'm4a1': self.m4a1,
            'galil': self.galil
        }
        return json_game_stats
