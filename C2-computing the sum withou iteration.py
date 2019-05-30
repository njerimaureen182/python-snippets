import time

def sumOfN3(n):

    start=time.time()
    end=time.time()

    return(n*(n+1))/2,end-start

print(sumOfN3(10))