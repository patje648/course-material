def total_cost(amount):
    if amount < 100:
        amount += 10
    if amount >= 200:
        amount *= 0.95
    return amount

def my_abs(x):
    if x <0:
        return x*2
    else:
        return x
