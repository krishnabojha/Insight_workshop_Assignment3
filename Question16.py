### sum of the numbers in list
a =input('Enter list of numbers separated by space : ').split()
x=[int(i) for i in a]
def list_sum():
    return sum(x)
print('Output : '+str(list_sum()))