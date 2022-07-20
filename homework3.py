from statistics import median


def split_male_female(args):
    """
    takes a list of persons and divides it to male and female
    :param args: the list of persons to be divided
    :return: two lists of persons
    """
    female_set = {}
    male_set = {}
    for key, item in args.items():
        if item["sex"] == "male":
            male_set[key] = item
        if item["sex"] == "female":
            female_set[key] = item
    return female_set, male_set


def find_median_average(args):
    """
    takes a list of persons and finds the age average and median of all the people
    :param args: the list of persons to be divided
    :return: only prints the average and median
    """
    age_sum = 0
    age_median = {}
    for key, item in args.items():
        age_sum += item["age"]
        age_median[key] = item["age"]
    age_avg = age_sum / len(args)
    age_med_num = median(age_median.values())
    print(f"The average age of this group of people is {age_avg}")
    print(f"The median age of this group of people is {age_med_num}")


def print_values_above(args, num=0):
    """
    takes a list of persons and prints only the persons who's age is above a certain number
    :param args: the list of persons to be divided
    :param num: the number that is the age in the check for persons to be above
    :return: only prints said persons
    """
    if num <= 0:
        print(args)
    for key, item in args.items():
        if item["age"] > num:
            print(item)


if __name__ == '__main__':
    data_set = {
        1: {"name": "Noam", "age": 26, "sex": "male"},
        2: {"name": "Tal", "age": 25, "sex": "female"},
        3: {"name": "Omri", "age": 37, "sex": "male"}
    }
    female_set, male_set = split_male_female(data_set)
    print(f"These are the males: {male_set}")
    print(f"These are the females: {female_set}")
    find_median_average(data_set)
    print_values_above(data_set, 26)



