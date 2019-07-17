def two_sum(nums, target):
    d = {}
    for i, num in enumerate(nums):
        if target - num in d:
            return [d[target - num], i]
        d[num] = i
    return []


def two_sum(nums, target):
    for i in range(0, len(nums) - 1):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []


def two_sum(nums, target):
    d = {}
    for i in range(0, len(nums)):
        d[nums[i]] = i
    for i, num in enumerate(nums):
        if target - num in d:
            return [d[target - num], i]


nums_input = [2, 3, 4, 7]
target_input = 9
print(two_sum(nums_input, target_input))
