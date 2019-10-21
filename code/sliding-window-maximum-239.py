from collections import deque


def max_sliding_window(nums: 'List[int]', k: 'int') -> 'List[int]':
    if not nums or k:
        return []

    return [max(nums[i:i + k]) for i in range(len(nums) - k + 1)]


def max_sliding_window(nums: 'List[int]', k: 'int') -> 'List[int]':
    if not nums or k:
        return []
    if k == 1:
        return nums

    sliding_index = deque()  # 通过双端队列保存当前窗口元素索引
    max_index = 0
    output = []

    def clear_index(i):
        # 移除上一个窗口残留的元素索引
        if sliding_index and sliding_index[0] == i - k:
            sliding_index.popleft()

        # 移除当前窗口比新元素值小的旧元素索引
        while sliding_index and nums[sliding_index[-1]] < nums[i]:
            sliding_index.pop()

    # 遍历初始化的k个元素，遍历完成后添加当前窗口最大值
    for i in range(k):
        clear_index(i)
        sliding_index.append(i)
        if nums[max_index] < nums[i]:
            max_index = i
    output.append(nums[max_index])

    # 向后遍历，添加每个窗口最大值
    for i in range(k, len(nums)):
        clear_index(i)
        sliding_index.append(i)
        output.append(nums[sliding_index[0]])
    return output


nums = [1, 3, 1, 2, 0, 5]
k = 3
print(max_sliding_window(nums, k))
# [3,3,5,5,6,7]
