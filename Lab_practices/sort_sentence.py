class Solution(object):
    def sortSentence(self, s):
        arr = s.split(" ")

        sorted_sentence = []

        for i in range(0, len(arr)):
            sorted_sentence.append("")
        for i in arr:
            num = i[len(i)-1]
            index = int(num) - 1
            word = i[:len(i)-1]
            sorted_sentence[index] = word
        return " ".join(sorted_sentence)


soln = Solution()
print(soln.sortSentence("Myself2 Me1 I4 and3"))
