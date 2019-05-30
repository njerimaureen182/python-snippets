price=24
item="banana"
itemdict={"item":"banana","cost":24}
print("The %s costs %d cents"%(item,price))
print("The %+10s costs %25.2f cents"%(item,price))
print("The %+10s costs %10.4f cents"%(item,price))
print("The %(item)s costs %(cost)17.2f cents"%itemdict)