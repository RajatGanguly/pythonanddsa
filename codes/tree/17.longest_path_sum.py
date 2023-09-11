# This problem is also known as LONGEST BLOODLINE PROBLEM
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
                     \
                      6
'''
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.left.right.right = Node(6)

class Solution:
    def topview(self, root):
        '''This function takes root node and returns sum of longest path of the tree'''
        ans = []
        def helper(root, current_sum, current_level, ans):
            if not root:
                return
            if current_level > ans[1]:
                ans[0] = current_sum + root.val
                ans[1] = current_level
            elif current_level == ans[1]:
                ans[0] = max(ans[0], current_sum + root.val)
            helper(root.left, current_sum+root.val, current_level+1, ans)
            helper(root.right, current_sum+root.val, current_level+1, ans)
        ans = [0, 0]
        helper(root, 0, 0, ans)
        return ans[0]
    
obj = Solution()
ans = obj.topview(root)
print(ans)