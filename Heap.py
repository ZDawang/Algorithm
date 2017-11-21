
import matplotlib.pyplot as plt

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def show(self, figname = "1"):
        #画图使用annotate，这个函数的主要作用是箭头指示来表示注释用的。
        #参数解释
        #第一个参数：箭头提示显示的内容
        #xy：箭头提示，箭头指向的地方
        #xytext：显示内容的地方，文本位置
        def plotNode(ax, nodeTxt, centerPos, parentPos):
            ax.annotate(nodeTxt, xy = parentPos, xytext = centerPos, arrowprops= dict(arrowstyle = "<-"))

        #寻找树的深度
        def getTreeDepth(root):
            if not root: return 0
            return max(getTreeDepth(root.left), getTreeDepth(root.right)) + 1

        #使用plotTree.xoff, plotTree.yoff做函数的全局变量，记录当前节点的位置。
        def plotTree(ax, root, curpos, level):
            if root.left:
                #每一层之间的高度差不变，都是1.0/plotTree.totalD，第n层之间的节点之间的距离为1.0/2**level, curpos[1]
                leftpos = (curpos[0] - 0.5/2**level, curpos[1] - 1.0/plotTree.totalD)
                plotNode(ax, root.left.val, leftpos, curpos)
                plotTree(ax, root.left, leftpos, level + 1)
            if root.right:
                rightpos = (curpos[0] + 0.5/2**level, curpos[1] - 1.0/plotTree.totalD)
                plotNode(ax, root.right.val, rightpos, curpos)
                plotTree(ax, root.right, rightpos, level + 1)

        if not self: return
        fig = plt.figure(figname)
        ax = fig.add_subplot(111)
        plotTree.totalD = float(getTreeDepth(self))
        ax.annotate(self.val, xy = (0.5, 0.9), xytext = (0.5, 0.9))
        plotTree(ax, self, (0.5, 0.9), 1)
        fig.show()


class Heap(object):
    def __init__(self, l):
        self.nums = l[:]

    #筛选操作与上浮操作为堆的构建方法
    #筛选操作，i为当前节点的下标，l为最后一个叶节点的下标。也就是树总共的节点个数
    def sift(self, nums, i, l):
        j = 2 * i
        while(j <= l):
            #选择左右节点中较小的值
            if j < l and nums[j] > nums[j + 1]:
                j += 1
            #如果父节点的值小于左右节点的值，说明子树为堆，则返回
            if nums[i] < nums[j]:
                return
            nums[i], nums[j] = nums[j], nums[i]
            #转子节点
            i, j = j, 2 * j
        return

    #上浮操作
    def floatUp(self, nums, i):
        #j为父节点下标
        j = i // 2
        while(j >= 1):
            #如果父节点的值较大，则交换
            if nums[j] > nums[i]:
                nums[i], nums[j] = nums[j], nums[i]
            else:
                return
            i, j = j, j // 2
        return

    #构建堆
    def HeapSort(self):
        l = len(self.nums)
        #从最后一个非叶子节点开始，逐个向上筛选，得到小根堆
        for i in range(l//2, 0, -1):
            #由于下标为0处没有存放，所以总节点个数为l-1
            self.sift(self.nums, i, l - 1)

    #删除操作，弹出最小值
    def pop(self):
        l = len(self.nums)
        if l == 1: return
        minnum = self.nums[1]
        #将最后一个叶节点拿到根节点，删除最后一个叶节点
        self.nums[1], self.nums[-1] = self.nums[-1], self.nums[1]
        self.nums.pop()
        #将叶节点进行sift操作
        self.sift(self.nums, 1, l - 2)
        #输出根节点的值
        return minnum

    #插入操作
    def insert(self, x):
        #新建叶节点
        self.nums.append(x)
        #将叶节点的值上浮
        self.floatUp(self.nums, len(self.nums) - 1)

    #将堆画出来
    #构建树
    def GenerateTree(self, nums):
        def CreateTree(tree, nums, i):
            if i >= len(nums) // 2:
                return
            if nums[2 * i] != 0:
                tree.left = TreeNode(nums[2 * i])
                CreateTree(tree.left, nums, 2*i)
            if nums[2 * i + 1] != 0:
                tree.right = TreeNode(nums[2 * i + 1])
                CreateTree(tree.right, nums, 2*i + 1)
        l = len(nums)
        pownum = 1
        while (l > pownum):
            pownum *= 2
        nums = nums + [0] * (pownum - l)
        root = TreeNode(nums[1])
        CreateTree(root, nums, 1)
        return root

    #画出来
    def show(self):
        root = self.GenerateTree(self.nums)
        root.show()


#0代表没有节点，数组第一个字符为0，数组的长度必须为2**n - 1



nums = [0, 49, 38, 65, 97, 76, 13, 27, 49]

Heap1 = Heap(nums)
Heap1.HeapSort()


print(Heap1.nums)

