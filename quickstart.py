import webbrowser
from urllib.parse import quote

rwr_uri = "steam://rungameid/270150//"
rwr_cmd = ["map=media/packages/_muttrah_map_project/maps/map18", "verbose",
           "debugmode", "metagame_debugmode",
           "no_ai", "no_simulation", "big_water"]
webbrowser.open_new(f"{rwr_uri}{'%20'.join(quote(c, safe='') for c in rwr_cmd)}")
