# This is an undirected unweighted graph and here we will use BFS algorith to check if the graph is Bipartite or not
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
    def bipartite_bfs(self, graph):
        '''This function takes an adjacency list and return if the graph is Bipartite or not'''
        from collections import deque
        n = len(graph)
        color = [-1]*n #creating a color array to track if a node is visited or not

        def bfs(node):
            q = deque([node])
            color[node] = 0
            while q:
                vertex = q.popleft()
                for v in graph[vertex]:
                    if color[v] == -1:
                        q.append(v)
                        color[v] = 1 - color[vertex] #coloring the node opposite of its previous node
                    elif color[v] == color[vertex]:
                        return False
            return True

        for i in range(n):
            # checking nodes are visited or not
            # this checking is important for graph with multiple component
            if color[i] == -1:
                if not bfs(i):
                    return "Not Bipartite"
        return "Bipartite"
    
obj = Solution()
ans = obj.bipartite_bfs(graph)
print(ans)