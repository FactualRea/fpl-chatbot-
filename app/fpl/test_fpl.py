from app.fpl.client import FPLClient

fpl = FPLClient()

data = fpl.get_getbootstrap()

print("Players:", len(data["elements"]))
print("Teams:", len(data["teams"]))
print("Gameweeks:", len(data["events"]))