class GraphDij(object):
    def __init__(self,vertices):
        self.v = vertices
        self.graph = [[0 for x in range(vertices)] for y in range(vertices)]

    def printRes(self,distList):
        for idx,dist in enumerate(distList):
            print(' distance to %d is %d'%(idx,dist))

    def minDistNode(self,distList,spSet):
        mindist = 999
        #minindex = 999

        for idx in range(self.v):
            if not spSet[idx] and distList[idx]<mindist:
                mindist = distList[idx]
                minindex = idx

        return minindex


    def dijkstra(self,src):
        distList = [999]*self.v
        distList[src] = 0
        spSet    = [False]*self.v

        for nodesearch in range(self.v): # search for all nodes
            u = self.minDistNode(distList,spSet)
            spSet[u] = True
            for v in range(self.v):# from msNode to target node
                if self.graph[u][v] > 0 and not spSet[v] and distList[v] > distList[u] + self.graph[u][v]:
                    distList[v] = distList[u] + self.graph[u][v]# Update Shortest distance

        self.printRes(distList)


g = GraphDij(9)
g.graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
           [4, 0, 8, 0, 0, 0, 0, 11, 0],
           [0, 8, 0, 7, 0, 4, 0, 0, 2],
           [0, 0, 7, 0, 9, 14, 0, 0, 0],
           [0, 0, 0, 9, 0, 10, 0, 0, 0],
           [0, 0, 4, 14, 10, 0, 2, 0, 0],
           [0, 0, 0, 0, 0, 2, 0, 1, 6],
           [8, 11, 0, 0, 0, 0, 1, 0, 7],
           [0, 0, 2, 0, 0, 0, 6, 7, 0]
           ]

g.dijkstra(2)


