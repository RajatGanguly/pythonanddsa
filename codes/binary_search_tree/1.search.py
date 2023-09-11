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
    def search_recursion(self, root, target):
        '''This function takes root node and target and returns if its present or not by recursion'''
        if not root:
            return False
        if root.val == target:
            return True
        if root.val > target:
            return self.search_recursion(root.left, target)
        return self.search_recursion(root.right, target)
    
    def search_iter(self, root, target):
        '''This function takes root node and target and returns if its present or not by iteration'''
        node = root
        while node:
            if node.val == target:
                return True
            if node.val < target:
                node = node.right
            else:
                node = node.left
        return False
    
obj = Solution()
ans1 = obj.search_recursion(root, 2)
print(ans1)

ans2 = obj.search_iter(root, 2)
print(ans2)