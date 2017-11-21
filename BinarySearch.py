
#二分法的写法总结

#找到target的下标
def BinarySearch1(nums, target):
    l, r = 0, len(nums) - 1
    while l < r:
        m = (l + r)//2
        #右区间满足且m不满足
        if nums[m] < target:
            l = m + 1
        #左区间满足且m也满足
        else:
            r = m
    return l


def BinarySearch2(nums, target):
    l, r = 0, len(nums) - 1
    while l < r - 1:                       #循环逻辑
        m = (l + r)//2
        #右区间满足且m不满足
        if nums[m] > target:                      #判断逻辑
            r = m - 1                         #l或者r的变换规则
        #左区间满足且m也满足
        else:
            l = m                  #l或者r的变换规则

    #结果判断
    return l if nums[l] == target else r


nums = [1,2,5,7,8,11,15,18,19,55,467,888]

print(BinarySearch2(nums, 3))