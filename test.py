def getConcatenation(nums: list[int]) -> list[int]:
    ans = nums.copy()

    for n in nums:
        ans.append(n)
    return ans


print(getConcatenation([1,2,3]))
