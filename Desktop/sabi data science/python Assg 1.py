cost = int(input('Please, what is the cost of a bike? '))
if cost >=100_000:
    tax = (15/100)*cost
    print('Kindly pay 15% which is' ,+ tax)
elif cost >50000 and cost<100000:
    tax = (10/100)*cost
    print('Kindly pay 10% which is' ,+ tax)
elif cost <=50000 and cost>10000:
    tax = (5/100)*cost
    print('Kindly pay 5% which is' ,+ tax)
else :
    print ('invalid Error')
