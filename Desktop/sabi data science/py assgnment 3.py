#3. Write a program that accepts a number from 1 to 7
# and display the nname of the day to the user (hint 1 = sunday)

num = int(input('Please choose a number from 1-7?, '))
if num ==1:
    print('{1} is a sunday')
elif num ==2:
    print('{2} is a monday')
elif num ==3:
    print('{3} is a tuesday')
elif num ==4:
    print('{4} is a wednessday')
elif num ==5:
    print('{5} is a thursday')
elif num ==6:
    print('{6} is a friday')
elif num ==7:
    print('{7} is a saturday')
elif num >7:
    print('invalid number')
