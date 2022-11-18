# msg = input("What's the secret password?: ")

# while msg != "bananas":
#     print("WRONG!")
#     msg = input("What's the secret password?: ")

# print("CORRECT!")

# EXERCISE

# num = 1

# while num < 11:
#     print("\U0001f600" * num)
#     num += 1

for num in range(1, 11):
    count = 1
    smileys = "\U0001f600"

    while count < num:
        smileys += "\U0001f600"
        count += 1
    
    print(smileys)