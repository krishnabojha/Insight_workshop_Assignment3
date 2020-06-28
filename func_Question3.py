######## calculate maximum value of list
a=[]
input_list=input('Enter number of list separated by space : ').split()
for i in input_list:
    a.append(int(i))
print('Input list : '+str(tuple(a)))
def mul():
    mul=1
    for value in a:
        mul*=value
    return mul
print('The Multiplication is '+str(mul()))