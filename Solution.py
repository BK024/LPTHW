from LPTHW import Exercise
from LPTHW.Exercise import moods_list, cost_list


def exercise_one_sol():
    data_list = []

    for idx, city in enumerate(Exercise.cities_list):
        dict_to_append_to_data_list = {}
        dict_to_append_to_data_list["city"] = city
        dict_to_append_to_data_list["mood"] = moods_list[idx % len(moods_list)]
        dict_to_append_to_data_list["cost_list"] = cost_list[idx % len(cost_list)]
        data_list.append(dict_to_append_to_data_list)

    return data_list
