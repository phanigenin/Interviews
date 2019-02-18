# Implement a class, and include methods
import numpy as np

class Graph():
   def __init__(self,vertices):
      self.graph = {}
      self.V     = vertices

   def addEdge(self,start,end):
      ed = self.graph.get(start,[])
      ed.append(end)
      self.graph[start] = ed

   def getAllPaths(self,start,final,path=[]):
           gr = self.graph
           path = path + [start]
           if start==final:
               return [path]

           if start not in gr:
               return []

           allpaths = []
           for n in gr[start]:
               if n not in path:
                  newpaths = self.getAllPaths(n , final, path)
                  for np in newpaths:
                      allpaths.append(np)

           return allpaths

   # A pain, if you have cycles. Better get all the paths and count
   def getCountPaths(self,start,final,path=[],count=0):
           gr = self.graph
           path = path + [start]
           print(start)
           if start not in gr:
               return 0

           if start==final:
               count+=1
               return count

           allcount = 0
           for n in gr[start]:
               #if n not in path:
                  newpaths = self.getCountPaths(n , final, path, count)
                  allcount += np.sum(newpaths)
           return allcount





'''
gr1 = {'A': ['B', 'C'],
             'B': ['C', 'D'],
             'C': ['D'],
             'D': ['C'],
             'E': ['F'],
             'F': ['C']}

'''
gr1 = Graph(6)
gr1.addEdge("A","B")
gr1.addEdge("A","C")
gr1.addEdge("B","C")
gr1.addEdge("B","D")
gr1.addEdge("C","D")
gr1.addEdge("D","C")
gr1.addEdge("E","F")
gr1.addEdge("F","C")

res = gr1.getAllPaths("A","E")
print(res)
rescount = gr1.getCountPaths("A","E")
print(rescount)




