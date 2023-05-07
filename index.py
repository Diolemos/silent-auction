import os
clear = lambda: os.system('clear')

# to clear the console clear()

bidders = {}


def auction():
    continue_auction = 'yes'
    while continue_auction != 'no':
        current_bidder = input("What is your name?")
        current_bid = input("What is your bid?")
        bidders[current_bidder] = int(current_bid)
        continue_auction = input('Is there more people in the room? Type "yes" or "no" ')
        clear()

    highest_bidder = max(bidders, key=bidders.get)
    highest_bid = bidders[highest_bidder]
    
    print(f"The highest bidder was {highest_bidder}, with ${highest_bid}")
    
auction()