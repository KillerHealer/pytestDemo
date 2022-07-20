import homework3
import pytest
import logging

logging.basicConfig(level=logging.DEBUG)
mylogger = logging.getLogger()


def test_split_male_female():
    """
    tests split_male_female()
    :return: 0/1
    """
    male_set = {}
    female_set = {}
    data_set = {
        1: {"name": "Noam", "age": 26, "sex": "male"},
        2: {"name": "Tal", "age": 25, "sex": "female"},
        3: {"name": "Omri", "age": 37, "sex": "male"}
    }
    female_set, male_set = homework3.split_male_female(data_set)
    mylogger.warning("in test for split_male_female")
    assert male_set[male_set.__iter__().__next__()]["sex"] == "male" \
           and female_set[female_set.__iter__().__next__()]["sex"] == "female"


def test_find_median_average(capsys):
    """
    tests find_median_average
    :return: 0/1
    """
    data_set = {
        1: {"name": "Noam", "age": 26, "sex": "male"},
        2: {"name": "Tal", "age": 25, "sex": "female"},
        3: {"name": "Omri", "age": 37, "sex": "male"}
    }
    homework3.find_median_average(data_set)
    out, err = capsys.readouterr()
    mylogger.warning("in test for find_median_average")
    assert "29.333333333333332" in out


def test_print_values_above(capsys):
    """
    tests print_values_above()
    :return: 0/1
    """
    data_set = {
        1: {"name": "Noam", "age": 26, "sex": "male"},
        2: {"name": "Tal", "age": 25, "sex": "female"},
        3: {"name": "Omri", "age": 37, "sex": "male"}
    }
    homework3.print_values_above(data_set,27)
    out, err = capsys.readouterr()
    mylogger.warning("in test for print_values_above")
    assert out == "{'name': 'Omri', 'age': 37, 'sex': 'male'}\n"

