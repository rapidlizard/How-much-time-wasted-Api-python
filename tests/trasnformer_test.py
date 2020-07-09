import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from models.transformers import User_transformer
from models.user import User

def test_user_transformer_turns_json_dict_into_user_obj():
    data = {
        "steamid": "76561198066000502",
        "communityvisibilitystate":3,
        "profilestate":1,
        "personaname":"Lixard",
        "commentpermission":1,
        "profileurl":"https://steamcommunity.com/profiles/76561198066000502/",
        "avatar":"https://steamcdn-a.akamaihd.net/steamcommunity/public/images/avatars/4a/4ad45031967e52ce05f28c7f5591227e66715c5d.jpg",
        "avatarmedium":"https://steamcdn-a.akamaihd.net/steamcommunity/public/images/avatars/4a/4ad45031967e52ce05f28c7f5591227e66715c5d_medium.jpg",
        "avatarfull":"https://steamcdn-a.akamaihd.net/steamcommunity/public/images/avatars/4a/4ad45031967e52ce05f28c7f5591227e66715c5d_full.jpg",
        "avatarhash":"4ad45031967e52ce05f28c7f5591227e66715c5d",
        "lastlogoff":1594245076,
        "personastate":0,
        "primaryclanid":"103582791463737200",
        "timecreated":1340730740,
        "personastateflags":4,
        "loccountrycode":"PT",
        "locstatecode":"14"
    }

    user = User_transformer().transform(data)

    assert type(user) == User
    assert user.name == 'Lixard'
    assert user.img == 'https://steamcdn-a.akamaihd.net/steamcommunity/public/images/avatars/4a/4ad45031967e52ce05f28c7f5591227e66715c5d_full.jpg'
    assert user.url == 'https://steamcommunity.com/profiles/76561198066000502/'
    assert user.created == '1340730740'

