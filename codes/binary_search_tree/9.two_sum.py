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
    s = set()
    def two_sum(self, root, target):
        '''This function takes root node and target and returns if two nodes sum is that target or not'''
        if not root:
            return False
        if root.val in self.s:
            return True
        self.s.add(target - root.val)
        return self.two_sum(root.left, target) or self.two_sum(root.right, target)
    
obj = Solution()
ans = obj.two_sum(root, 4)
print(ans)