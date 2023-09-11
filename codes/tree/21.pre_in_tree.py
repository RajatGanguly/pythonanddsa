class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
in_order = [7, 3, 11, 1, 17, 3, 18]
pre_order = [1, 3, 7, 11, 3, 17, 18]

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def pre_in_tree(self, in_order, pre_order):
        '''This function takes preorder and inorder array and construct a tree out of it'''
        ind = 0
        n = len(pre_order)

        def find(element, start, end):
            for i in range(start, end+1):
                if in_order[i] == element:
                    return i
            return -1

        def build(start, end):
            print(start, end)
            nonlocal ind
            if ind >= n or start > end:
                return None
            element = pre_order[ind]
            ind += 1
            pos = find(element, start, end)
            root = Node(element)
            root.left = build(start, pos-1)
            root.right = build(pos+1, end)
            return root
        
        root = build(0, n-1)
        return root
    
    def preorder(self, root):
        if not root:
            return
        print(root.val, end = "\t")
        self.inorder(root.left)
        self.inorder(root.right)
    
obj = Solution()
root = obj.pre_in_tree(in_order, pre_order)
obj.preorder(root)