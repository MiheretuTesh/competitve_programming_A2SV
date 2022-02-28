
minutes = list(map(int,input().split()))

def NewYearHurry(arr):
    lm = arr[0]
    mn = arr[-1]
    arr1 = []
    count = 0
    totalTime = 240
    curr = totalTime - mn
    for i in range(1, lm+1):
        arr1.append(i*5)
    for i in arr1:
        if(curr >= i):
            curr -= i
            count += 1
        else:
            break
    return count

print(NewYearHurry(minutes))