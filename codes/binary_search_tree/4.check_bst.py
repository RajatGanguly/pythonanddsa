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
    def check_bst(self, root, mn, mx):
        '''This function takes root node and returns if its a bst or not'''
        if not root:
            return True
        if root.val < mn or root.val > mx:
            return False
        return self.check_bst(root.left, mn, root.val-1) and self.check_bst(root.right, root.val+1, mx)
    
obj = Solution()
ans = obj.check_bst(root, -float('inf'), float('inf'))
print(ans)