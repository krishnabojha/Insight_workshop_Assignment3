###########check whether a number is in a given range.

num=int(input('Enter a number : '))
def check():
    if num in range(5,20):
        print('{} is in range.'.format(num))
    else:
        print('{} is not in range.'.format(num))
check()