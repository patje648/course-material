def reverse(lst):
    for i in range(len(lst) // 2):
        j = len(lst) - i - 1
        temp = lst[i]
        lst[i] = lst[j]
        lst[j] = temp

def is_prime(n):
    k = 2
    while k * k < n:
        if n % k == 0:
            return False
        k += 1

    return k >= 2