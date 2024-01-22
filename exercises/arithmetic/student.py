from math import floor, ceil
def five():
    return 5 

def triple(x):
    return x*3

def average(x, y):
    return (x+y)/2

def distance(x1, y1, x2, y2):
    return ((x2 - x1)**2 + (y2 - y1)**2)**0.5

def buses_needed(people_count, bus_capacity):
    return ceil(people_count/bus_capacity)

def pizza(n_people, slices_per_pizza):
    return ceil(n_people/slices_per_pizza)

def cake(eggs):
    return eggs//5

def candy_per_child(candy_count, child_count):
    return candy_count//child_count

def cake2(eggs, flour):
    return min(eggs//5, flour//250)

def cake3(eggs, flour, butter, sugar):
    Eggs=eggs//5
    Four= flour//250
    Butter=butter//200
    Sugar=sugar//250
    return min(Eggs,Four,Butter,Sugar)

def cake4(eggs, flour, butter, sugar, eggs_per_cake, flour_per_cake, butter_per_cake, sugar_per_cake):
    Eggs=eggs//eggs_per_cake
    Four= flour//flour_per_cake
    Butter=butter//butter_per_cake
    Sugar=sugar//sugar_per_cake
    return min(Eggs,Four,Butter,Sugar)

def hours(duration):
    return duration//3600

def minutes(duration):
    return (duration - hours(duration) * 3600) // 60

def seconds(duration):
    return duration - hours(duration) * 3600 - minutes(duration) * 60

def coins(amount):
    five_coins = amount // 5
    amount -= 5 * five_coins
    two_coins = amount // 2
    amount -= 2 * two_coins
    one_coins = amount
    return five_coins + two_coins + one_coins

def leftover_candy(candy_count, child_count):
    return candy_count%child_count

