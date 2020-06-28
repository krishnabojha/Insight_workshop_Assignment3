############## find the string with lowest length
def max_str_length():
    prev=0
    a=input("Enter list of strings separated by space : ").split()
    for data in a:
        if(prev<len(data)):
            prev=len(data)
    return prev
print("The longest string have length of "+str(max_str_length())+" character.")