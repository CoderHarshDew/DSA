class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i == j:
                    continue
                if nums[i] + nums[j] == target:
                    return [i , j]

# Approach: Brute force, checks each two number combination,
# using nested loops, resulting  in O(n^2) time complexity.

    def twoSum2(self, nums: list[int], target: int) -> list[int]:
        d = dict.fromkeys(nums, 0)

        for i in range(len(nums)):
            x = target - nums[i]
            if x in d:
                for j in range(len(nums)):
                    if i == j:
                        continue
                    if nums[j] == x:
                        return [i, j]

# Approach use a  dict to look up if target - nums[i] exists
# if it does locate it via a linear search and return indexes
# Encountered a problem when the nums array contains negative values.
# The problem was taking  mod of target - nums, which is wrong as we do not need to look up their absolute difference.