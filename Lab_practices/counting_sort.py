
def countingSort(arr):
    # Write your code here
    occurence_arr = []
    occ = []
    max = arr[0]
    for i in arr:
        if(max<i):
            max = i
            
    for i in range(0, max+1):
        occurence_arr.append(i)
        
    count = 0
    for i in range(0, len(occurence_arr)):
        for j in arr:
            if i==j:
                count += 1
        
        occurence_arr[i] = count
        count = 0
    for i in range(0, len(occurence_arr)):
        occ.append(str(occurence_arr[i]))
    
    return occ
    # for i in range(0, len(occurrences_arr)-1):

    #     occurrences_arr[i+1] = occurrences_arr[i] + occurrences_arr[i+1]
    #     print(occurrences_arr[i+1]);
    # count = 0
    # for i in range(0, len(arr)):
    #     sorted_arr.append(0)
    # for i in arr:
    #     for j in range(0, len(occurrences_arr)):
    #         if i==j:
    #             sorted_arr[occurrences_arr[j-1]] = i
    #             print(occurrences_arr)
    # return sorted_arr


print(countingSort([11, 30, 24, 7, 31, 16, 39, 41, 41]))