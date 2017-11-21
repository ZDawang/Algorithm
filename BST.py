
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
        ax.clear()
        plotTree.totalD = float(getTreeDepth(self))
        ax.annotate(self.val, xy = (0.5, 0.9), xytext = (0.5, 0.9))
        plotTree(ax, self, (0.5, 0.9), 1)
        fig.show()






class BST(object):
    def __init__(self):
        self.root = None

    #构建树
    def GenerateTree(self, nums):
        def CreateTree(tree, nums, i, l):
            if i > l // 2:
                return
            if 2 * i <= l and nums[2 * i] != 0:
                tree.left = TreeNode(nums[2 * i])
                CreateTree(tree.left, nums, 2*i, l)
            if 2 * i + 1 <= l and nums[2 * i + 1] != 0:
                tree.right = TreeNode(nums[2 * i + 1])
                CreateTree(tree.right, nums, 2*i + 1, l)
        l = len(nums)
        root = TreeNode(nums[1])
        CreateTree(root, nums, 1, l - 1)
        return root
    
    #初始化一个BST
    def BSTinit(self, nums):
        self.root = self.GenerateTree(nums)

    #得到第k个元素
    def GetKmin(self, k):
        stack = []
        node = self.root
        count = 0
        while node or stack:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            count += 1
            if count == k:
                return node.val
            node = node.right
        return -1





    #寻找除当前值外的最小值
    def findminnum(self, root):
        minnum = root.val
        while root.left:
            root = root.left
            minnum = root.val
        return minnum

    #删除一个元素
    def delete(self, x):
        def deleteHelp(root, key):
            if root == None: return None
            if root.val > key:
                root.left = deleteHelp(root.left, key)
            elif root.val < key:
                root.right = deleteHelp(root.right, key)
            else:
                if not root.right: return root.left
                if not root.left: return root.right
                root.val = self.findminnum(root.right)
                root.right = deleteHelp(root.right, root.val)
            return root
        self.root = deleteHelp(self.root, x)

    #插入一个元素
    def insert(self, x):
        def insertHelp(root, x):
            if not root:
                root = TreeNode(x)
                return root
            if x >= root.val:
                root.right = insertHelp(root.right, x)
            else:
                root.left = insertHelp(root.left, x)
            return root
        self.root = insertHelp(self.root, x)


    def show(self):
        if self.root:
            self.root.show()





nums = [0, 15, 10, 29, 5, 12, 0, 38, 1, 0, 11, 0, 0, 0, 0, 40]

BST1 = BST()
BST1.BSTinit(nums)
BST1.show()

