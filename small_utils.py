def decimal2binary(x):
    return bin(x).replace("0b","")


def decimal2binary2(x):
    q, rem, decimal = 1,0,x
    l = []
    while(q>0):
        q   = x//2
        rem = x%2
        l.append(rem)
        x=q

    return ''.join([str(i)for i in l[::-1]])


def decimal2binary3(x,p=[]):
    if x>1:
        decimal2binary3(x//2)

    p += [x % 2]
    return p



def binary2decimal(n):
    return int(n,2)

def binary2decimal2(n):
    power  = 0
    base = 2
    dec = 0
    for c in n[::-1]:
        rem = int(c)
        dec += rem*pow(base,power)
        power+=1
    return dec




#res = binary2decimal('100')
res = binary2decimal2('1010')
print(res)
'''
res = decimal2binary(100)
print(res)
res = decimal2binary2(100)
print(res)
res = decimal2binary3(100)
print(res)

'''
