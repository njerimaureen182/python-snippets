from pythonds.basic.stack import Stack
rStack = Stack()

def toStr(n,base):
    convStr="0123456789ABCDEF"
    while n > 0:
        if n < base:
            rStack.push(convStr[n])

        else:
            rStack.push(convStr[n%base])
        n = n//base
        res = " "
    while not rStack.isEmpty():
        res = res + str(rStack.pop())
    return res
print(toStr(1453,16))                 