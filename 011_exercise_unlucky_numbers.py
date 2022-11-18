# for num in range(1, 21):
#     if num % 2 == 0:
#         print(f'{num} is even')
#     elif num == 4 or num == 13:
#         print(f'{num} is unlucky')
#     else:
#         print(f'{num} is odd')

for num in range(1, 21):
    if num % 2 == 0:
        state = 'even'
    elif num == 4 or num == 13:
        state = 'unlucky'
    else:
        state = 'odd'

    print(f'{num} is {state}')