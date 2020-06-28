###### check whether dictionary in the list is empty or not

a=input('Enter list of dictionary separated by space(eg. {1,2} {} {} ) : ').split()
def empty_test():
    for i in a:
        if len(i)!=2:
            return 'False'
    return 'True'
print(empty_test())