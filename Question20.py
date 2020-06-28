###### Number of Strings that starts and ends with same character

a=input('Eneter list of strings separated by space : ').split()
def count_string():
    count=0
    for i in a:
        if (len(i)>1) & (i[0]==i[len(i)-1]):
            count+=1
    return count   
print("Output : "+str(count_string())) 