Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 14:57:15) [MSC v.1915 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> phoneext={'david':1410,'brad':1137}
>>> phoneext
{'david': 1410, 'brad': 1137}
>>> phoneext.keys()
dict_keys(['david', 'brad'])
>>> list(phoneext.keys())
['david', 'brad']
>>> phoneext.values()
dict_values([1410, 1137])
>>> list(phoneext.values())
[1410, 1137]
>>> phoneext.items()
dict_items([('david', 1410), ('brad', 1137)])
>>> list(phoneext.items())
[('david', 1410), ('brad', 1137)]
>>> phoneext.get("kent")
>>> phoneext.get("kent","NO ENTRY")
'NO ENTRY'
>>> 
