n = int(input("Enter array Length: "))

arr1 = []
for i in range(n):
    arr1.append(int(input("Enter: ")))

n1 = int(input("Enter buy number: "))
b_arr = []
for i in range(n1):
    a = int(input("Enter: "))
    b_arr.append(a)
arr1.sort()

left = 0
best = 0
right = len(arr1) - 1
while left <= right:
    mid = left + (right - left)//2

    # if arr1[mid] <= :
    #     left = mid + 1
    #     best = mid + 1
    # else:
    #     right = mid - 1
print(best)
