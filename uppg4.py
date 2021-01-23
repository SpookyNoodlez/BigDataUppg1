import random

values = ['A',2,3,4,5,6,7,8,9,10,'J','Q','K']
suits = ['♥','♦','♣','♠']

selectedValue = values[random.randint(0, len(values)-1)]
selectedSuit = suits[random.randint(0, 3)]

print(selectedValue, selectedSuit)