import requests

pokemon_base_url = "https://pokeapi.co/api/v2/pokemon/"

def get_pokemon_json(pokemon): 
    """
    Gets JSON data for a specific Pokemon from the PokeAPI.

    Args:
        pokemon (str): The name of the Pokemon to retrieve JSON data for.

    Returns:
        dict: A dictionary containing JSON data for the specified Pokemon.

    Raises:
        SystemExit: If the api call to PokeAPI fails.
    """
    url = pokemon_base_url + pokemon
    try:
        assert pokemon
        response = requests.get(url)
        result = response.json()
        return result
    except requests.exceptions.RequestException as error:
        raise SystemExit(error)
