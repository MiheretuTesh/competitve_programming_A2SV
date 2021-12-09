# #User function Template for python3

# class Solution: 
#     def select(self, arr, i):
#         # code here
#         min = arr[0]
#         for j in range(i+1, len(arr)):
#             if(min>arr[j]):
#                 min = arr[j]
#         min, arr[j] = min, arr[j]

#         return arr
            
#     def selectionSort(self, arr,n):
#         #code here
#         for i in range(0, len(arr)):
#             Solution.select(arr, i)


# #{ 
# #  Driver Code Starts
# #Initial Template for Python 3

# if __name__ == '__main__': 
#     t = int(input())
#     for _ in range(t):
#         n = int(input())
#         arr = list(map(int, input().strip().split()))
#         Solution().selectionSort(arr, n)
#         for i in range(n):
#             print(arr[i],end=" ")
#         print()
# # } Driver Code Ends

def selectionSort(arr):
    for i in range(0, len(arr)):
        min = i
        for j in range(i+1, len(arr)):
            if(arr[min]>arr[j]):
                min = j
        arr[i] ,arr[min]= arr[min], arr[i]

    return arr

print(selectionSort([4,3,6,1]))