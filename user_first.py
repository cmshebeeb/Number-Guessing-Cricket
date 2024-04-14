
import innings

def user_bat():
    user_score=innings.user_batting()
    print(" Fisrt Innings completed\n Target: "+str(user_score+1))
    cpu_score=innings.user_bowling()
    innings.result(cpu_score,user_score)
    return

def user_bowl():
    cpu_score=innings.user_bowling()
    print(" First Innings completed\n Target: "+str(cpu_score+1))
    user_score=innings.user_batting()
    innings.result(cpu_score,user_score)
    return