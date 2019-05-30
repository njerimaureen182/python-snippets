Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 14:57:15) [MSC v.1915 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> myList=[1,3,True,6.5]
>>> myList
[1, 3, True, 6.5]
>>> myList[0]=2**10
>>> myList
[1024, 3, True, 6.5]
>>> myName="David"
>>> myName
'David'
>>> myName[0]='X'
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    myName[0]='X'
TypeError: 'str' object does not support item assignment
>>> 
