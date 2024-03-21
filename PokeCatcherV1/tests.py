import json
import pytest
import api
import utils

def test_get_pokemon_json():
    """
    Test for verifying the correctness of `get_pokemon_json`
    Checks that valid inputs return the correct Pokemon JSON.
    """
    json_data = api.get_pokemon_json("magikarp")
    assert(type(json_data) == type({}))
    assert(json_data['name'] == "magikarp")
    assert (json_data['weight'] == 100)

    json_data = api.get_pokemon_json("snorlax")
    assert(type(json_data) == type({}))
    assert(json_data['name'] == "snorlax")
    assert (json_data['height'] == 21)

def test_get_pokemon_json_bad_input():
    """
    Test for verifying the correctness of `get_pokemon_json`
    Checks that invalid inputs return Exception
    """
    with pytest.raises(Exception):
        json_data = api.get_pokemon_json("charmander1")

    with pytest.raises(Exception):
        json_data = api.get_pokemon_json("")
        

def test_get_random_pokemon():
    """
    Test for verifying the correctness of `get_random_pokemon`
    Checks that the random pokemon from `get_random_pokemon` exists in the `pokemon.txt' file.
    """
    random_pokemon = utils.get_random_pokemon()
    with open("pokemon.txt", 'r') as text_file:  
        for line in text_file:
            if random_pokemon in line:
                return
        raise Exception

def test_extract_pokemon_data():
    """
    Test for verifying the correctness of `extract_pokemon_data`.
    It tests that the function correctly extracts and formats data from the provided JSON.
    """
    pokemon_json = api.get_pokemon_json("charmander")
    formatted_data = utils.extract_pokemon_data(pokemon_json)
    assert(formatted_data['name'] == "charmander")
    assert(formatted_data['types'] == ["fire"])
    assert(formatted_data['order'] == 5)
    assert(formatted_data['base_stat_hp'] == 39)
    assert(formatted_data['base_stat_attack'] == 52)
    assert(formatted_data['base_stat_defense'] == 43)
    assert(formatted_data['base_stat_special_attack'] == 60)
    assert(formatted_data['base_stat_special_defense'] == 50)
    assert(formatted_data['base_stat_speed'] == 65)
    assert(formatted_data['sprite'] == "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/4.png")