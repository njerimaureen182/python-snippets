Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 14:57:15) [MSC v.1915 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> myList=[1,2,3,4]
>>> A=[myList]*3
>>> print(A)
[[1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]]
>>> myList[2]=10
>>> print(A)
[[1, 2, 10, 4], [1, 2, 10, 4], [1, 2, 10, 4]]
>>> 
