# Check if there is any cycle in directed graph or not
graph = [[1], [2], [3], [0,3]]

class Solution:
    def bfs_dir_cycle(self, graph):
        '''This function takes an adjacency list and return if there is any cycle or not'''
        from collections import deque
        n = len(graph)
        in_degree = [0] * n #this will store the indegree of each node from 0 to n-1
        topo_count = 0
        for i in graph:
            for j in i:
                in_degree[j] += 1
        q = deque([])
        for i in range(n):
            if in_degree[i] == 0:
                q.append(i)
        while q:
            node = q.popleft()
            topo_count += 1
            for v in graph[node]:
                in_degree[v] -= 1
                if in_degree[v] == 0:
                    q.append(v)
        return "Cycle" if topo_count != n else "No Cycle"
    
obj = Solution()
ans = obj.bfs_dir_cycle(graph)
print(ans)