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
    def level_order(self, root):
        '''This function takes root node and returns an array of level order traversal'''
        from collections import deque
        ans = []
        if not root: # If root is none it will return empty array
            return ans
        q = deque([root])
        while q:
            node = q.popleft()
            ans.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        return ans
    
    def level_order_rec(self, root):
        '''This function takes root node and returns an array of level order traversal'''
        from collections import defaultdict
        ans = defaultdict(list)
        if not root: # If root is none it will return empty array
            return ans
        def dfs(node, level):
            if node:
                ans[level].append(node.val)
                dfs(node.left, level+1)
                dfs(node.right, level+1)
        dfs(root, 0)
        return ans
    
obj = Solution()
ans1 = obj.level_order(root)
print(ans1)

ans2 = obj.level_order_rec(root)
print(ans2)