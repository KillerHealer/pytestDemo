from homework4 import Date
import logging
import pytest
import logging

logging.basicConfig(level=logging.DEBUG)
mylogger = logging.getLogger()


@pytest.mark.Date
def test___init__():
    """
    tests to see if __init__ really created a new Date
    :return: PASSED/FAILED
    """
    d1 = Date(20, 7, 2022)
    mylogger.warning("in test for __init__")
    assert d1._day == 20
    assert d1._month == 7
    assert d1._year == 2022


@pytest.mark.Date
def test__str__():
    """
    tests to see if __str__ made a good string out of Date
    :return: PASSED/FAILED
    """
    d1 = Date(20, 7, 2022)
    mylogger.warning("in test for __str__")
    assert d1.__str__() == "20/7/2022"


@pytest.mark.Date
def test___eq__():
    """
    tests to see if __eq__ checks if 2 Dates are equal
    :return: PASSED/FAILED
    """
    d1 = Date(20, 7, 2022)
    d2 = Date(20, 7, 2022)
    mylogger.warning("in test for __eq__")
    assert d1 == d2


@pytest.mark.Date
def test___lt__():
    """
    tests to see if d2 is lower than d1
    :return: PASSED/FAILED
    """
    d1 = Date(20, 7, 2022)
    d2 = Date(20, 6, 2021)
    mylogger.warning("in test for __lt__")
    assert d2 < d1


@pytest.mark.Date
def test___gt__():
    """
    tests to see if d1 is greater than d2
    :return: PASSED/FAILED
    """
    d1 = Date(20, 7, 2022)
    d2 = Date(20, 6, 2021)
    mylogger.warning("in test for __gt__")
    assert d1 > d2


@pytest.mark.Date
def test___ge__():
    """
    tests to see if d1 is greater or equal to d2
    :return: PASSED/FAILED
    """
    d1 = Date(20, 8, 2022)
    d2 = Date(20, 7, 2022)
    mylogger.warning("in test for __ge__")
    assert d1 >= d2


@pytest.mark.Date
def test___le__():
    """
    tests to see if d1 is lower or equal to d2
    :return: PASSED/FAILED
    """
    d1 = Date(20, 6, 2022)
    d2 = Date(20, 7, 2022)
    mylogger.warning("in test for __le__")
    assert d1 <= d2


@pytest.mark.Date
def test___ne__():
    """
    tests to see if d1 is not equal to d2
    :return: PASSED/FAILED
    """
    d1 = Date(2, 7, 2020)
    d2 = Date(20, 7, 2022)
    mylogger.warning("in test for __ne__")
    assert d1 != d2


@pytest.mark.Date
def test___sub__():
    """
    tests to see if d1 - d2 = 7 days in a date perspective
    :return: PASSED/FAILED
    """
    d1 = Date(20, 7, 2022)
    d2 = Date(13, 7, 2022)
    mylogger.warning("in test for __sub__")
    assert d1.__sub__(d2) == 7


@pytest.mark.Date
def test_isValid():
    """
    checks to see if the date is valid
    from checking the amount of days in the month in specific years
    :return: PASSED/FAILED
    """
    d1 = Date(30, 9, 2021)
    d2 = Date(29, 2, 2020)
    mylogger.warning("in test for isValid")
    assert d1.isValid()
    assert d2.isValid()


@pytest.mark.Date
def test_getNextDay():
    """
    takes the current day and returns the next day
    :return: PASSED/FAILED
    if today is 28/2/2016 tomorrow is 29/2/2016
    if today is 28/2/2016 tomorrow is 1/3/2017
    if today is 31/12/2000 tomorrow is 1.1.2001
    """
    d1 = Date(30, 9, 2021)
    d2 = Date(1, 10, 2021)
    mylogger.warning("in test for getNextDay")
    assert d1.getNextDay() == d2


@pytest.mark.Date
def test_getNextDays():
    """
    checks if getNextDays takes current date and adds 'daysToAdd' days to it
    :return: PASSED/FAILED
    """
    d1 = Date(30, 9, 2021)
    d2 = Date(5, 10, 2021)
    mylogger.warning("in test for getNextDays")
    assert d1.getNextDays(5) == d2


