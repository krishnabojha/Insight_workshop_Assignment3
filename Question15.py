####### put the string in the middle of another string
word=input('String you want in middle : ')
b=input('String (eg. <<>>) : ')
def insert_mid():
    mid=int(len(b)/2)
    return b[:mid]+word+b[mid:]
print(insert_mid())