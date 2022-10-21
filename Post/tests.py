from django.test import TestCase


def flatten(lst) :
    result = []
    for item in lst :
        if type(item) == list :
            result += flatten(item)
        else :
            result += [item]
    return result
# Create your tests here.
a = [[1,2,3]]
b = flatten(a)

print(b)