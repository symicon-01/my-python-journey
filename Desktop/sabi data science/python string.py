str1 = 'my name is fadesola' #assigning a single quote string to str1
print(str1)

str2 = "my name is fadesola" #assigning a double quote string to str2
print(str2)

str3 = '''my name is fadesola''' #assigning a triple single quote string to str3
print(str3)

str4 = """my name is fadesola""" #assigning a triple double quote string to str4
print(str4)

#MULTILINE STRING
str5 = '''this is my
own multi-line string
using a single quote
''' #assigning triple single quote multi-line string to str5
print(str5)

str6 = """this is my
second multi-line string
using double quotes""" #assigning triple double quote multi-line string to str6
print(str6)

#QUOTE IN A QUOTE
str7 = 'welcome to "engineer-D`s" class' #including double quote in a single quote string
print(str7)

str8 = "welcome to 'engineer-D`s' class" #including single quote in a double quote string
print(str8)

#string length and indexing
str9 = 'sabi programmer'
print(len(str9)) #return the length of str9
print(str9[0]) #return first index using +VE indexing
print(str9[-15]) #return first index using -VE indexing
print(str9[14]) #return last index using +VE indexing
print(str9[-1]) #return last index using -VE indexing
print(str9[7]) #return the 8th index using +VE indexing
print(str9[-8]) #return the 8th index using -VE indexing

#STRING CONVERSION
print(str(100)) #converting an int to a str
print(str(12.2342)) #converting a float to a string
print(str(False)) #converting a boolean to a string

#ESCAPE SEQUENCES
str10 = 'welcome to \'engineer-D`s\' class' #escape sequence to include single quotes
print(str10)

str11 = "welcome to \"engineer-D`s\" class" #escape sequence to include double quotes
print(str11)

str12 = r'welcome to \'engineer-D`s\' class' #ignoring escape sequence
print(str12)

str13 ='https:\\sabiprogrammers.org\\home' #escape sequence to include backslash
print(str13)

str14 = 'including\tdistance' #including tab in a sequence
print(str14)

str15 = 'go to \nnext line' #include newline
print(str15)

#STRING OPERATORS
str16 = 'catherine'
str17 = 'welcome back'
print(str16 + str17) #concatenating two strings
print(str16 * 3) #kate how many times would i call you
print(str16[0:4]) #slicing
print(str16[5:9]) #slicing
print('kate' in str16) #check if kate is in str16
print('back' in str17) #check if back is in str17
print('kate' not in str16) #check if kate is not in str16
print('back' not in str17) #check if kate is not in str17

box = 'hello'
print (box)

