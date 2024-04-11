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

def result(cpu_score,user_score):
    runs=abs(cpu_score-user_score)
    if cpu_score>=user_score:
        print("You loss by "+str(runs)+" Runs\n Better luck for next time")
    else:
        print("You won by "+str(runs)+" Runs\n Congratulations!!!")