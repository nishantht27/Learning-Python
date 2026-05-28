import random
a=input('stone...paper...scissor...?')
print('\n',a)
item=('stone','paper','scissor')
b= random.choice(item)
print(b)
if (a==b):
    print('YOU WON!!')
else:
    print('BETTER LUCK NXT TIME')