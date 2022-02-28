def countingValleys(steps, path):
    # Write your code here
    circle = 0
    level = 0
    for i in range(0,len(path)):
        if(path[i]=="D"):
            level -=1
        elif((path[i]=="U") and (level+1==0)):
            level+=1
            circle+=1
        elif(path[i]=="D" and (level-1)==0):
            level -= 1
            circle +=1
        else:
            level+=1
    return circle

print(countingValleys(8,"UDDDUDUU"))