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
    def successor_predecessor(self, root, k):
        '''This function takes root node and returns successor and predecessor'''
        pred = -1
        succ = -1
        node = root
        while node:
            if node.val > k:
                succ = node.val
                node = node.left
            elif node.val < k:
                pred = node.val
                node = node.right
            else:
                break
        left, right = node.right, node.left
        while left:
            succ = left.val
            left = left.left
        while right:
            pred = right.val
            right = right.right
        return [pred, succ]
    
obj = Solution()
ans = obj.successor_predecessor(root, 3)
print(ans)