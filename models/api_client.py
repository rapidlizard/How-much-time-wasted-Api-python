import requests, json

class Steam():
    def get_user():
        url = "http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?key=2FA14ED02A1D7CCC0E4FCA80AE6AE194&steamids=76561198066000502"
        response = requests.get(url)
        return response.json()