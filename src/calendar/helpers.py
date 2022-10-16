from math import modf
from numpy import ndarray, array, append


def min_to_dec(minutes):
    return minutes/60


def dec_to_min(decimal):
    return int(decimal * 60)


def time_formatter(time):
    if isinstance(time, int) or isinstance(time, float):
        minutes, hours = modf(time)
        minutes = round(minutes, 2)
        return str(int(hours)).zfill(2) + ':' + str(int(dec_to_min(minutes))).zfill(2)
    elif isinstance(time, ndarray):
        label_array = array([])
        for elt in time:
            minutes, hours = modf(elt)
            minutes = round(minutes, 2)
            label = str(int(hours)).zfill(2) + ':' + str(dec_to_min(minutes)).zfill(2)
            label_array = append(label_array, label)
        return label_array
    else:
        raise TypeError("time_formatter requests a 'numpy.ndarray' or an 'int' type argument")


def day_to_string(day: int) -> str:
    if day == 0:
        return "Monday"
    elif day == 1:
        return "Tuesday"
    elif day == 2:
        return "Wednesday"
    elif day == 3:
        return "Thursday"
    elif day == 4:
        return "Friday"
    elif day == 5:
        return "Saturday"
    elif day == 6:
        return "Sunday"
    else:
        raise ValueError("day_to_string: Not a valid day received")
