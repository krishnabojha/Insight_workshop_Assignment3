###### print even number of list
import numpy as np
num_list=[]
result=[]
num=input('Enter number of list separated by space : ').split()
for i in num:
    num_list.append(int(i))
def check():
    for j in num_list:
        if j%2==0:
            result.append(j)
check()
print('Output : {}'.format(result))