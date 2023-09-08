class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

# Constructing a tree manually

'''
                    1
                   / \
                  2   3
                 / \
                4   5
'''
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

class Solution:
    def check_balanced_brutforce(self, root):
        '''This function takes root node and returns the tree is balanced or not'''
        def height(root):
            return max(height(root.left), height(root.right)) + 1 if root else 0
        
        def is_balanced(root):
            if not root:
                return True
            left_height = height(root.left)
            right_height = height(root.right)
            return is_balanced(root.left) and is_balanced(root.right) and abs(left_height - right_height) <= 1
        
        return is_balanced(root)
    
    def check_balanced_optimized(self, root):
        '''This function takes root node and returns the tree is balanced or not'''
        if not root:
            return [True, 0]
        left = self.check_balanced_optimized(root.left)
        right = self.check_balanced_optimized(root.right)
        height = max(left[1], right[1]) + 1
        return [left[0] and right[0] and abs(left[1] - right[1]) <= 1, height]
    
obj = Solution()
ans1 = obj.check_balanced_brutforce(root)
print(ans1)

ans2 = obj.check_balanced_optimized(root)
print(ans2[0])