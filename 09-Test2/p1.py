def f(player1, player2):
    score1 = 0
    score2 = 0

    for n in player1:
        if n.isdigit():
            score1 += int(n) 
        else:
            score1 += 10

    for n in player2:
        if n.isdigit():
            score2 += int(n) 
        else:
            score2 += 10

    if score1 >= score2:
        return True
    else:
        return False

if __name__ == "__main__":
    #check your program in this place
    print(f("AJ972","AQT72")) 
    print(f("9532","K8") ) 