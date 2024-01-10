# How do we decide if we should use a while loop or a for loop?
# Use a for loop when you know the loop should execute n times. 
# Use a while loop for reading a file into a variable. Use a while loop when asking for user input. 
# Use a while loop when the increment value is nonstandard.
from tkinter import N


def print_numbers(a, b, step):
    current = a
    while current < b:
        print(current)
        current += step

def thanos(queue_size, target_size):
    snapcount=0
    while queue_size > target_size:
        queue_size//=2
        snapcount+=1
    return snapcount

def sum_input():
    result = 0
    value = int(input("Enter integer: "))
    while value != 0:
        result += value
        value = int(input("Enter integer: "))
    print(f'The sum equals {result}.')

def factorial(n):
    result = 1
    for k in range(2, n+1):
        result *= k
    return result

def rpg2(n_sides, goal):
    count=0
    for a in range(1,n_sides+1):
        for b in range(1,n_sides+1):
            if a+b >=goal:
                count +=1
    return count / n_sides**2 * 100

def rpg3(n_sides, goal):
    count=0
    for a in range(1,n_sides+1):
        for b in range(1,n_sides+1):
            for c in range(1,n_sides+1):
                if a+b+c >=goal:
                    count +=1
    return count / n_sides**3 * 100

def invest(amount, rate, goal):
    current = amount
    year_count = 0
    while current < goal:
        current += current * rate / 100
        year_count += 1
    return year_count

def is_prime(n):
    for k in range(2, n):
        if n % k == 0:
            return False
    return n > 1

def gcd(x, y):
    for i in range(min(abs(x), abs(y)), 0, -1):
        if x % i == 0 and y % i == 0:
            return i

 