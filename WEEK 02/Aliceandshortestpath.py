import sys

"""
I searched and found the buggy code
"""
 
INF  = 10000000
MAXN = 5005
n, m = 0, 0
 
adjMatrix = [[INF for x in range(MAXN)] for x in range(MAXN)]
qq   = []
res  = [0]*MAXN
dist = [0]*MAXN
 
def bfs(src):
    Q = []
    for i in range(0, MAXN):
        dist[i] = INF
 
    dist[src] = 0
 
    Q.append(src)
 
    while Q:
        u = Q.pop(0)
 
        for i in range(1, n+1):
            if dist[i] > dist[u] + adjMatrix[u][i]:
                dist[i] = dist[u] + adjMatrix[u][i];
                Q.append(i)
    return
 
 
n, m =  map(int, sys.stdin.readline().split())
 
 
for i in range(0, m):
    u, v, w =  map(int, sys.stdin.readline().split())
    adjMatrix[v][u] = min(adjMatrix[v][u],w)
 
 
d, q =  list(map(int, sys.stdin.readline().split()))
 
qq   = list(map(int, sys.stdin.readline().split()))
 
bfs(d)
for i in range(0, q):
    res[i] = dist[qq[i]]
 
for i in range(0, q):
    if(res[i] == INF):
        print("Impossible")
    else:
        print(res[i])
