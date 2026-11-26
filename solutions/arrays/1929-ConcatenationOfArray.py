class Solution:
    def getConcatenation(self, nums: list[int]) -> list[int]:
        ans = nums.copy()

        for n in nums:
            ans.append(n)

        return ans

# Create a copy of nums (shallow) and append the elements of num to it.
# But this works only in python, as python lists can be resized, and copy exists
# in python.