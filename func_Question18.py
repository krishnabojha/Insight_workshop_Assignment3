####### check the string is number or not
user_string=input('Enter a string : ')
x=lambda x: x.replace('.','',1).isdigit()
if x(user_string)==True:
    print('The string is a number')
else:
    print('The string is not a number')