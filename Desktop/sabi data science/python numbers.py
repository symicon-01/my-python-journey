#INTEGERS
num1 = 100 #assigning a +ve int to num1
print(num1)

num2 = -10 #assingning a -ve integer to num2
print (num2)

num3 = 1_000_000 #separation numbers with underscore
print (num3)

print (type(num1), type(num2), type(num3)) #printing type num1, num2 and num3

num4 = int (5.0345) #converting float to integer

num5 = int ('16') #converting string to interger
print (num4)
print (num5)

num6 = int('100', 2)#converting string 100 to integer
print (num6)

num7= int('3234', 8) #converting string to int
print (num7)

#BINARY
num8 = 0b111101110101 #assigning binary number to num8
print (num8) #printing num8 in base 10
print (type(num8)) #printing out the type of var num8

num9 = 0b1_001_111_101 #separating binary no with underscore
print (num9)

#OCTAL
num10 = 0o12 #assigning octal number to num10
print (num10) #printing num 10 in base 10
print (type(num10))#printing type of num10

num11 = 0o12344567 #assigning oct to num 11
print (num11) #printing num11 in base 10

#HEXADECIMAL
num12 = 0x123afde #assigning hex to num 12
print (num12)
print (type(num12))

num13 = 0x1234567adefcb #assigning hex to num13
print (num13)
print (type(num13))

#FLOAT
num14 = 1.23356734 #assigning a +ve float to num14
print (num14)
print (type(num14))

num15 = -1234542.12456 #assigning a -ve float to num15
print (num15)
print (type(num15))

num16 = 123_234.732_357 #separating float with underscore____
print (num16)
print (type(num16))

num17 = 2e400 #exceeding memory size
print (num17)
print (type(num17))

num18 = 1e3 #using scientific notation
print (num18)
print (type(num18))

num19 = 3.14234232e3 #using scientific notation
print (num19)
print (type(num19))

#FLOAT CONVERSION
num20 = float('-5.5') #converting -ve float string to float
print (num20)
print (type(num20))

num21 = float('5') #converting +ve int string to float
print (num21)
print (type(num21)) 

num22 = float('          -5')#converting string with spaces and int to float
print (num22)
print (type(num22))

num23 = float('1e3') #converting scientific notation
print (num23)
print (type(num23))

num24 = float('-infinity') #converting -infinity to float
print (num24)
print (type(num24))

num25 = float('inf') #converting inf to float
print (num25)
print (type(num25))

#ARITHMETIC
num26 = 1500
num27 = 20

print (num26+num27) #adding num26 and num27
print (num26-num27) #subtraction
print (num26*num27) #MULTIPLICATION
print (num26/num27) #division
print (num26%num27) #modulus prints out reminder
print (num26**num27) #exponent or power
print (num26//num27) #floor division
print (f'{hex(num26)}')#converting num26 to hex
print (f'{oct(num26)}')#converting num26 to oct
print (f'{bin(num26)}')#converting num26 to bin
print (pow(num27, 3)) #num27^3
print (abs(-1245432)) #absolute
print (round(123.345678))#round to nearest whole number
print (f'{hex(num27)}')#converting num27 to hex
print (f'{oct(num27)}')#converting num27 to oct
print (f'{bin(num27)}')#converting num27 to bin
