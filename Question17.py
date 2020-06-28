######### Multiplication of numbers of the list
a =input('Enter list of numbers separated by space : ').split()
def list_mul():
    x=1
    for i in a:
        x*=int(i)
    return x
print('Output : '+str(list_mul()))