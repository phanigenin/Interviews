gr1 = {'A': ['B', 'C'],
             'B': ['C', 'D'],
             'C': ['D'],
             'D': ['C'],
             'E': ['F'],
             'F': ['C']}


def find_all_paths(gr, start,end,path=[]):
    path = path + [start]
    if start==end:
        return [path]

    if start not in gr:
        return []

    allpaths = []
    for nextnode in gr[start]:
        if nextnode not in path:
            nextpaths = find_all_paths(gr,nextnode,end,path)
            for n in nextpaths:
               allpaths.append(n)

    return allpaths

print(find_all_paths(gr1,'A','D'))