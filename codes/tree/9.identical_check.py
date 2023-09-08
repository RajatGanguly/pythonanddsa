class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

# Constructing a tree manually

'''
                    1                                                       1
                   / \                                                     / \
                  2   3                                                   2   3
                 / \                                                     / \
                4   5                                                   4   5
'''
root1 = Node(1)
root1.left = Node(2)
root1.right = Node(3)
root1.left.left = Node(4)
root1.left.right = Node(5)

root2 = Node(1)
root2.left = Node(2)
root2.right = Node(3)
root2.left.left = Node(4)
root2.left.right = Node(5)

class Solution:
    def check_identical(self, root1, root2):
        '''This function takes 2 root nodes of 2 trees and returns if the are identical or not'''
        if not root1 and not root2:
            return True
        if not root1 and root2:
            return False
        if root1 and not root2:
            return False
        if root1.val != root2.val:
            return False
        return self.check_identical(root1.left, root2.left) and self.check_identical(root1.right, root2.right)
    
obj = Solution()
ans = obj.check_identical(root1, root2)
print(ans)