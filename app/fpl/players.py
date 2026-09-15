from app.fpl.client import FPLClient


class PlayerService:
    def __init__(self):
        self.fpl = FPLClient()

    def get_all_players(self):
        data = self.fpl.get_bootstrap()
        return data["elements"]

    def find_player(self, name):
        players = self.get_all_players()
        name = name.lower()
        matches = []
        for player in players:
            full_name = (
                f"{player['first_name']}"f"{player['second_name']}").lower()
            web_name = player["web_name"].lower()
            if name in full_name or name in web_name:
                matches.append(player)
        return matches