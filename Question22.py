####### remove duplicate item in list

a=input('Enter list of Strings separated by space : ').split()
def remove_duplicate():
    return list(set(a))
print("Output : "+", ".join(remove_duplicate()))