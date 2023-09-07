# Topological sort are applicable only on DAG(Directed Acyclic Graph)
# The below algorithm is also known as KAHN'S Algorithm
graph = [[], [0], [0], [0]]

class Solution:
    def bfs_topo_sort(self, graph):
        '''This function takes an adjacency list and return an array topologically sorted by BFS'''
        from collections import deque
        n = len(graph)
        in_degree = [0] * n #this will store the indegree of each node from 0 to n-1
        ans = []
        for i in graph:
            for j in i:
                in_degree[j] += 1
        q = deque([])
        for i in range(n):
            if in_degree[i] == 0:
                q.append(i)
        while q:
            node = q.popleft()
            ans.append(node)
            for v in graph[node]:
                in_degree[v] -= 1
                if in_degree[v] == 0:
                    q.append(v)
        return ans
    
obj = Solution()
ans = obj.bfs_topo_sort(graph)
print(ans)

# Note: This can also be used if the graph is DAG or not, if not then len(ans) != n