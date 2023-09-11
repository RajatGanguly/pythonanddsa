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
    def kth_smallest(self, root, k):
        '''This function takes root node and returns k th smallest element'''
        ans = -1
        def find(root):
            nonlocal k, ans
            if root:
                find(root.right)
                k -= 1
                if k == 0:
                    ans = root.val
                find(root.left)
        find(root)
        return ans
    
obj = Solution()
ans = obj.kth_smallest(root, 3)
print(ans)