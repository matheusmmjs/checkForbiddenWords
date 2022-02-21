from timeit import timeit
from Levenshtein import distance as lev
from array import array

setForbiddenNames = ['adolf hitler', 'barack obama']


def calculateLevenshteinDistance(name):
    result = []
    name = checkWords(name)

    for f in setForbiddenNames:
        result.append(lev(name, f))

    return result


def checkWords(name):
    if '1' in name:
        name = name.replace('1', 'i')
    if '3' in name:
        name = name.replace('3', 'e')
    if '4' in name:
        name = name.replace('4', 'a')
    if '5' in name:
        name = name.replace('5', 's')
    if '7' in name:
        name = name.replace('7', 't')
    if '8' in name:
        name = name.replace('8', 'b')
    if '0' in name:
        name = name.replace('0', 'o')

    return name


name = 'pedro da h1t7er silva'

params = {'number': 10000, 'globals': globals()}

print(timeit('calculateLevenshteinDistance(name)', **params))

print((calculateLevenshteinDistance(name)))
