####### concating string to each element of the list

num_list=input('Enter list of numbers separated by space : ').split()
prefix=input('Enter a string that you want to in prefix : ')
def concat_list():
    for i in range(len(num_list)):
        num_list[i]=prefix+num_list[i]
    return num_list
print('Output : '+str(concat_list()))