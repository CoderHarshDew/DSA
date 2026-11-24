class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        runningSum = list()
        runningSum.append(nums[0])

        for i in range(1, len(nums)):
            runningSum.append(runningSum[i-1] + nums[i])

        return runningSum


# The pattern is to create a runningSum and for ith index take the i-1 th sum
# and add element i of nums to it and append it (store it) on ith index of running sum
# As the loop runs n-1 times, and we allocate an array equally big as nums
# the time & space complexities are both O(n)