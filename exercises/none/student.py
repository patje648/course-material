def product(a,b,c):
    if a is None:
        a=1
    if b is None:
        b=1
    if c is None:
        c=1
    return a*b*c

def multiple_choice(right_answer, given_answer):
    if right_answer==given_answer:
        return 1
    elif given_answer is None:
        return 0
    else:
        return -0.2


