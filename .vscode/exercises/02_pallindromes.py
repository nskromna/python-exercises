def palindrome(str):
    if str == str[::-1]:
        return True
    return False

print(palindrome('aba'))
print(palindrome(' aba'))
print(palindrome('aba '))
print(palindrome('greetings'))
print(palindrome('100000001'))
print(palindrome('Fish hsif'))
print(palindrome('pennep'))