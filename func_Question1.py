######## calculate maximum value of list
a=[]
input_list=input('Enter three number separated by space : ').split()
for i in input_list:
    a.append(int(i))
print('Input list : '+str(tuple(a)))
def max_value():
    return max(a)
print('The maximum value is '+str(max_value()))