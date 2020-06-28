###### remove the given key
d={}
def get_dict():
    mul=1
    n=input('Enter number of keys in dictionary(eg.4) : ')
    try:
        print('\n(Enter key and value separated by comma)')
        for i in range(int(n)):        
            text = input().split(',') #split the input text based on space & store in the list 'text'
            d[text[0]] = text[1]
    except:
        print('value should be integer and separated by comma.')
get_dict()
print('Input Dictionary : '+str(d))
key=input('\nEnter the key that you want to remove : ')
if key in d:
    del d[key]
else:
    print("\nThis key is not present in dictionary")

print('Updated dictionary : '+str(d))