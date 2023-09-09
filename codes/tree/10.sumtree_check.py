class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

# Constructing a tree manually

'''
                   10
                   / \
                  3   4
                 / \
                1   2
'''
root = Node(10)
root.left = Node(3)
root.right = Node(4)
root.left.left = Node(1)
root.left.right = Node(2)

class Solution:
    def check_sumtree_brutforce(self, root):
        '''This function takes root node and returns the tree is sum tree or not'''
        def get_sum(root):
            if not root:
                return 0
            if not root.left and not root.right:
                return root.val
            return get_sum(root.left) + get_sum(root.right) + root.val
        
        def is_sumtree(root):
            if not root:
                return True
            if not root.left and not root.right:
                return True
            left_sum = get_sum(root.left)
            right_sum = get_sum(root.right)
            return is_sumtree(root.left) and is_sumtree(root.right) and left_sum+right_sum == root.val
        
        return is_sumtree(root)
    
    def check_sumtree_optimized(self, root):
        '''This function takes root node and returns the tree is sum tree or not'''
        if not root:
            return [True, 0]
        if not root.left and not root.right:
            return [True, root.val]
        left = self.check_sumtree_optimized(root.left)
        right = self.check_sumtree_optimized(root.right)
        return [left[0] and right[0] and left[1] + right[1] == root.val, left[1] + right[1] + root.val]
    
obj = Solution()
ans1 = obj.check_sumtree_brutforce(root)
print(ans1)

ans2 = obj.check_sumtree_optimized(root)
print(ans2[0])