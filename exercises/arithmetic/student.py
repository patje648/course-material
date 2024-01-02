def five():
    return 5

def triple(x):
    return x*3

def average (x, y):
    return (x+y)/2

def distance(x1,y1,x2,y2):
    return ((x2-x1)**2+(y2-y1)**2)**(1/2)

from math import floor, ceil
def buses_needed(people_count, bus_capacity):
    people_count=int(input())
    bus_capacity=int(input())
    x=people_count/bus_capacity
    buses_neede=ceil(x)
    return buses_neede

def pizza(n_people,slices_per_pizza):
    slice=n_people/slices_per_pizza
    return slice 

def cake(eggs):
   cake=eggs//5
   return cake
   
def candy_per_child(candy_count,child_count):
    snoep=candy_count//child_count
    return snoep

def coins(amount):
    five_coins = amount // 5
    amount -= 5 * five_coins
    two_coins = amount // 2
    amount -= 2 * two_coins
    one_coins = amount
    return five_coins + two_coins + one_coins

def leftover_candy(candy_count, child_count):
    rest= candy_count % child_count
    return rest

def internet_costs(duration_in_seconds, cost_per_block):
       return ceil(duration_in_seconds / 360) * cost_per_block  

def middle(a, b, c):
    return (a + b + c) - min(a, b, c) - max(a, b, c)

def last_digit(n):
     return n%10  

def drop_last_digit(n):
    return n //10

def next_player(player, player_count):
    return (player+1) % player_count

def next_player2(player, player_count):
    return player % player_count +1