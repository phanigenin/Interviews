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

l = [2,3,10,2,4,8,1]
print(maxDifference(l))
