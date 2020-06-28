####### Largest number in the list

a =input('Enter list of numbers separated by space : ').split()
x=[int(i) for i in a]
def max_list():
    return max(x)
print("Output : "+str(max_list()))