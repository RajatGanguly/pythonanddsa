# This is an undirected unweighted graph and here we will use DFS algorith to check if the graph is Bipartite or not
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
    def bipartite_dfs(self, graph):
        '''This function takes an adjacency list and return if the graph is Bipartite or not'''
        n = len(graph)
        color = [-1]*n #creating a color array to track if a node is visited or not

        def dfs(node, parent = -1):
            if color[node] == -1:
                color[node] = 0
            for v in graph[node]:
                if color[v] == -1:
                    color[v] = color[node] ^ 1 # As we know 1^0 = 1 and 1^1 = 0 so color of v will be opposite of node
                    if not dfs(v):
                        return False
                elif color[v] == color[node]:
                    return False
            return True

        for i in range(n):
            # checking nodes are visited or not
            # this checking is important for graph with multiple component
            if color[i] == -1:
                if not dfs(i):
                    return "Not Bipartite"
        return "Bipartite"
    
obj = Solution()
ans = obj.bipartite_dfs(graph)
print(ans)