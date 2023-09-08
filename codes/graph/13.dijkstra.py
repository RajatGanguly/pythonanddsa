# Dijkstra's algo uses heap data structure to get the minimum distance connected with each node
# It is also BFS 
graph = [[[1, 1], [2, 6]], [[2, 3], [0, 1]], [[1, 3], [0, 6]]]

class Solution:
    def dijkstra(self, graph, src):
        '''This algorithm is used to find the shortes distance from a source node to other nodes of undirected weighted graph'''
        import heapq
        n = len(graph)
        dis = [float('inf')] * n
        heap = [[0, src]]
        dis[src] = 0
        while heap:
            distance, node = heapq.heappop(heap)
            for v, w in graph[node]:
                if dis[v] > dis[node] + w:
                    dis[v] = dis[node] + w
                    heapq.heappush(heap, [dis[v], v])
        return dis
    
obj = Solution()
ans = obj.dijkstra(graph, 0)
print(ans)