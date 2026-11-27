
def twoSum(nums: list[int], target: int) -> list[int]:
    d = dict.fromkeys(nums, 0)
    print(d.keys())

    for i in range(len(nums)):
        x = target - nums[i]
        x = -1*x if x < 0 else x
        print(x)

        if x in d:
            print(1)
            for j in range(len(nums)):
                if i == j:

                    continue
                if nums[j] == x:
                    print(2)
                    return [i, j]



print(twoSum([3,2,4], 6))
