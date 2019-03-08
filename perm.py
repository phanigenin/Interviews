# Permutations of string


def tostring(l):
    return ''.join(l)

def permute(inputl,start,end,res=[]):
    if start==end:
        res.append(tostring(inputl))
    else:
        for i in range(start,end+1):
            inputl[start],inputl[i] = inputl[i],inputl[start]
            permute(inputl,start+1,end,res)
            inputl[i], inputl[start] = inputl[start], inputl[i]
    return res

'''

inp = 'abcd'
N = len(inp)
print(permute(list(inp),0,N-1))

'''

# Possible Paths on matrix
'''
def possiblePaths(mat,ix,iy,jx,jy,res=[]):
    if ix==jx and iy==jy:
        return res
    else:
        p1 = mat[ix][iy],mat[ix+1][iy]
        p2 =
        #res.append(possiblePaths(mat[]))


'''