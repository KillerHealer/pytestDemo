class Date:
    """
    My version of the Date class. Thank you very much!!!
    """
    def __init__(self, day: int, month: int, year: int):
        """
        this class gets these three params and creates a date
        :param day: int. the day of the month
        :param month: int. the month of the year
        :param year: int. 4-digit number between 1900 and 2300 to tell us the year of the date
        """
        if 1 <= day <= 31:
            self._day = day
        else:
            raise TypeError("Need integer between 1-31 as in days of the month")
        if 1 <= month <= 12:
            self._month = month
        else:
            raise TypeError("Need integer between 1-12 as in months of the year")
        if 1000 <= year <= 9999:
            self._year = year
        else:
            raise TypeError("Need integer that is 4 digits!")

    def __str__(self) -> str:
        """
        normal stringify function
        :return: how I made it to show when user is asking to stringify a Date
        """
        return f"{self._day}/{self._month}/{self._year}"

    def __eq__(self, other) -> bool:
        """
        checks to see if the day, month and year of both Dates are the same
        :param other: the other date to check against type Date
        :return: True/False if they are equal or not
        """
        if self._day == other._day and self._month == other._month and self._year == other._year:
            return True

    def __lt__(self, other) -> bool:
        """
        checks to see if 'self' is lower than 'other'
        :param other: the other date to check against type Date
        :return: true or false
        """
        if self._year < other._year:
            return True
        if self._month < other._month:
            return True
        if self._day < other._day:
            return True
        return False

    def __gt__(self, other) -> bool:
        """
        checks to see if 'self' is greater than 'other'
        :param other: the other date to check against type Date
        :return: true or false
        """
        if self._year > other._year:
            return True
        if self._month > other._month:
            return True
        if self._day > other._day:
            return True
        return False

    def __ge__(self, other) -> bool:
        """
        checks to see if 'self' is greater or equal to 'other'
        :param other: the other date to check against type Date
        :return: true or false
        """
        return not self._day < other._day and self._month < other._month and self._year < other._year

    def __le__(self, other) -> bool:
        """
        checks to see if 'self' is lower or equal to 'other'
        :param other: the other date to check against type Date
        :return: true or false
        """
        return not self._day > other._day and self._month > other._month and self._year > other._year

    def __ne__(self, other) -> bool:
        """
        checks to see if the day, month and year of both Dates are the same
        :param other: the other date to check against type Date
        :return: True/False if they are equal or not
        """
        return self._year != other._year or self._month != other._month or self._day != other._day

    def __sub__(self, other) -> int:
        """
        subtracts the days difference between 'self' and 'other'
        :param other: the other date to check against type Date
        :return: the number of days difference between 'self' and 'other'
        """

        subdif = 0
        years = 0
        months = 0
        days = 0
        if self == other:
            return subdif

        if self > other:
            gd = self
            ld = other
        else:
            gd = other
            ld = self
        tmp = ld.getNextDay()
        subdif += 1
        while tmp != gd:
            tmp = tmp.getNextDay()
            subdif += 1
        return subdif

    def isValid(self) -> bool:
        """
        checks to see if the date is valid
        from checking the amount of days in the month in specific years
        :return: True/False
        """
        if self._month == 4 or self._month == 6 \
                or self._month == 9 \
                or self._month == 11:
            if 1 <= self._day <= 30:
                return True
            else:
                return False
        if self._year % 4 == 0:
            if self._month == 2:
                if 1 <= self._day <= 29:
                    return True
                else:
                    return False
        else:
            if self._month == 2:
                if 1 <= self._day <= 28:
                    return True
                else:
                    return False

    def getNextDay(self):
        """
        takes the current day and returns the next day
        :return: the day next to self
        if today is 28/2/2016 tomorrow is 29/2/2016
        if today is 28/2/2016 tomorrow is 1/3/2017
        if today is 31/12/2000 tomorrow is 1.1.2001
        """
        if self.isValid():
            if self._month == 4 or self._month == 6 \
                    or self._month == 9 \
                    or self._month == 11:
                if self._day == 30:
                    tmp = Date(1, self._month + 1, self._year)
                    return tmp
            if self._year % 4 == 0:
                if self._month == 2:
                    if self._day == 29:
                        tmp = Date(1, self._month + 1, self._year)
                        return tmp
            else:
                if self._month == 2:
                    if self._day == 28:
                        tmp = Date(1, self._month + 1, self._year)
                        return tmp
            if self._day == 31:
                if self._month == 12:
                    tmp = Date(1, 1, self._year + 1)
                    return tmp
                else:
                    tmp = Date(1, self._month + 1, self._year)
                    return tmp
            tmp = Date(self._day + 1, self._month, self._year)
            return tmp

    def getNextDays(self, daysToAdd: int):
        """
        takes current date and adds 'daysToAdd' days to it
        :param daysToAdd: number of days to add
        :return: returns a date 'daysToAdd' after the original date
        """
        num = self._day + daysToAdd
        if self._month == 4 or self._month == 6 \
                or self._month == 9 \
                or self._month == 11:
            if num >= 31:
                dta = num - 30
                tmp = Date(dta, self._month + 1, self._year)
                return tmp
        if self._year % 4 == 0:
            if self._month == 2:
                if num >= 30:
                    dta = num - 30
                    tmp = Date(dta, self._month + 1, self._year)
                    return tmp
        else:
            if self._month == 2:
                if num >= 29:
                    dta = num - 30
                    tmp = Date(dta, self._month + 1, self._year)
                    return tmp
        if num >= 32:
            if self._month == 12:
                dta = num - 30
                tmp = Date(dta, 1, self._year + 1)
                return tmp
            else:
                dta = num - 30
                tmp = Date(dta, self._month + 1, self._year)
                return tmp
        tmp = Date(num, self._month, self._year)
        return tmp


if __name__ == '__main__':
    d1 = Date(20, 1, 2001)
    d2 = Date(20, 1, 2000)
    print(d1.__sub__(d2))
