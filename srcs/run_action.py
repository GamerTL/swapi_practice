from swapi.constant_variables import *
from swapi import sw_utils
from swapi import films
from swapi.vehicle import Vehicle
from swapi.filtration_condition import FiltrationCondition as FC


def show_the_films_species():
    films_title = "Revenge of the Sith"
    action_require_url = f"{SW_API_BASE_URL}/{API_NAME_FILMS}/?format={FORMAT_JSON}&search={films_title}"
    return_data = films.get_films_results(action_require_url)
    if len(return_data) == 1:
        return_data[0]['species'].sort(key=lambda x: int(x.split('/')[-2]))
        print(f"Films Title: {return_data[0]['title']}\n"
              f"Species Count: {len(return_data[0]['species'])}\n"
              f"Species: ")
        print(*return_data[0]['species'], sep='\n')


def show_the_films_characters_cover_how_many_species():
    films_title = "Revenge of the Sith"
    action_require_url = f"{SW_API_BASE_URL}/{API_NAME_FILMS}/?format={FORMAT_JSON}&search={films_title}"
    return_data = films.get_specific_films_character_species_count(action_require_url)
    print(f"Films Title: {return_data['films_title']}\n"
          f"Character Species Count: {return_data['character_species_count']}\n"
          f"Species:")
    print(*return_data['character_species_urls'], sep='\n')


def show_films_name_that_sort_by_episode_id():
    action_require_url = f"{SW_API_BASE_URL}/{API_NAME_FILMS}/?format={FORMAT_JSON}"
    return_films_data_list = []
    sw_utils.get_all_result(action_require_url, return_films_data_list)
    return_films_data_list.sort(key=lambda films_dict: int(films_dict["episode_id"]))
    for films_data in return_films_data_list:
        print(f"Films Title: {films_data['title']} ; Episode Id: {films_data['episode_id']}")


def find_out_all_vehicles_which_max_atmosphering_speed_is_over_1000():
    action_require_url = f"{SW_API_BASE_URL}/{API_NAME_VEHICLES}/?format={FORMAT_JSON}"

    eval_command = """True if int(vehicle["max_atmosphering_speed"]) > 1200 else False"""
    new_filtration_condition = FC(eval_command)

    return_vehicle_list = Vehicle.get_vehicles_with_specific_filtration_condition(
        action_require_url, new_filtration_condition.get_results_with_filter)

    for vehicle_dict in return_vehicle_list:
        print(f"Vehicle Neme: {vehicle_dict['name']}, Model: {vehicle_dict['model']}"
              f"MAS: {vehicle_dict['max_atmosphering_speed']}")


def get_all_films_result():
    action_require_url = f"{SW_API_BASE_URL}/{API_NAME_FILMS}/?format={FORMAT_JSON}"
    return_data = films.get_films_results(action_require_url)
    return return_data


def test_get_all_films_result():
    return_data = get_all_films_result()
    assert len(return_data) != 7


if __name__ == '__main__':
    pass
