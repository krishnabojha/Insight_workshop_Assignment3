######## calculate maximum value of list
a=[]
input_list=input('Enter number of list separated by space : ').split()
for i in input_list:
    a.append(int(i))
print('Input list : '+str(tuple(a)))
def sum_value():
    return sum(a)
print('The sum is '+str(sum_value()))