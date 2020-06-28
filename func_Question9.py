###### check number is prime or not
import numpy as np
num=int(input('Enter a number : '))
def check():
    itr=2
    while itr<num:
        if num%itr==0:
            print("{} is not prime".format(num))
            return 0
        itr+=1
    print("{} is prime".format(num))
check()