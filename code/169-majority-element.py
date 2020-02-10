import collections
import random


def majority_element(nums):
    majority_count = len(nums) // 2
    for num in nums:
        count = sum(1 for elem in nums if elem == num)
        if count > majority_count:
            return num


def majority_element(nums):
    majority_count = len(nums) // 2
    map = {}
    for i in nums:
        map.update({i: map.get(i, 0) + 1})
        if map.get(i) > majority_count:
            return i


def majority_element(nums):
    nums.sort()
    return nums[len(nums) // 2]


def majority_element(nums):
    def majority_element_rec(low, high):
        # 当元素个数为1,该元素即为众数
        if low == high:
            return nums[low]

        # 将数组切为两段,分别递归计算每段的众数
        mid = (high - low) // 2 + low
        left = majority_element_rec(low, mid)
        right = majority_element_rec(mid + 1, high)

        # 当左右两段的众数相同,返回众数
        if left == right:
            return left

        # 当左右两段众数不同,分别计算两个众数出现次数
        left_count = sum(1 for i in range(low, high + 1) if nums[i] == left)
        right_count = sum(1 for i in range(low, high + 1) if nums[i] == right)
        # 若左段众数较大,则返回左段众数,否则返回右段众数
        return left if left_count > right_count else right

    return majority_element_rec(0, len(nums) - 1)


def majority_element(nums):
    num = None
    count = 0
    for i in nums:
        if count == 0:
            num = i
        count += 1 if i == num else -1
    return num


print(majority_element([1, 1, 2, 2, 2, 2, 3]))
