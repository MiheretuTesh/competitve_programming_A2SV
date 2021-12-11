#User function Template for python3

class Solution: 
    def select(self, arr, i):
        # code here
        min = 0
        for j in range(i):
            if(arr[min]> arr[j]):
                min = j
        return min
            
            
    def selectionSort(self, arr,n):
        #code here
        
        for i in range(0, n):
            min = self.select(arr[i:], n-i)
            arr[i], arr[min+i]=arr[min+i], arr[i]
        return arr
            
soln = Solution()
a = [3,1,7,5,6,9,4]
print(soln.selectionSort(a,len(a)))