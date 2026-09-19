from app.fpl.client import FPLClient


class PlayerService:
    def __init__(self, client: FPLClient = None):
        self.client = client or FPLClient()
        self._bootstrap = None

    def _load(self):
        if self._bootstrap is None:
            self._bootstrap = self.client.get_bootstrap()
        return self._bootstrap

    def search(self, term: str):
        term = term.lower().strip()
        players = self._load()["elements"]
        matches = []
        for p in players:
            haystack = f"{p['first_name']} {p['second_name']} {p['web_name']}".lower()
            if term in haystack:
                matches.append(p)
        return matches

    def get_by_id(self, fpl_id: int):
        players = self._load()["elements"]
        for p in players:
            if p["id"] == fpl_id:
                return p
        return None