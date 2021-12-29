class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        counter = Counter(nums)
        nonUsedElements = []
        ans = 0
        count = 0
        for i in range(nums[0], nums[-1]):
            if i not in counter:
                nonUsedElements.append(i)
        max_num = nums[-1]
        for i in range(len(nums)):
            max_num += 1
            nonUsedElements.append(max_num)
        print(nonUsedElements)
        for i in counter:
            while counter[i] > 1:
                if nonUsedElements[count] - i > 0 and len(nonUsedElements) > count:
                    ans += nonUsedElements[count] - i
                    count += 1
                    counter[i] -= 1
                    print(ans)
                else:
                    count += 1
        return ans