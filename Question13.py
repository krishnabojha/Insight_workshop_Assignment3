############# sort list of tuple
list_data=[]
item=int(input('Enter number of tuple in list : '))
print('Enter key and value of a tuple separated by space : ')
for i in range(item):
    print('Enter {} tuple : '.format(i+1))
    key,value=input().split()
    tuple_data= key,int(value)
    list_data.append(tuple_data)
print('Original list of tuple : {}'.format(list_data))
list_data.sort(key=lambda a:a[1])

print('\nSorted list of tuple : {}'.format(list_data))