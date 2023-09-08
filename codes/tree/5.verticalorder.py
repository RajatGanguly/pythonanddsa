class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

# Constructing a tree manually

'''
horizontal    -2 -1 0 1
distance :          1
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
        '''This function takes root node and returns an array of vertical order traversal'''
        from collections import defaultdict
        d = defaultdict(lambda: defaultdict(list))
        ans = []
        def f(root, hd, level):
            if not root:
                return
            d[hd][level] = root.val
            f(root.left, hd-1, level+1)
            f(root.right, hd+1, level+1)
        f(root, 0, 0)
        min_hd, max_hd = min(d.keys()), max(d.keys())
        for hd in range(min_hd, max_hd+1):
            levels = sorted(d[hd].keys())
            for level in levels:
                ans.append(d[hd][level])
        return ans
    
obj = Solution()
ans = obj.level_order(root)
print(ans)