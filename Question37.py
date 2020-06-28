############ Multiplication of dictionary 

def get_dict():
    mul=1
    d={}
    n=input('Enter number of keys in dictionary(eg.4) : ')
    try:
        print('\n(Enter key and value separated by comma)')
        for i in range(int(n)):        
            text = input().split(',') #split the input text based on space & store in the list 'text'
            d[text[0]] = int(text[1])
        for i in d:
            mul*=d[i]
        return mul
    except:
        print('value should be integer and separated by comma.')
 
print('Multiplication of Dictionary : '+str(get_dict()))