print('How many kilometers did you cycle today?')
kms = input()
miles = round(float(kms)/1.60934, 2)
print('Ok, you said ' + kms + f'km which is {miles}mi.')