import random
def user_bowling():
    cpu_score=0
    while True:
        cpu_bat=random.randint(0,6)
        user_bowl=int(input("Enter a number between 0 to 6\t"))
        if cpu_bat==user_bowl:
            print("Cpu scored: "+str(cpu_bat))
            print("Wicket!!")
            print("Total Score of Cpu: "+str(cpu_score))
            break
        else:
            print("Cpu scored: "+str(cpu_bat))
            cpu_score+=cpu_bat
            print("Total Score: "+str(cpu_score))
    return cpu_score
def user_batting():
    user_score=0
    while True:
        cpu_bowl=random.randint(0,6)
        user_bat=int(input("Enter a number between 0 to 6\t"))
        if cpu_bowl==user_bat:
            print("cpu guessed "+str(cpu_bowl))
            print("wicket!!!")
            print("Total score of You: "+str(user_score))
            break
        else:
            user_score+=user_bat
            print("cpu guessed "+str(cpu_bowl))
            print("Total Score: "+str(user_score))
    return user_score

print("Welcome Cricket Tornament -2024")
print("=================================")
cpu_guess=random.randint(0,11)
user_guess=input("\nIt is Toss Time\n\t Enter odd or even\t")
sum=cpu_guess+user_guess
if sum%2==0:
    if cpu_guess.lower=='even':
        while True:
            chose=input("You won the Toss\n Choose 1 for bat and 2 bowl")
            if chose=='1':
                user_batting()
            elif chose=='2':
                user_bowling()
            else:
                break
    else:
        chose=random.randint(0,1)
        if chose==0:
            print("cpu choose to ball first")
            user_batting()
        elif chose==1:
            print("cpu choose to bat first")
            user_bowling()
        




cpu_score=user_bowling()
user_score=user_batting()
