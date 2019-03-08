

gr2 = {
        '0' :['1','3'],
        '1' :['2'],
        '2' :[],
        '3' :['0','4','7'],
        '4' :['3','5','6','7'],
        '5' :['4','6'],
        '6' :['4','5','7'],
        '7' :['3','4','6']
}



def find_paths_pr(graph,start,end,path=[]):
    path = path + [start]

    if start==end:
        return [path]

    if start not in graph:
        return []

    allpaths = []
    for nextnode in graph[start]:
        if nextnode not in path:
            newpaths = find_paths_pr(graph,nextnode,end,path)
            if newpaths:
                for newpath in newpaths:
                    allpaths.append(newpath)
        #return path

    return allpaths

allpaths = find_paths_pr(gr2,'0','7')
d = {len(x)-1:x for x in allpaths}
#print(d)
shortespath = d.get(min(d.keys()))
print(shortespath)

