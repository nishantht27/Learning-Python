import random

while True :
  a = input('stone...paper...scissor...? ').lower()
  print('\nYou chose:', a)
  item = ('stone', 'paper', 'scissor')
  b = random.choice(item)
  print('Computer chose:', b)
  if a == b:
       print('DRAW!!')
  elif (a == 'stone' and b == 'scissor') or \
       (a == 'paper' and b == 'stone') or \
       (a == 'scissor' and b == 'paper'):
       print('YOU WON!! 🔥')
       break
  else:
       print('BETTER LUCK NEXT TIME 😜')
