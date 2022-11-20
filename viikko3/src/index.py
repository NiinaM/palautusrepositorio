import requests
from player import Player

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2021-22/players"
    response = requests.get(url).json()

    print("JSON-muotoinen vastaus:")
    print(response)

    players = []

    for player_dict in response:
        player = Player(
            player_dict['name'],
            player_dict['team'],
            player_dict['goals'],
            player_dict['assists'],
            player_dict['nationality']
            
        )

        players.append(player)

    finnish_players = sorted(filter(lambda x: x.nationality == "FIN", players), key=lambda x: x.count_goals_assists(), reverse=True)

    print("Oliot:")

    for player in finnish_players:
        print(player)

main()