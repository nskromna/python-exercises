from random import choice # ---> choice()
# import random ---> random.choice()

print('...rock...')
print('...paper...')
print('...scissors...')
P1 = input("(enter your choice): ")
P1 = P1.lower()

# for i in range(25):
# print('-----NO CHEATING!-----\n' * 20)

# P2 = input("(enter Player 2's choice): ")
P2 = choice(['rock', 'paper', 'scissors'])
# print('Player 2 chose: ' + P2)
print(f'Player 2 chose {P2}')
if P1 == P2:
    print("It's a match!")
elif P1 == 'rock':
    if P2 == 'scissors':
        print('Player 1 wins!')
    # elif P2 == 'paper':
    #     print('Player 2 wins!')
    else:
        print('Player 2 wins!')
elif P1 == 'paper':
    if P2 == 'rock':
        print('Player 1 wins!')
    else: #elif P2 == 'scissors':
        print('Player 2 wins!') 
elif P1 == 'scissors':
    if P2 == 'paper':
        print('Player 1 wins!')
    else: #elif P2 == 'rock':
        print('Player 2 wins!')
else:
    print('Something went wrong.')