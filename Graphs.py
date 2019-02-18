# Graphs
# Directed ( arcs ) or unDirected ( edges )
'''
Path beteen two Nodes
Shortest Path
Cycles in a graph
Find path that reaches all nodes ( travelling salesman problem )

Weight on Nodes or Edges - cheapest path
Caller - Callee relationships


'''
# backtracking: it tries each possibility in turn until it finds a solution.
gr1 = {'A': ['B', 'C'],
             'B': ['C', 'D'],
             'C': ['D'],
             'D': ['C'],
             'E': ['F'],
             'F': ['C']}

# Path between nodes
def find_path(graph, start, end, path=[]):
    #path.append(start)
    path = path + [start]
    if start==end:
        return path

    if start not in graph:
        return None

    for n in graph[start]:
       if n not in path:# Avoids Cycles
          newpath = find_path(graph,n,end,path)
          if newpath: return newpath

    return None


def find_all_paths(graph, start, end, path=[]):
    #path.append(start)
    path = path + [start]
    if start==end:
        return [path]

    if start not in graph:
        return []

    allpaths = []
    for n in graph[start]:
       if n not in path:# Avoids Cycles
          newpaths = find_all_paths(graph,n,end,path)
          for np in newpaths:
            allpaths.append(np)

    return allpaths

'''
res = find_all_paths(gr1, 'A','D')
print(res)
'''

gr2 = {'A': ['B', 'C','E'],
             'B': ['E', 'D'],
             'C': ['E'],
             'D': ['C'],
             'E': []}

# Same as Find All paths
def count_paths(graph, start, end, path=[]):
    path = path + [start]
    if start==end:
        return [path]

    if start not in graph:
        return []

    allpaths = []
    for n in graph[start]:
       if n not in path:# Avoids Cycles
          newpaths = count_paths(graph,n,end,path)
          for np in newpaths:
            allpaths.append(np)
    return allpaths

# Doesnt evaluate/return all paths, optimised
def count_paths_2(graph, start, end, path=[],count=0):

    path = path + [start]
    if start==end:
        count+=1
        return count

    if start not in graph:
        return 0

    for n in graph[start]:
       if n not in path:# Avoids Cycles
          count = count_paths_2(graph,n,end,path,count)

    return count

#res = len(count_paths(gr2, 'A','E'))
#res = len(count_paths(gr2, 'A','D'))
#res = count_paths_2(gr2, 'A','E')
res = count_paths_2(gr2, 'A','D')
print(res)


