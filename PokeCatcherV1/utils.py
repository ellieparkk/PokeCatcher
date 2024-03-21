import random

TOTAL_POKEMON = 1302

def get_random_pokemon():
    """
    Gets a random Pokemon from 'pokemon.txt'.

    Returns:
        str: A randomly selected Pokemon.
    """
    with open("pokemon.txt") as text_file:
        random_line = random.randrange(1, TOTAL_POKEMON)
        for i, line in enumerate(text_file):
            if i == random_line:
                text_file.close()
                return line.rstrip()

def extract_pokemon_data(pokemon_json):
    """
    Formats relevant data from a Pokemon JSON object.

    Args:
        pokemon_json (dict): A dictionary containing JSON data for a Pokemon.

    Returns:
        dict: A dictionary containing extracted Pokemon data, including name, types, order, base stats, and sprite.
    """
    pokemon_data = {
        "name": pokemon_json["name"],
        "types": [types["type"]["name"] for types in pokemon_json["types"]],
        "order": pokemon_json["order"],
        "base_stat_hp": pokemon_json['stats'][0]["base_stat"],
        "base_stat_attack": pokemon_json['stats'][1]["base_stat"],
        "base_stat_defense": pokemon_json['stats'][2]["base_stat"],
        "base_stat_special_attack": pokemon_json['stats'][3]["base_stat"],
        "base_stat_special_defense": pokemon_json['stats'][4]["base_stat"],
        "base_stat_speed": pokemon_json['stats'][5]["base_stat"],
        "sprite": pokemon_json['sprites']['front_default']
    }
    return pokemon_data

