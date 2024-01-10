from collections import namedtuple


def split_name(full_name):
    spatie= full_name.find(" ")
    lettervn= full_name[0:spatie]
    letteran=full_name[spatie+1:]
    return lettervn, letteran

def all_equal(xs):
    for i in range(1, len(xs)):
        if xs[i-1] != xs[i]:
            return False
    return True

def all_different(xs):
    for i in range(len(xs)):
        for j in range(i + 1, len(xs)):
            if xs[i] == xs[j]:
                return False
    return True

def increasing(ns):
    for i in range(1, len(ns)):
        if ns[i-1] > ns[i]:
            return False
    return True

def subtuple(xs, ys):
    for i in range(len(xs)-len(ys)+1):
        if xs[i:i+len(ys)] == ys:
            return True
    return False

def passing_percentage(grades):
    passing = 0
    for grade in grades:
        if grade >= 10:
            passing += 1
    return passing / len(grades) * 100

def heatwave(temperatures):
    above_25_count = 0
    above_30_count = 0
    for temperature in temperatures:
        if temperature < 25:
            above_25_count = 0
            above_30_count = 0
        else:
            above_25_count += 1
            if temperature >= 30:
                above_30_count += 1
            if above_25_count >= 5 and above_30_count >= 3:
                return True
    return False    
