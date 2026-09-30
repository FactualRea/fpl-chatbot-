from app.fpl.client import FPLClient

fpl = FPLClient()

data = fpl.get_bootstrap()

player = data["elements"][0]

print(player)