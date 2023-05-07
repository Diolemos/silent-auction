import os
clear = lambda: os.system('clear')

# to clear the console clear()

biders = {}


def auction():
    continue_auction = 'yes'
    while continue_auction != 'no':
      current_bider =   input("What your name?")
      current_bid = input("What is your bid?")
      biders[current_bider] = current_bid
      continue_auction = input('is there more people in the room? type "yes" or "no" ' )
      clear()


auction()        