###### find unique element of list
import numpy as np
num=input('Enter element of list separated by space :  ').split()
print('Input list : '+str(num))
def check():
    return np.unique(num)

print('The list of unique element : {}'.format(check()))