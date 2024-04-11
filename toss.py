import random
import user_first
def toss():
    cpu_guess=random.randint(0,11)
    user_guess=int(input("Enter an integer "))
    chosing=input("\nIt is Toss Time\n\t Enter odd or even\t")
    sum=int(cpu_guess)+int(user_guess)
    return chosing,sum
def toss_won():
    while True:
        chose=input("You won the Toss\n Choose 1 for bat and 2 bowl")
        if chose=='1':
            user_first.user_bat()
        elif chose=='2':
            user_first.user_bowl()
        else:
            break
def toss_loss():
    while True:
        chose=random.randint(0,1)
        if chose==0:
            print("cpu choose to ball first")
            user_first.user_bat()
        elif chose==1:
            print("cpu choose to bat first")
            user_first.user_bowl()
        else:
            break