

#直接插入排序
def DirectInserteSort(nums):
    l = len(nums)
    tmp = nums[0]
    for i in range(1, l):
        #若大于，则不用排序
        if nums[i] < nums[i - 1]:
            #将当前元素暂存
            tmp = nums[i]
            for j in range(i - 1, -2, -1):
                #若找到相应的位置，即比当前值小的元素。或者没找到元素时,即当前tmp为最小值
                if j < 0 or nums[j] <= tmp:
                    break
                #后移数组
                nums[j + 1] = nums[j]
            #插入
            nums[j + 1] = tmp
    return

#希尔排序
def ShellInsertSort(nums):
    l = len(nums)
    d = l // 2
    while(d >= 1):
        #0到d-1为初始序列，也就是d个长度为1的有序序列
        for i in range(d, l):
            #做直接插入排序
            if nums[i] < nums[i - d]:
                tmp = nums[i]
                for j in range(i - d, -d - 1, -d):
                    if j < 0 or nums[j] <= tmp:
                        break
                    nums[j + d] = nums[j]
                nums[j + d] = tmp
        d = d // 2
    return

#冒泡排序
def BubbleSort(nums):
    l = len(nums)
    #i为无序区最后一个元素
    for i in range(l - 1, -1, -1):
        #对无序区进行相邻元素比较
        for j in range(i):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
    return

#改进的冒泡排序
def ImproveBubbleSort(nums):
    #i为无序区最后一个元素
    i = len(nums) - 1
    while(i >= 0):
        #交换的位置
        pos = -1
        for j in range(i):
            if nums[j] > nums[j + 1]:
                pos = j
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
        i = pos
    return

#快速排序
def QuickSort(nums):
    #分区函数
    #i,j为区域范围,这里将第一个元素作为轴值
    def Partion(nums, i, j):
        pivot = nums[i]
        while(i < j):
            #右侧扫描，交换后轴值下标变为j
            while i < j and nums[j] >= pivot:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]
            #左侧扫描，交换后轴值下标重新变为i
            while i < j and nums[i] <= pivot:
                i += 1
            nums[i], nums[j] = nums[j], nums[i]
        return i
    
    #改进分区函数
    #因为交换操作不是必须的，轴值放在那里就可以了
    def Partion2(nums, i, j):
        pivot = nums[i]
        while(i < j):
            #右侧扫描，将较小值放到i处
            while i < j and nums[j] >= pivot:
                j -= 1
            nums[i] = nums[j]
            #左侧扫描，将较大值放到j处
            while i < j and nums[i] <= pivot:
                i += 1
            nums[j] = nums[i]
        nums[i] = pivot
        return i

    #递归分区，直到分区中只有一个函数
    def dfs(nums, i, j):
        if i < j:
            pivotloc = Partion(nums, i, j)
            dfs(nums, i, pivotloc - 1)
            dfs(nums, pivotloc + 1, j)

    dfs(nums, 0, len(nums) - 1)
    return

#简单选择排序
def SelectSort(nums):
    l = len(nums)
    for i in range(l):
        index = i
        #寻找最小值
        for j in range(i + 1, l):
            if nums[j] < nums[index]:
                index = j
        #交换
        if i != index:
            nums[i], nums[index] = nums[index], nums[i]
    return 

#堆排序
def HeapSort(nums):
    #筛选(下沉)操作,大根堆
    def sift(nums, i, l):
        #从下标0开始，所以左孩子位置为2*i+1，右孩子为2*i+2
        j = 2*i + 1
        while(j <= l):
            #选子节点中最大值
            if j < l and nums[j] < nums[j + 1]:
                j += 1
            #比较
            if nums[i] >= nums[j]:
                break
            #交换
            nums[i], nums[j] = nums[j], nums[i]
            i, j = j, 2*j + 1
        return

    l = len(nums)
    #构建堆
    for i in range(l//2, -1, -1):
        sift(nums, i, l - 1)
    #弹出元素
    for i in range(l):
        nums[0], nums[l - 1 - i] = nums[l - 1 - i], nums[0]
        sift(nums, 0, l - i - 2)
    return

#二路合并排序
def MergeSort(nums):
    #将nums1的l-m与m到r合并到nums2的l-r中，nums1的l-m与m到r均已为有序序列
    def merge(nums1, nums2, l, m, r):
        #nums1的两个下标
        i, j = l, m + 1
        #nums2的下标
        k = l
        while i <= m and j <= r:
            #若nums[i]小，则将nums[i]写入nums2
            if nums1[i] < nums1[j]:
                nums2[k] = nums1[i]
                i, k = i + 1, k + 1
            else:
                nums2[k] = nums1[j]
                j, k = j + 1, k + 1
        #若l-m没处理完
        if i <= m:
            while i <= m:
                nums2[k] = nums1[i]
                i, k = i + 1, k + 1
        #若m-r没处理完
        if j <= r:
            while j <= r:
                nums2[k] = nums1[j]
                j, k = j + 1, k + 1
        return

    #h为子序列长度
    def MergeHelper(nums1, nums2, h):
        i, l = 0, len(nums1)
        #将前面可以分成长度为h的子序列进行合并,i为子序列开始的下标
        while i <= l - 1 - 2*h:
            merge(nums1, nums2, i, i + h - 1, i + 2*h - 1)
            i += 2*h
        #剩下最后一个长度小于2*h的子序列
        #若最后一个子序列长度大于h，则分成两个子序列合并,否则直接赋值给nums2
        if i < l - h:
            merge(nums1, nums2, i, i + h - 1, l - 1)
        else:
            merge(nums1, nums2, i, l - 1, l - 1)


    h, l = 1, len(nums)
    #存放中间结果使用
    nums2 = nums[:]
    while h < l:
        MergeHelper(nums, nums2, h)
        h *= 2
        #将nums更新，下次排序使用
        for i in range(l):
            nums[i] = nums2[i]
    return

#二路合并排序递归模式
def MergeSort2(nums):
    #将nums1的l-m与m到r合并到nums2的l-r中，nums1的l-m与m到r均已为有序序列
    def merge(nums1, nums2, l, m, r):
        #nums1的两个下标
        i, j = l, m + 1
        #nums2的下标
        k = l
        while i <= m and j <= r:
            #若nums[i]小，则将nums[i]写入nums2
            if nums1[i] < nums1[j]:
                nums2[k] = nums1[i]
                i, k = i + 1, k + 1
            else:
                nums2[k] = nums1[j]
                j, k = j + 1, k + 1
        #若l-m没处理完
        if i <= m:
            while i <= m:
                nums2[k] = nums1[i]
                i, k = i + 1, k + 1
        #若m-r没处理完
        if j <= r:
            while j <= r:
                nums2[k] = nums1[j]
                j, k = j + 1, k + 1
        return

    def MergeHelper(nums1, nums2, l, r):
        if l == r:
            nums2[l] = nums1[l]
        else:
            m = (l + r) // 2
            #对左边的子序列进行递归合并
            MergeHelper(nums1, nums2, l, m)
            #对右边的子序列进行递归合并
            MergeHelper(nums1, nums2, m + 1, r)
            #对左右子序列进行合并,因为nums2为合并结果，所以作为合并输入，合并结果为nums1
            merge(nums2, nums1, l, m, r)
            #将nums2作为合并结果
            for i in range(len(nums1)):
                nums2[i] = nums1[i]

    nums2 = nums[:]
    MergeHelper(nums2, nums, 0, len(nums) - 1)









nums = [4, 3, 2, 1, 7, 8, 9, 5, 6]
nums2 = [49, 38, 65, 97, 76, 13, 27, 49, 55, 4,2]
