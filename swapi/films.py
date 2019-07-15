from swapi import *
from swapi import sw_utils
from swapi.constant_variables import *
import unittest


def get_specific_films_all_characters_url(films_api_url: str) -> dict:
    characters_url_list = []
    r = requests.get(films_api_url)
    if r.status_code == 200 and r.text != "" and r.text is not None:
        r_json = r.json()

        # Only get the first films
        for character_url in r_json["results"][0]["characters"]:
            characters_url_list.append(character_url)
    else:
        print("Requests Fail")
    return {"films_title": r_json["results"][0]["title"],
            "characters": characters_url_list}


def get_character_species_url(character_api_url: str) -> dict:
    return_character_and_species = {
        "character_url": character_api_url,
        "species_url": requests.get(character_api_url).json()["species"]  # ["species_url"]: list
    }

    return return_character_and_species


def get_specific_films_all_characters_and_species(films_api_url: str) -> dict:
    characters_url: dict = get_specific_films_all_characters_url(films_api_url)
    character_and_species_list: list = []
    for character_url in characters_url["characters"]:
        character_and_species_list.append(
            get_character_species_url(character_url)
        )

    return {"films_title": characters_url["films_title"],
            "character_and_species": character_and_species_list}


# Return {"character_species_count": <count of this film character's species>,
#         "character_species_urls": [<species list of this film character>]}
def get_specific_films_character_species_count(films_api_url: str) -> dict:
    return_dict = {
        "films_title": "",
        "character_species_count": 0,
        "character_species_urls": []
    }

    characters_and_species = \
        get_specific_films_all_characters_and_species(films_api_url)

    return_dict["films_title"] = characters_and_species["films_title"]

    for data in characters_and_species["character_and_species"]:
        if len(data["species_url"]) != 0:
            for species_url in data["species_url"]:
                if species_url not in return_dict["character_species_urls"]:
                    return_dict["character_species_urls"].append(species_url)
    return_dict["character_species_count"] = len(return_dict["character_species_urls"])

    return_dict["character_species_urls"].sort(key=lambda x: int(x.split('/')[-2]))
    return return_dict


def get_films_results(films_api_url: str) -> list:
    result_films_list = []
    sw_utils.get_all_result(films_api_url, result_films_list)
    return result_films_list
