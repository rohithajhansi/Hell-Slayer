from random import randint

character = {'hp': 1, 'mp': 1, 'attack': 1, 'defense': 1, 'name': input('Enter your character name: ')}

chest = {key: randint(1, 10) for key in ["attack", "defense", "hp", "mp"]}


items = ['wooden club', 'flashlight', 'knife', 'map', 'compass','grenade','bomb','bottle of water' ,'lighter' ,'matches','candle','torch','lantern','flashlight','flashlight','first-aid-kit', 'bandages', 'medicine', 'food', 'water', 'sleeping-bag', 'tent', 'fishing-rod', 'fishing-net', 'fishing-line','shield','oxygen-tank','ladder','rope','axe']

def fun(x):
    """Creates a function that will be called when the player encounters a random item"""
    if x in ['shield','oxygen-tank','ladder','rope','axe']:
        return True
    else:
        return False
necessary_items = list(filter(fun, items))
unnecessary_items = list(filter(lambda x: not fun(x), items))

demons = [
    {
        "name": "Susamaru",
        "hp": 1,
        "attack": 1,
        "defense": 1
    },
    {
        "name": "Yahaba",
        "hp": 2,
        "attack": 2,
        "defense": 2
    },
    {
        "name": "Rui",
        "hp": 3,
        "attack": 3,
        "defense": 3
    },
    {
        "name": "Kyogai",
        "hp": 4,
        "attack": 4,
        "defense": 4
    },
    {
        "name": "Daki",
        "hp": 5,
        "attack": 5,
        "defense": 5
    },
    {
        "name": "Gyutaro",
        "hp": 6,
        "attack": 6,
        "defense": 6
    },
    {
        "name": "Hantengu",
        "hp": 7,
        "attack": 7,
        "defense": 7
    },
    {
        "name": "Akaza",
        "hp": 8,
        "attack": 8,
        "defense": 8
    },
    {
        "name": "Doma",
        "hp": 9,
        "attack":9 ,
        "defense": 9
    },
    {
        "name": "Kokushibo",
        "hp": 10,
        "attack": 10,
        "defense": 10
    },
    {
        "name": "Muzan Kibutsuji",
        "hp": 11,
        "attack": 11,
        "defense": 11
    },
]
