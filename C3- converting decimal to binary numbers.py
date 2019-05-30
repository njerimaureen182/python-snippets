from pythonds.basic.stack import Stack
def divideBy2(decNumber):
    remstack=Stack()

    while decNumber>0:
        rem=decNumber%2
        remstack.push(rem)
        decNumber=decNumber//2

    binStr=""
    while not remstack.isEmpty():
        binStr=binStr+str(remstack.pop())
    
    return binStr

print(divideBy2(42))