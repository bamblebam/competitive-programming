nums = [-1, 0, 1, 2, -1, -4]


def threesum(nums):
    if len(nums) < 3:
        return []
    sums = list()
    for i in range(len(nums)-1):
        s = set()
        for j in range(i+1, len(nums)):
            x = -(nums[i]+nums[j])
            if x in s:
                sums.append([x, nums[i], nums[j]])
            else:
                s.add(nums[j])
    output = list()
    for sum_ in sums:
        sum_.sort()
        if sum_ not in output:
            output.append(sum_)
    return output


print(threesum(nums))
