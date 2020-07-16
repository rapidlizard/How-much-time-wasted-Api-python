import requests
import json


class Steam():

    def get_user_data(self, steamid: str):
        url = 'http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?key=2FA14ED02A1D7CCC0E4FCA80AE6AE194&steamids=' + steamid
        response = requests.get(url)

        data = response.json()

        return data['response']['players'][0]

    def get_user_games(self, steamid: str):
        url = 'http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key=2FA14ED02A1D7CCC0E4FCA80AE6AE194&steamid=' + steamid
        response = requests.get(url)

        data = response.json()

        return data['response']['games']

    def get_user_csgo_stats(self, steamid: str):
        url = 'http://api.steampowered.com/ISteamUserStats/GetUserStatsForGame/v0002/?appid=730&key=2FA14ED02A1D7CCC0E4FCA80AE6AE194&steamid=' + steamid
        response = requests.get(url)

        data = response.json()

        data = data['playerstats']['stats']

        stats_list = {}
        for stat in data:
            stats_list[stat['name']] = stat['value']

        return stats_list
