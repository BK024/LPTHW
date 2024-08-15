import pytest

from Exercise import exercise_one, cities_list
from Solution import exercise_one_sol


# ANSI color codes
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
RESET = "\033[0m"

expected_output = [
    {"city": "Colombo", "mood": "tired", "cost_list": 50.26},
    {"city": "Kandy", "mood": "energetic", "cost_list": 45.34},
    {"city": "Galle", "mood": "adventurous", "cost_list": 23.00},
    {"city": "Jaffna", "mood": "tired", "cost_list": 99.99},
    {"city": "Negombo", "mood": "energetic", "cost_list": 50.26},
    {"city": "Anuradhapura", "mood": "adventurous", "cost_list": 45.34},
    {"city": "Trincomalee", "mood": "tired", "cost_list": 23.00},
    {"city": "Batticaloa", "mood": "energetic", "cost_list": 99.99},
    {"city": "Ratnapura", "mood": "adventurous", "cost_list": 50.26},
    {"city": "Matara", "mood": "tired", "cost_list": 45.34}
]


def assert_ex_one(result):
    try:
        assert len(result) == len(cities_list), (f"\n\n\t\t{BLUE}Expected that the amount of elements in the result \n"
                                                 f"list are the same as the amount of cities. \n\t\tInstead the amount "
                                                 f"of elements in the result list was  {len(result)}, \n\t\tthe result"
                                                 f" list was: {result}{RESET}")

        assert result == expected_output, (f"\n\n\t\t{BLUE}Expected a list with dictionaries that contain the cities"
                                           f" and their data. Like so: \n\n{expected_output}\n\n "
                                           f"but got\n\n {result}\n\n\n\n{RESET}")

        print(f"\n\n{GREEN}All tests passed{RESET}\n\n")
    except AssertionError as e:
        print(e)
        raise e


def test_exercise_one():
    result = exercise_one()
    assert_ex_one(result)


def test_exercise_one_sol():
    result = exercise_one_sol()
    assert_ex_one(result)


