import requests

API = 'https://akabab.github.io/superhero-api/api'

def get_hero(competitors: list) -> str:
    response = requests.get(API)
    response.raise_for_status()
    for hero in competitors:
        for result in requests.get(API + f'/search/{hero}').json()['results']:
            superheroes[hero] = int(result['powerstats']['intelligence'])
    winner =  max(superheroes, key=superheroes.get)
    return f'The Winner is {winner} with intelligence {superheroes[winner]}'

if __name__ == '__main__':
    superheroes = {}
    heroes_list = ['Hulk', 'Captain America', 'Thanos']
    print(get_hero(heroes_list))