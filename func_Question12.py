###### Add a number with random number
import random
def add(a):
    unknown_num=int(random.random()*100)
    print('The sum between {} and {}(unknown_num) : {}'.format(a,unknown_num,(a+unknown_num)))
a=int(input('Enter a number : '))    
add(a)