import random

def createlist(n):
    n=int(n)#
    return list(random.uniform(0,100)*random.randint(-1,1) for i in range(n) )

def createlis(n):
    n=int(n)#
    return list(random.randint(0,100)*random.randint(-1,1) for i in range(n) )

def fTask(n):
    Neg=0
    Arr = createlist(n)
    Mult=1
    Min=9^99
    Max = -9^99
    for iD in Arr:
        if iD < 0:
            Neg += iD

        if Min > iD:
            Min = iD
            Mind=Arr.index(iD)
        if Max < iD:
            Max = iD
            Mxid = Arr.index(iD)
    if  Mind<Mxid:
         for b in range(Mind,Mxid):
             Mult*=Arr[b]
    else:
            for b in range(Mxid, Mind):
                Mult *= Arr[b]
    print(Mult)
    print(Neg)
    print(Arr)

def ThTask(n):
    Arr =  createlist(n)
    lastPos=-1
    SumOfPos=0
    Max = -9 ^ 99
    for i in range(0,n):
        if Max < Arr[i]:
            Max = Arr[i]
        if Arr[i]>0:
            lastPos = i
    if lastPos != -1:
        for i in range(0,lastPos):
            SumOfPos+=Arr[i]
    print(Arr)
    print(SumOfPos)
def main():
    n=10
    fTask(n)
    ThTask(n)
if __name__ == '__main__':
    main()
