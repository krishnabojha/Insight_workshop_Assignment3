###### count uppercase and lowercase character of string
num=input('Enter a String : ')
def check():
    count_upper=0
    count_lower=0
    for i in num:
        if i.isupper():
            count_upper+=1
        elif i.islower():
            count_lower+=1
    print('No. of Uppercase : {}'.format(count_upper))
    print('No. of lowercase : {}'.format(count_lower))
check()
