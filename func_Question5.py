###### Factorial of non negative number
num=int(input('Enter a non negative number to calculate factorial : '))
print('Input : '+str(num))
def fact(num):
    if num==1:
        return 1
    else:
        return num*fact(num-1)
if num>0:
    print('Factorial : '+str(fact(num)))
else:
    print('You entered negative number.')