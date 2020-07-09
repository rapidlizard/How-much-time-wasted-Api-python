import requests, json

class Steam():
    def get_user_data(steamid: str):
        url = 'http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?key=2FA14ED02A1D7CCC0E4FCA80AE6AE194&steamids=' + steamid
        response = requests.get(url)

        data = response.json()

        return data['response']['players'][0]

    def get_games_data(steamid: str):
        url = 'http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key=2FA14ED02A1D7CCC0E4FCA80AE6AE194&steamid=' + steamid
        response = requests.get(url)

        data = response.json()

        return data['response']['games']