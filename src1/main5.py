# Demonstrates inport and random.choice

# import random

# coin = random.choice (["heads", "tails"])
# print (coin)

# Demonstrates from

# from random import choice

# coin = choice (["heads", "tails"])
# print (coin)

# Demonstrates randint

# import random
# number = random.randint(1, 10)
# print (number)

# Demonstrates shuffle

# import random

# cards = ["jack", "queen", "king"]
# random.shuffle (cards)
# for card in cards:
#     print (card)

# Demonstrates Statistics

# import statistics
# print (statistics.mean([100, 90]))

# Demonstrates sys.argv

# import sys

# print ("hello, my name is", sys.argv[1])

# Demonstrates IndexError

import sys

try:
    print ("hello my name is", sys.srgv[1])
except IndexError:
    print ("Too few argument")    



