from pythonds.basic.stack import Stack
def baseConverter(decNumber,base):
    digits="0123456789ABCDEF"
    remstack=Stack()

    while decNumber>0:
        rem=decNumber%base
        remstack.push(rem)
        decNumber=decNumber//base

    newStr=""
    while not remstack.isEmpty():
        newStr=newStr+digits[remstack.pop()]

    return newStr

print(baseConverter(25,2))
print(baseConverter(25,16))
