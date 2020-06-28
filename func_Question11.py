###### add and multiplication using lambda function
import numpy as np
a=int(input('Enter a number to add with 15 : '))
b,c=input('Enter x and y separated by space : ').split()
result_sum=lambda x:x+15
result_mul=lambda x,y:x*y

print('sum : {}'.format(result_sum(a)))
print('Multiplication : {}'.format(result_mul(int(b),int(c))))