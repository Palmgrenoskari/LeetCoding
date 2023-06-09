class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sum = 0
        cumulative_sum = []
        for num in nums:
            sum += num
            cumulative_sum.append(sum)
        return cumulative_sum
            