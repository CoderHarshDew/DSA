class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        seen = set()
        response = False

        for num in nums:
            if num in seen:
                response = True
                break
            seen.add(num)
        return response

# Solution Quick Note
# Use set  to keep track of seen number, if seen twice return True else False.