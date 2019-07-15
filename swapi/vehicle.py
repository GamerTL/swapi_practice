from swapi.constant_variables import *
from swapi import sw_utils
from swapi.filtration_condition import FiltrationCondition as FC


class Vehicle:
    @staticmethod
    def get_all_vehicles_results():
        sended_require_url: str = f"{SW_API_BASE_URL}/{API_NAME_VEHICLES}/"
        all_vehicles_results = []
        sw_utils.get_all_result(sended_require_url, all_vehicles_results,
                                require_params={"format": FORMAT_JSON})
        return all_vehicles_results

    @staticmethod
    def get_vehicles_with_specific_filtration_condition(api_url, filtration_condition):
        results_list = []
        sw_utils.get_all_result(api_url, results_list, process_function=filtration_condition)
        return results_list


if __name__ == "__main__":
    # MAX_ATMOSPHERING_SPEED_OVER_100 = \
    #     """True if int(vehicle["max_atmosphering_speed"]) > 1200 else False"""

    c1 = """'sa' in vehicle["name"] or 'Sa' in vehicle["name"]"""
    c2 = """'sa' in vehicle["model"] or 'Sa' in vehicle["model"]"""

    MAX_ATMOSPHERING_SPEED_OVER_100 = \
        f"""True if ({c1} or {c2}) else False"""

    require_url = f"{SW_API_BASE_URL}/{API_NAME_VEHICLES}/?format={FORMAT_JSON}"
    new_fc = FC(MAX_ATMOSPHERING_SPEED_OVER_100)

    return_list = \
        Vehicle.get_vehicles_with_specific_filtration_condition(
            require_url, new_fc.get_results_with_filter)

    for data in return_list:
        for k, v in data.items():
            if k == "max_atmosphering_speed":
                print(f"Vehicle Neme: {data['name']}, Model: {data['model']}"
                      f"Max Atmosphering Speed: {data['max_atmosphering_speed']}")

    pass
