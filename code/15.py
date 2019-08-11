def three_sum(nums):
    if len(nums) < 3:
        return []
    nums.sort()
    res = set()
    for i in range(0, len(nums) - 2):
        for j in range(i + 1, len(nums)-1):
            for x in range(j+1,len(nums)):
                if nums[i]+nums[j]+nums[x]==0:
                    res.add((nums[i],nums[j],nums[x]))
    return list(map(list, res))


def three_sum(nums):
    if len(nums) < 3:
        return []
    nums.sort()
    res = set()
    for i, v in enumerate(nums[:-2]):
        if i >= 1 and v == nums[i - 1]:
            continue
        d = {}
        for x in nums[i + 1:]:
            if x in d:
                res.add((v, x, -v - x))
            else:
                d[-v - x] = 1
    return list(map(list, res))


# nums=[-1,0,1,2,-1,-4]
# import time
# import resource
# import memory_profiler
#
# def using():
#     usage = resource.getrusage(resource.RUSAGE_SELF)
#     mem = usage[2]*resource.getpagesize() /1000000.0
#     print("mem: ", mem,  " Mb")
#     return mem
#
#
# def mem_scan():
#     before_mem = memory_profiler.memory_usage()
#
#     for i in range(1000000):
#         print(i)
#
#     after_mem = memory_profiler.memory_usage()
#
#     print("Memory (Before): {}Mb".format(before_mem))
#     print("Memory (After): {}Mb".format(after_mem))
#
# before_mem = memory_profiler.memory_usage()
# a=time.time()
nums = [-1, 0, 1, 2, -1, -4]
print(three_sum(nums))
# print(time.time(),a)
# after_mem = memory_profiler.memory_usage()
# print("Memory (Before): {}Mb".format(before_mem))
# print("Memory (After): {}Mb".format(after_mem))
# print(1565563053060- 1565562096107)