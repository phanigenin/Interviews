
# Fibonacci
def fibrecur(n):
    if n<=2:
        return n
    else:
        return fibrecur(n-1)+fibrecur(n-2)

def fibWrapper(n):
    res = [fibrecur(i) for i in range(1,n+1)]
    return res


def fibgen(n):
    a,b = 1,2
    for _ in range(n):
        yield a
        a,b = b,a+b


# Factorial
def factrecur(n):
    if n<=2:
        return n
    else:
        return n*factrecur(n-1)

def factgen(n):
    res = 1
    if n<=2:
        yield n

    for i in range(2,n+2):
        yield res
        res = res*i

'''
l = factrecur(3)
print(l)
l = list(factgen(3))[-1]
print(l)


'''



# sum of squares
def sumSqRecur(n):
    if n==1:
        return 1
    else:
        return n**2 + sumSqRecur(n-1)


def sumSqGen(n):
    res = 1
    for i in range(2,n+2):
        yield res
        res = res + i**2

'''
l = sumSqRecur(3)
print(l)
l = list(sumSqGen(3))[-1]
print(l)
'''



class Fibonacci(object):
    def __init__(self,n):
        self.__num=n
        self.lastnum=None
        self.allnum=[]

    def getAllFib(self):
        return self.allnum

    def getLastFib(self):
        return self.lastnum

    def getNumber(self):
        return self.__num


class FibonacciRecur(Fibonacci):
    def __init__(self,n):
        Fibonacci.__init__(self,n)
        self.generatefibList()

    def generatefibList(self):
        n=self.getNumber()

        self.allnum  = fibWrapper(n)
        self.lastnum = self.allnum[-1] if  self.allnum else 0


class FibonacciGen(Fibonacci):
    def __init__(self,n):
        Fibonacci.__init__(self,n)
        self.generatefibList()

    def generatefibList(self):
        n=self.getNumber()

        self.allnum  = list(fibgen(n))
        self.lastnum = self.allnum[-1] if  self.allnum else 0



def fibfactory(n,mode="A"):
    ref = {"A":FibonacciRecur,"B":FibonacciRecur}
    obj = ref.get(mode)
    print( obj(n).getAllFib() )
    print( obj(n).getLastFib() )

import timeit
t = timeit.Timer(fibfactory(4,"A"))
print(t.timeit())






