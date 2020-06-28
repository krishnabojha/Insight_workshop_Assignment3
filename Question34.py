########## concatination of two dictionary

concat_list=[]
dict_num=input('Enter the number of dictionary(eg. 2): ')
def get_dict(num):
    d ={}
    n=input('Enter number of keys in {}st dictionary(eg.4) : '.format(num+1))
    try:
        print('\n(Enter key and value separated by comma)')
        for i in range(int(n)):        
            text = input().split(',') #split the input text based on space & store in the list 'text'
            d[text[0]] = text[1]
        return (list(d.items()))
    except:
        print('Enter valid input ')
for i in range(int(dict_num)):
    concat_list+=get_dict(i)
    
print('Output : '+str(dict(concat_list)))