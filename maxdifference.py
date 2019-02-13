# Given an array, max of diff of all elements to the left

def maxDifference(a):
    maxres = -1
    for i in range(1,len(a)):
        temp = []
        for y in range(i):
            if a[y]<a[i]:
                temp.append(a[i]-a[y])
            else:
                temp.append(-1)

        if temp and (maxres < max(temp)):
          maxres = max(temp)

    return maxres

# optimised
def maxDifference2(a):
    maxres = -1
    temp = []
    prevlist = []
    for i in range(1,len(a)):
        latestdiff = a[i]-a[i-1]
        newelem = -1 if latestdiff<0 else latestdiff
        print(latestdiff)
        if temp:
            new = [latestdiff+x if latestdiff+x>=0 else -1 for x in temp ]

            print(new)
            prevlist = new
            temp.extend(new)
        temp.append(newelem)
        print(temp)
        '''
        for y in range(i):
            if a[y]<a[i]:
                temp.append(a[i]-a[y])
            else:
                temp.append(-1)



        if temp and (maxres < max(temp)):
          maxres = max(temp)

        
        '''


    return maxres

l = [2,3,10,2,4,8,1]

print(maxDifference(l))
#print(maxDifference2(l))
