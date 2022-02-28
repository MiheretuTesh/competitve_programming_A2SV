class Solution(object):
    def fizzBuzz(self, n):
        collection = []
        for i in range(1, n+1):
            if(i%3==0 and i%5==0):
                collection.append("FizzBuzz")
            elif(i%3==0):
                collection.append("Fizz")
            elif(i%5==0):
                collection.append("Buzz")
            else:
                collection.append(str(i))
        return collection
        """
        :type n: int
        :rtype: List[str]
        """
