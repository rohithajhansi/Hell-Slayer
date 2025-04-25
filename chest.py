from Setup import chest, character
from random import choice

def open_chest():
  print('\nYou found a chest!'
        '\nDo you want to open it?')
  try:
    while True:
      user_input = input('\nEnter yes or no: \n').lower().strip()
      if user_input == 'yes':
        print('You opened the chest and found a random item!\n')
        random_item = choice(list(chest.keys()))
        print(f'You found a {random_item} item!')
        character[random_item] += chest[random_item]
        print(f'Your {random_item} has increased by {chest[random_item]}!')
        break       
      if user_input == 'no':
        print('You decided not to open the chest.')
        break
  except (TypeError, ValueError, Exception):
    print('Please enter yes or no.')