tpl1 = ('vera', 'sola', 'kate', 'gbenga')#string tuple
print (tpl1)
print (type(tpl1))
tpl2 = (1, 2, 3, 4)#int tuple
print(tpl2)
print (type(tpl2))
tpl3 = (1.1, 2.2, 3.3, 4.4)#float tuple
print (tpl3)
print (type(tpl3))
tpl4 = (True, False)#bool tuple
print (tpl4)
print (type(tpl4))
tpl5 = (1, 1.1, 'vera', True)#heterogenous tuple
print (tpl5)
print (type(tpl5))
tpl6 = ()#empty tuple
print (tpl6)
print (type(tpl6))

tpl7 = 'vera', 'sola', 'kate', 'gbenga'#string tuple
print (tpl1)

tpl8 = 1, 2, 3, 4#int tuple
print(tpl2)

tpl9 = 1.1, 2.2, 3.3, 4.4#float tuple
print (tpl3)

tpl10 = True, False#bool tuple
print (tpl4)

tpl11 = 1, 1.1, 'vera', True#heterogenous tuple
print (tpl5)

#INDEXING
print(tpl1[0]) #first index using +ve indexing
print(tpl1[-4]) #first index using -ve indexing

print(tpl1[3]) #last index using +ve indexing
print(tpl1[-1]) #last index using -ve indexing

print(tpl1[1]) #second index using +ve indexing
print(tpl1[-3]) #second index using -ve indexing

#DELETING
del tpl1 #delete tpl1

#conversion
tpl12 = tuple('sabi programmers') #converting a string to tuple
print(tpl12)
tpl13 = tuple(['sabi','programmers']) #converting a list to tuple
print(tpl13)
tpl14 = tuple({1,2,3,4,5,6}) #converting a set to tuple
print(tpl14)
tpl15 = tuple({1:'one', 2:'two'}) #converting dict to tuple
print(tpl15)

#operators
print(tpl2 + tpl3) #+operator
print(tpl4 * 4) #*operator
print(tpl2[1:3]) #slicing
print(2.4 in tpl3) #in operator
print(2.4 not in tpl3) #not in operator
