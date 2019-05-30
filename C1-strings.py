Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 14:57:15) [MSC v.1915 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> "David"
'David'
>>> myName="David"
>>> myName[3]
'i'
>>> myName*2
'DavidDavid'
>>> len(myName)
5
>>> myName
'David'
>>> myName.upper()
'DAVID'
>>> myName.centre(10)
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    myName.centre(10)
AttributeError: 'str' object has no attribute 'centre'
>>> myName.center(10)
'  David   '
>>> myName.find('v')
2
>>> myName.split('v')
['Da', 'id']
>>> 
