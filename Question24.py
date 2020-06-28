######## clone or copy

import copy
a=input("Enter list of string separated by space : ").split()
b=a.copy()
c=copy.deepcopy(a)
print('Copy : '+str(b))
print('DeepCopy : '+str(c))