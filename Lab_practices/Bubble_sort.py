def countSwaps(a):
    # Write your code here
    countSwap = 0
    for i in range(len(a)-1):
        for j in range(0, len(a)-1):
            if(a[j]>a[j+1]):
                a[j], a[j+1] = a[j+1], a[j]
                countSwap += 1
            else:
                continue
    print("Array is sorted in "+ str(countSwap)+ " swaps.")
    print("First Element: " + str(a[0]))
    print("Last Element: "+ str(a[len(a)-1]))