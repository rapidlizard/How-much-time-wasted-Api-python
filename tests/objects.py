from models.game import Game
from models.user import User
from models.gun_stats import Gun_stats
from models.csgo_stats import Csgo_stats
from services.rating_calc import Rating_calc


game1_for_test = Game(appid=10, playtime=82)
game2_for_test = Game(appid=80, playtime=0)
game3_for_test = Game(appid=100, playtime=0)
game4_for_test = Game(appid=240, playtime=98)

gun_stats_for_test = Gun_stats(
    glock=7100,
    deagle=12602,
    elite=150,
    fiveseven=679,
    xm10=394,
    mac10=1169,
    ump=1576,
    p90=1128,
    awp=33620,
    ak47=107332,
    aug=1584,
    famas=721,
    g3sg1=222,
    m249=220,
    p2000=8907,
    p250=2403,
    sg556=1787,
    scar20=233,
    scout=1593,
    mp7=1593,
    mp9=932,
    nova=208,
    negev=299,
    sawedoff=112,
    bizon=386,
    tec9=463,
    mag7=137,
    m4a1=23951,
    galil=752
)

csgo_stats_for_test = Csgo_stats(
    defused_bombs=717,
    hours=5272693,
    knife_kills=1177,
    money_earned=278525408,
    mvps=29980,
    planted_bombs=2732,
    shots_fired=2231475,
    shots_hit=552856,
    total_deaths=103202,
    total_kills=214095,
    total_wins=56101
)

user_for_testing = User(
    name='Lixard',
    img='https://steamcdn-a.akamaihd.net/steamcommunity/public/images/avatars/4a/4ad45031967e52ce05f28c7f5591227e66715c5d_full.jpg',
    url='https://steamcommunity.com/profiles/76561198066000502/',
    created=1340730740,
    games=[
        game1_for_test,
        game2_for_test,
        game3_for_test,
        game4_for_test
    ],
    rating_calc=Rating_calc(),
    csgo_stats=csgo_stats_for_test
)


def user():
    return user_for_testing
