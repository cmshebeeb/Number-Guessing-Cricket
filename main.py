#random function,modules
import toss

print("\n====================================\n\tWelcome Cricket Tornament -2024\n====================================")
chosing,sum=toss.toss()
if sum%2==0:
    if chosing.lower=='even':
        toss.toss_won()
    else:
        toss.toss_loss()
else:
    if chosing.lower=='odd':
        toss.toss_won()
    else:
        toss.toss_loss()
