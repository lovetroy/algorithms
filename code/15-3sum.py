def three_sum(nums):
    if len(nums) < 3:
        return []
    nums.sort()
    res = set()
    for i in range(0, len(nums) - 2):
        for j in range(i + 1, len(nums) - 1):
            for x in range(j + 1, len(nums)):
                if nums[i] + nums[j] + nums[x] == 0:
                    res.add((nums[i], nums[j], nums[x]))
    return list(map(list, res))


def three_sum(nums):
    if len(nums) < 3:
        return []
    nums.sort()
    res = set()
    for i, v in enumerate(nums[:-2]):
        if i > 0 and v == nums[i - 1]:
            continue
        d = {}
        for x in nums[i + 1:]:
            if -v - x in d:
                res.add((v, x, -v - x))
            else:
                d[x] = 1
    return list(map(list, res))


def three_sum(nums):
    if len(nums) < 3:
        return []
    nums.sort()
    res = []
    for i in range(0, len(nums) - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        l, r = i + 1, len(nums) - 1
        while l < r:
            sum = nums[i] + nums[l] + nums[r]
            if sum > 0:
                r -= 1
            elif sum < 0:
                l += 1
            else:
                res.append((nums[i], nums[l], nums[r]))
                while l < r and nums[l] == nums[l + 1]:
                    l += 1
                while l < r and nums[r] == nums[r - 1]:
                    r -= 1
                l += 1
                r -= 1
    return res


nums = [-1, 0, 1, -1, 0, 1, -1, 0, 1, -1, 0, 1, ]
print(three_sum(nums))
