class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

# Constructing a bst manually

'''
                    4
                   / \
                  2   6
                 / \
                1   3
'''
root = Node(4)
root.left = Node(2)
root.right = Node(6)
root.left.left = Node(1)
root.left.right = Node(3)

class Solution:
    def insert_recursion(self, root, item):
        '''This function takes root node and item and insert it in a bst by recursion'''
        if not root:
            return Node(item)
        if root.val > item:
            root.left =  self.insert_recursion(root.left, item)
        else:
            root.right = self.insert_recursion(root.right, item)
        return root
    
    def insert_iter(self, root, target):
        '''This function takes root node and target and insert it in a bst by iteration'''
        node = root
        cur = None
        if not root:
            return Node(target)
        while node:
            cur = node
            if node.val < target:
                node = node.right
            elif node.val > target:
                node = node.left
            else:
                break
        if cur.val > target:
            cur.left = Node(target)
        elif cur.val < target:
            cur.right = Node(target)
    
    def preorder(self, root):
        if root:
            print(root.val, end="\t")
            self.preorder(root.left)
            self.preorder(root.right)
    
obj = Solution()
obj.insert_recursion(root, 5)
obj.preorder(root)

print("\n")

obj.insert_iter(root, 7)
obj.preorder(root)