# Kruskal's algorithm uses disjoint set data structure to eliminate loops and returns the minimum Spanning Tree

graph = [[[1,5], [2,1]], [[0,5], [2,3]], [[0,1], [1,3]]]

class Solution:
    def prim_algorithm(self, graph):
        '''Kruskal's algorithm is used to get the minimum spanning tree out of a weighted undirected graph'''
        n = len(graph)
        g = []
        for i in range(len(graph)):
            for j in graph[i]:
                g.append([j[1], j[0], i])
        g.sort()
        mst = set()
        rank = [0] * n
        parent = [i for i in range(n)]
        
        def find_parent(node):
            if node == parent[node]:
                return node
            parent[node] = find_parent(parent[node])
            return parent[node]
        
        def union(u, v):
            u = find_parent(u)
            v = find_parent(v)
            if rank[u] < rank[v]:
                parent[u] = v
            elif rank[v] < rank[u]:
                parent[v] = u
            else:
                parent[v] = u
                rank[u] += 1
        
        cost = 0
        for i in g:
            if find_parent(i[1]) != find_parent(i[2]):
                cost += i[0]
                mst.add(i[1])
                mst.add(i[2])
                union(i[1], i[2])
        return f"Cost of MST is: {cost}"
    
obj = Solution()
ans = obj.prim_algorithm(graph)
print(ans)