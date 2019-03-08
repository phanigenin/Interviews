from collections import defaultdict

# Adjacency List implementation

class Graph(object):
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self,start,end):
        self.graph[start].append(end)

    # Breadth First search
    def bfs(self,start):
        visited = [False]*len(self.graph)
        queue = []
        queue.append(start)
        visited[start] = True
        while len(queue):
              currnode = queue.pop(0)
              print(currnode,end=",")
              for nextnode in self.graph[currnode]:
                  if not visited[nextnode]:
                      queue.append(nextnode)
                      visited[nextnode]=True


    def dfs(self,start):

        def dfsutil(st,visited):
            visited[st]=True
            print(st,end=",")

            for nextnode in self.graph[st]:
                if not visited[nextnode]:
                  dfsutil(nextnode,visited)


        visitedrec = [False]*len(self.graph)
        dfsutil(start,visitedrec)
















g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)

g.bfs(2)
print('\n')
g.dfs(2)


