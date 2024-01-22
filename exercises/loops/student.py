def print_numbers(a, b, step):
    current=a 
    while current <b:
        print(current)
        current+=step

def thanos(queue_size, target_size):
    snapcount=0
    while queue_size> target_size:
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
