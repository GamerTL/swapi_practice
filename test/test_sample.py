from swapi.constant_variables import *
from swapi import sw_utils
from swapi import films
from swapi.vehicle import Vehicle
from swapi.filtration_condition import FiltrationCondition as FC


class TestClass:
    def test_show_the_films_species(self):
        films_title = "Revenge of the Sith"
        action_require_url = f"{SW_API_BASE_URL}/{API_NAME_FILMS}/?format={FORMAT_JSON}&search={films_title}"
        return_data = films.get_films_results(action_require_url)
        if len(return_data) == 1:
            return_data[0]['species'].sort(key=lambda x: int(x.split('/')[-2]))
            print(f"Films Title: {return_data[0]['title']}\n"
                  f"Species Count: {len(return_data[0]['species'])}\n"
                  f"Species: ")
            print(*return_data[0]['species'], sep='\n')
        assert return_data is not None

    def test_show_the_films_characters_cover_how_many_species(self):
        films_title = "Revenge of the Sith"
        action_require_url = f"{SW_API_BASE_URL}/{API_NAME_FILMS}/?format={FORMAT_JSON}&search={films_title}"
        return_data = films.get_specific_films_character_species_count(action_require_url)
        print(f"Films Title: {return_data['films_title']}\n"
              f"Character Species Count: {return_data['character_species_count']}\n"
              f"Species:")
        print(*return_data['character_species_urls'], sep='\n')
        assert return_data['character_species_urls'] is not None

    def test_show_films_name_that_sort_by_episode_id(self):
        action_require_url = f"{SW_API_BASE_URL}/{API_NAME_FILMS}/?format={FORMAT_JSON}"
        return_films_data_list = []
        sw_utils.get_all_result(action_require_url, return_films_data_list)
        return_films_data_list.sort(key=lambda films_dict: int(films_dict["episode_id"]))

        for films_data in return_films_data_list:
            print(f"Films Title: {films_data['title']} ; Episode Id: {films_data['episode_id']}")

        for i in range(len(return_films_data_list) - 1):
            assert int(return_films_data_list[i]['episode_id']) < \
                   int(return_films_data_list[i+1]['episode_id'])

    def test_find_out_all_vehicles_which_max_atmosphering_speed_is_over_1000(self):
        action_require_url = f"{SW_API_BASE_URL}/{API_NAME_VEHICLES}/?format={FORMAT_JSON}"

        eval_command = """True if int(vehicle["max_atmosphering_speed"]) > 1000 else False"""
        new_filtration_condition = FC(eval_command)

        return_vehicle_list = Vehicle.get_vehicles_with_specific_filtration_condition(
            action_require_url, new_filtration_condition.get_results_with_filter)

        for vehicle_dict in return_vehicle_list:
            print(f"Vehicle Neme: {vehicle_dict['name']}, Model: {vehicle_dict['model']}"
                  f"MAS: {vehicle_dict['max_atmosphering_speed']}")

        for vehicle_dict in return_vehicle_list:
            assert int(vehicle_dict['max_atmosphering_speed']) > 1000

    def test_get_all_films_result(self):
        action_require_url = f"{SW_API_BASE_URL}/{API_NAME_FILMS}/?format={FORMAT_JSON}"
        return_data = films.get_films_results(action_require_url)
        assert len(return_data) == 7

