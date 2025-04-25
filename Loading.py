import time


def loading():
  print('Loading...')
  time.sleep(1)
  for i in range(10):
    print('.', end='')
    time.sleep(1)
  print('Finished Loading!')
