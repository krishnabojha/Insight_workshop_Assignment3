########### check the key in the dictionary

a={1: 2, 2: 4, 3: 6, 4: 9, 5: 8, 6: 22}
input_key=input('(dictionary conains key from 1 to 6)\nEnter any key : ')
def check_key():
    try:
        print('This {} key is present with {} value in dictionary.'.format(input_key,a[int(input_key)]))
    except:
        print('This {} key is not present in dictionary.')
check_key()