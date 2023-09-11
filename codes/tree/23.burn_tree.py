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
    def burn_tree(self, root, target):
        '''This function takes postorder and inorder array and construct a tree out of it'''
        from collections import deque
        parent = {}
        def create_parent(root, target):
            q = deque([root])
            parent[root] = None
            res = None
            while q:
                node = q.popleft()
                if node.val == target:
                    res = node
                if node.left:
                    q.append(node.left)
                    parent[node.left] = node
                if node.right:
                    q.append(node.right)
                    parent[node.right] = node
            return res
        
        def burn(node):
            vis = set()
            vis.add(node)
            q = deque([node])
            time = 0
            flag = 0
            while q:
                for _ in range(len(q)):
                    res = q.popleft()
                    if res.left and res.left not in vis:
                        vis.add(res.left)
                        q.append(res.left)
                        flag = 1
                    if res.right and res.right not in vis:
                        vis.add(res.right)
                        q.append(res.right)
                        flag = 1
                    if parent[res] and parent[res] not in vis:
                        vis.add(parent[res])
                        q.append(parent[res])
                        flag = 1
                if flag: time += 1
                flag = 0
            return time
        
        node = create_parent(root, target)
        time = burn(node)
        return time
    
obj = Solution()
ans = obj.burn_tree(root, 5)
print(ans)