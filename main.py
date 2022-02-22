from timeit import timeit
from Levenshtein import distance as lev

set_forbidden_names = ["adolf hitler", "barack obama"]


def calculate_levenshtein_distance(name):
    score = 0
    min_score = 99999
    name = check_words(name)

    for f in set_forbidden_names:
        score = lev(name, f)

        if(score < min_score):
            min_score = score

    return min_score


def check_words(name):
    if "1" in name:
        name = name.replace("1", "i")
    if "3" in name:
        name = name.replace("3", "e")
    if "4" in name:
        name = name.replace("4", "a")
    if "5" in name:
        name = name.replace("5", "s")
    if "7" in name:
        name = name.replace("7", "t")
    if "8" in name:
        name = name.replace("8", "b")
    if "0" in name:
        name = name.replace("0", "o")

    return name


name = "pedro henrique da silva"

params = {"number": 10000, "globals": globals()}

print(timeit("calculate_levenshtein_distance(name)", **params))

print((calculate_levenshtein_distance(name)))
