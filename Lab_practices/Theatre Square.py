from math import ceil 

def theatreSquare(n, m, a):
    num = ceil(n/a)
    num1 = ceil(m/a)
    
    return num * num1

print(theatreSquare(6,6,4))
print(theatreSquare(1,1,1))
print(theatreSquare(6,3,4))