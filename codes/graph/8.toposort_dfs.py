# Topological sort are applicable only on DAG(Directed Acyclic Graph)
graph = [[], [0], [0], [0]]

class Solution:
    def bfs_topo_sort(self, graph):
        '''This function takes an adjacency list and return an array topologically sorted by DFS'''
        n = len(graph)
        visited = [False] * n
        stack = []

        def dfs(node):
            visited[node] = True
            for v in graph[node]:
                if not visited[v]:
                    dfs(v)
            stack.append(node)

        for i in range(n):
            if not visited[i]:
                dfs(i)
        return stack[::-1]
    
obj = Solution()
ans = obj.bfs_topo_sort(graph)
print(ans)