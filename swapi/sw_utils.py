from swapi import *
import warnings


def get_all_result(api_url: str, return_list: list, process_function=None, require_params=None):
    r_json = requests.get(api_url, params=require_params).json()

    # If require specific logical to process data, use the function to processing
    # If no, append all results to result_list
    if process_function is not None and hasattr(process_function, '__call__'):
        process_function(r_json, return_list)
    else:
        for result_dada in r_json["results"]:
            return_list.append(result_dada)

    # Go through all pagination to get all data.
    if "next" in r_json:  # Make sure return json dict have 'next' key
        # Make sure 'next' key content value
        if r_json["next"] is not None and len(r_json["next"]) != 0:
            return get_all_result(r_json["next"], return_list, process_function)
        else:
            return
    else:
        warning_msg = f"\n### The result from URL:['{api_url}'] not contain ['next'] key\n" + \
                      f"### Result JSON data:\n\t{str(r_json)}"
        warnings.warn(warning_msg)
