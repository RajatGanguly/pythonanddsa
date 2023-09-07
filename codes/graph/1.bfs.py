# This is an undirected unweighted graph and here we will use BFS algorith to traverse the graph
graph = [[1,2], [0,4], [0,3,4,5], [2,5], [1,2], [2,3], [7], [6]]

'''
    The above decleared graph is depected below
        0    3
      /   \ /  \    6
     1     2 - 5     \
      \   /           7
        4   
'''

class Solution:
    def bfs_traversal(self, graph):
        '''This function takes an adjacency list and return an array of BFS Traversal'''
        from collections import deque
        n = len(graph)
        ans = []
        visited = [False]*n #creating a visited array to track if a node is visited or not

        def bfs(node):
            q = deque([node])
            while q:
                vertex = q.popleft()
                ans.append(vertex)
                for v in graph[vertex]:
                    if not visited[v]:
                        q.append(v)
                        visited[v] = True

        for i in range(n):
            # checking nodes are visited or not
            # this checking is important for graph with multiple component
            if not visited[i]:
                visited[i] = True
                bfs(i)
        return ans
    
obj = Solution()
ans = obj.bfs_traversal(graph)
print(ans)

# Notes:    This algorithm can also be used in counting components in a graph
# by incrementing a variable each time the loop got one element with visited[i] == True