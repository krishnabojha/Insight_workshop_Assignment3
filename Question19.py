#### smallest number of the list

a =input('Enter list of numbers separated by space : ').split()
x=[int(i) for i in a]
def min_list():
    return min(x)
print("Output : "+str(min_list()))