
def insertionSort1(n, arr):
    # Write your code here
    lastNumber = arr[len(arr)-1]
    temp = lastNumber
    for i in range(len(arr)-1, 0, -1):
        if(lastNumber< arr[i-1]):
            arr[i] = arr[i-1]
            # print("exchanged")
            for j in arr:
                print(j, end=" ")
            print("")
            if((i-1) == 0):
                arr[i-1] = lastNumber
                for j in arr:
                    print(j, end=" ")
                print("")
        elif(lastNumber==arr[i-1]):
            arr[i] = lastNumber
            for j in arr:
                print(j, end=" ")
            print("")
            break
        else:
            arr[i] = lastNumber
            for j in arr:
                print(j, end=" ")
            print("")
            break


print(insertionSort1(3, [2, 3, 4, 5, 6, 7, 8, 9, 10, 1]))
print(insertionSort1(3, [1, 3, 5, 9, 13, 22, 27, 35, 46, 51, 55, 83, 87, 23]))
