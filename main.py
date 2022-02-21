from timeit import timeit
from Levenshtein import distance as lev

setForbiddenNames = set(map(str.casefold, [
    'Corona', 'Clorivaldo', 'Pfizernaldo', 'Hulk', 'Naruto', 'Goku', 'Cloroquina', 'Hitler']))


def calculateLevenshteinDistance(name):
    for n in name.split():
        for f in setForbiddenNames:
            if(lev(n.casefold(), f.casefold()) <= 3):
                return False

    return True


name = 'Pedro da H1t7er Silva'

params = {'number': 10000, 'globals': globals()}

print(timeit('calculateLevenshteinDistance(name)', **params))

print((calculateLevenshteinDistance(name)))
