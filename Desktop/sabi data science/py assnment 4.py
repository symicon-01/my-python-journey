
# To take month and year input from the user
month = int(input('choose a num between 1-12: '))

    
if((month==2) and ((year%4==0)  or ((year%100==0) and (year%400==0)))) :
    print("Number of days is 29")
    print('The month is Feburary')

elif(month==2) :
    print("Number of days is 28")
    print('The month is Feburary')

elif(month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12) :
        arr = [1,Janaury, 3, 5, 30, 31, 30, 31, 31, 30, 31, 30, 31 ]
        print ("the month is ",+ arr[month-(1)])
        
        print("Number of days is 31")
        
    

else :
    print("Number of days is 30")
