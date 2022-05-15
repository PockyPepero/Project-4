from random import *

lotto_list = ['1','2','3','4']
winning_ticket = []

while len(winning_ticket) < 4:
    pick = choice(lotto_list)
    if pick not in winning_ticket:
        winning_ticket.append(pick)

winning_ticket.sort()

print("If your ticket matches these numbers/letters, you win!")
print(winning_ticket)