class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

# Constructing a bst manually

'''
                    4
                   / \
                  2   5
                 / \
                1   3
'''
root = Node(4)
root.left = Node(2)
root.right = Node(5)
root.left.left = Node(1)
root.left.right = Node(3)

class Solution:
    def delete(self, root, target):
        '''This function takes root node and target and remove it from the tree'''
        if not root:
            return None
        if root.val > target:
            root.left = self.delete(root.left, target)
        elif root.val < target:
            root.right = self.delete(root.right, target)
        else:
            if not root.left:
                root = root.right
            elif not root.right:
                root = root.left
            else:
                mn = self.minimum(root.right)
                root.val = mn
                root.right = self.delete(root.right, mn)
        return root

    def minimum(self, root):
        while root:
            res = root.val
            root = root.left
        return res

    def preorder(self, root):
        if root:
            print(root.val, end="\t")
            self.preorder(root.left)
            self.preorder(root.right)
    
obj = Solution()
root = obj.delete(root, 2)
obj.preorder(root)