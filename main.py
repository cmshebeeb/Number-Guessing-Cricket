#random function,modules
import innings
import random
import toss
import user_first

print("Welcome Cricket Tornament -2024")
print("=================================")
chosing,sum=toss.toss()
if sum%2==0:
    if chosing.lower=='even':
        toss.toss_won()
    else:
        toss.toss_loss()
else:
    if chosing.lower=='odd':
        while True:
            chose=input("You won the Toss\n Choose 1 for bat and 2 bowl")
            if chose=='1':
                user_first.user_bat()
            elif chose=='2':
                user_first.user_bowl
            else:
                break
    else:
        chose=random.randint(0,1)
        if chose==0:
            print("cpu choose to ball first")
            user_first.user_bat()
        elif chose==1:
            print("cpu choose to bat first")
            user_first.user_bowl()
