# User FiltrationCondition class to created the new get_results_with_filter function
# that use to send to swapi.sw_utils.get_all_result() as the process_function argument

import traceback


class FiltrationCondition:
    filtration_condition_str = ""

    # If eval command allow contain those words
    # will cause major security problems
    eval_unsafe_string_blacklist = ['__', 'import', 'system'
                                    'class', 'bases', 'subclasses', 'lambda']

    def __init__(self, new_filtration_condition_str):
        # filtration_condition_str maybe like this:
        #     """True if int(vehicle["max_atmosphering_speed"]) > 1000 else False"""
        self.filtration_condition_str = new_filtration_condition_str

    def get_results_with_filter(self, r_json, resutls_return_list: list):
        for eval_unsafe_string in self.eval_unsafe_string_blacklist:
            if eval_unsafe_string in self.filtration_condition_str:
                error_msg = "The filtration_condition_str contain illegal string or command!"
                raise Exception(f"{error_msg} : {eval_unsafe_string}\n{self.filtration_condition_str}")

        for vehicle in r_json["results"]:
            try:
                is_target = eval(self.filtration_condition_str)
                if is_target:
                    resutls_return_list.append(vehicle)
            except Exception:
                traceback.print_exc()
                print(vehicle)
