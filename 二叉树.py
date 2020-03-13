# 二叉树类
class BTree():
    def __init__(self, value=None, left=None, right=None):  #初始化，直接用节点数据定义
        self.value = value    # 数据域
        self.left = left    # 左子树
        self.right = right  # 右子树


    # 前序遍历
    def preorder(self):
        if self.value is not None:
            print(self.value, end=' ')
        if self.left is not None:
            self.left.preorder()
        if self.right is not None:
            self.right.preorder()

    # 中序遍历
    def inorder(self):
        if self.left is not None:
            self.left.inorder()
        if self.value is not None:
            print(self.value, end=' ')
        if self.right is not None:
            self.right.inorder()

    # 后序遍历
    def postorder(self):

        if self.left is not None:
            self.left.postorder()
        if self.right is not None:
            self.right.postorder()
        if self.value is not None:
            print(self.value, end=' ')

    # 层序遍历
    def levelorder(self):
        # 返回某个节点的左孩子
        def LChild_Of_Node(node):
            return node.left if node.left is not None else None
        # 返回某个节点的右孩子
        def RChild_Of_Node(node):
            return node.right if node.right is not None else None

        # 层序遍历列表
        level_order = []
        # 是否添加根节点中的数据
        if self.value is not None:
            level_order.append([self])

        # 二叉树的高度
        height = self.height()
        if height >= 1:
            # 对第二层及其以后的层数进行操作, 在level_order中添加节点而不是数据
            for _ in range(2, height + 1):
                level = []  # 该层的节点
                for node in level_order[-1]:
                    # 如果左孩子非空，则添加左孩子
                    if LChild_Of_Node(node):
                        level.append(LChild_Of_Node(node))
                    # 如果右孩子非空，则添加右孩子
                    if RChild_Of_Node(node):
                        level.append(RChild_Of_Node(node))
                # 如果该层非空，则添加该层
                if level:
                    level_order.append(level)

            # 取出每层中的数据
            for i in range(0, height):  # 层数
                for index in range(len(level_order[i])):
                    level_order[i][index] = level_order[i][index].value

        return level_order

    # 二叉树的高度
    def height(self):
        # 空的树高度为0, 只有root节点的树高度为1
        if self.value is None:
            return 0
        elif self.left is None and self.right is None:
            return 1
        elif self.left is None and self.right is not None:
            return 1 + self.right.height()
        elif self.left is not None and self.right is None:
            return 1 + self.left.height()
        else:
            return 1 + max(self.left.height(), self.right.height())

    # 二叉树的叶子节点
    def leaves(self):

        if self.value is None:
            return None
        elif self.left is None and self.right is None:
            print(self.value, end=' ')
        elif self.left is None and self.right is not None:
            self.right.leaves()
        elif self.right is None and self.left is not None:
            self.left.leaves()
        else:
            self.left.leaves()
            self.right.leaves()

'''
# 构造二叉树, BOTTOM-UP METHOD
right_tree = BTree(6)
right_tree.left = BTree(2)
right_tree.right = BTree(4)

left_tree = BTree(5)
left_tree.left = BTree(1)
left_tree.right = BTree(3)

tree = BTree(11)
tree.left = left_tree
tree.right = right_tree

left_tree = BTree(7)
left_tree.left = BTree(3)
left_tree.right = BTree(4)

right_tree = tree # 增加新的变量
tree = BTree(18)
tree.left = left_tree
tree.right = right_tree
'''
tree=BTree(18,BTree(7,BTree(3),BTree(4)),BTree(11,BTree(5,BTree(1),BTree(3)),BTree(6,BTree(2),BTree(4))))

print('先序遍历为:')
tree.preorder()
print()

print('中序遍历为:')
tree.inorder()
print()

print('后序遍历为:')
tree.postorder()
print()

print('层序遍历为:')
level_order = tree.levelorder()
print(level_order)
print()

height = tree.height()
print('树的高度为%s.' % height)

print('叶子节点为：')
tree.leaves()
print()