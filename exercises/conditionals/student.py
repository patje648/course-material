def total_cost(amount):
    if amount < 100:
        amount += 10
    if amount >= 200:
        amount *= 0.95
    return amount

def my_abs(x):
    if x <0:
        return -x
    else:
        return x


def sign(x):
    if x <0:
        return -1
    elif x==0:
        return 0
    else:
        return 1
    
def rock_paper_scissors(player1_choice, player2_choice):
    rock = 0
    paper = 1
    scissors = 2
    if player1_choice == player2_choice:
        return 0
    elif player1_choice == rock and player2_choice == scissors:
        return 1
    elif player1_choice == paper and player2_choice == rock:
        return 1
    elif player1_choice == scissors and player2_choice == paper:
        return 1
    else:
        return 2   