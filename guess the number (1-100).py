import random

b = random.randint(1,100)
while True :
   try:
      a = int(input('Guess the number between 1 to 100'))
      print('\n',a)
      if a == b :
          print('Congratulations_You_Won 🏆')
          again = input('Try Again? (yes/no)').lower()
          if again=='yes':
             b = random.randint(1,100)
             continue
          else:
             print('Thanks For Playing...☺️')
             break    
      elif a>b :
          print('Too_High 📈')
      else:
          print('Too_Low 📉')
    except ValueError :
          print('Please_Enter_a_valid_Number ❌')
