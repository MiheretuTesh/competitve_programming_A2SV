class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort(reverse=True)
        n = len(piles)
        coins = 0
        c = n / 3
        for i in range(1,n,2):
            coins += piles[i]
            c -= 1
            if c == 0:
                return coins

        