# Disjoint Set is a data structure

class DisjointSet:
    def __init__(self, n):
        self.rank = [0 for _ in range(n)]
        self.parent = [i for i in range(n)]

    def find_parent(self, node):
        if node == self.parent[node]:
            return node
        self.parent[node] = self.find_parent(self.parent[node])
        return self.parent[node]

    def union(self, u, v):
        u = self.find_parent(u)
        v = self.find_parent(v)
        if self.rank[u] < self.rank[v]:
            self.parent[u] = v
        elif self.rank[v] < self.rank[u]:
            self.parent[v] = u
        else:
            self.parent[v] = u
            self.rank[u] += 1

n = 7
obj = DisjointSet(n)
obj.union(0,1)
obj.union(1,2)
obj.union(3,4)
obj.union(5,6)
obj.union(4,5)
obj.union(2,6)
for i in range(n):
    print(f"Parent of {i} is: {obj.find_parent(i)} and rank is: {obj.rank[i]}")