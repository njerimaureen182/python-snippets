Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 14:57:15) [MSC v.1915 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> mySet={3,6,"cat",4.5,False}
>>> mySet
{False, 3, 4.5, 6, 'cat'}
>>> len(mySet)
5
>>> False in mySet
True
>>> "dog" in mySet
False
>>> yourSet={99,3,100}
>>> mySet.union(yourSet)
{False, 3, 4.5, 99, 6, 100, 'cat'}
>>> mySet|yourSet
{False, 3, 4.5, 99, 6, 100, 'cat'}
>>> mySet.intersection(yourSet)
{3}
>>> mySet&yourSet
{3}
>>> mySet.difference(yourSet)
{False, 4.5, 'cat', 6}
>>> mySet-yourSet
{False, 4.5, 'cat', 6}
>>> {3,100}.issubset(yourSet)
True
>>> {3,100}<=yourSet
True
>>> mySet.add("house")
>>> mySet
{False, 3, 4.5, 6, 'house', 'cat'}
>>> mySet.remove(4.5)
>>> mySet
{False, 3, 6, 'house', 'cat'}
>>> mySet.pop()
False
>>> mySet
{3, 6, 'house', 'cat'}
>>> mySet.clear()
>>> mySet
set()
>>> 
