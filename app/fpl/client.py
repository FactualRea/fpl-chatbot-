import requests

class FPLClient:
    
    Base_URL = "https://fantasy.premierleague.com/api/"
    
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({"User-Agent" : "Mozilla/5.0"})

    def get(self, endpoint):
        url = self.Base_URL + endpoint
        response = self.session.get(url)
        response.raise_for_status()
        return response.json()

    def get_bootstrap(self):
        return self.get("bootstrap-static/")

    def get_fixtures(self):
        return self.get("fixtures/")

    def get_player_summary(self, player_id):
        return self.get(f"element-summary/{player_id}/")

    def get_live_gameweek(self, gameweek):
        return self.get(f"event/{gameweek}/live/")