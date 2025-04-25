from Setup import character
import time

name = character['name'].title()


def backstory():
  '''Print the backstory of the game'''
  print(
      '\nYou are a great older sibling who will do anything to protect your little sister.'
  )
  time.sleep(2)
  print('You have a loving family and a happy life.\n')
  time.sleep(3)
  print('But one day, your little sister was turned into a demon by a demon.')
  time.sleep(2)
  print('You are heartbroken and want to save her.')
  time.sleep(2)
  print(
      'You have to find the legendary medicine,"The Flower of Life", that can turns her back.\n'
  )
  time.sleep(2)
  print('But...\n')
  time.sleep(4)
  print(
      'To bring her back, you must venure into hell itself and scale the largest mountain in the heart of hell to find the "The Flower of Life".'
  )
  time.sleep(4)
  print(
      'After a long journey you finally reach the collosal mountain with the "The Flower of Life".'
  )
  time.sleep(2)
  print('\nHowever...\n')
  time.sleep(4)
  print(
      'Fate continues toying with you as you learn, there is only one "The Flower of Life" and it lies is at the peak of the mountain.\n'
  )
  time.sleep(3)
  print(
      'To reach it you be prepared to not only fight your way through the demons guarding it, but also the obstacles that come your way.'
  )
  time.sleep(3)
  print('\nTo assist you on your journey, you have a backpack with the capacity to carry 7 items.')
  time.sleep(3)
  print('\nPick the right objects and you will be able to reach the peak of the mountain.')
  time.sleep(3)
  print('Pick the wrong objects and you will be doomed to fail.')
  time.sleep(1)
  print(f'\nThe stakes are high. Good luck {name}!\n')
