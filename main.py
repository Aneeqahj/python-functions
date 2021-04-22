# Exercise 1

def distance_from_zero(x):
    if type(x) == int or type(x) == float:
        return abs(x)
    else:
        return "Nope"


print(distance_from_zero("what"))
print(distance_from_zero(-5))
print(distance_from_zero(6))
