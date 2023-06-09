class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        sum = 0
        for i in range(len(jewels)):
            for j in range(len(stones)):
                if jewels[i] == stones[j]:
                    sum += 1
        return sum