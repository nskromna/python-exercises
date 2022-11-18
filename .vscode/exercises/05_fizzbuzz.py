def fizzbuzz(num):
    for i in range(1, num+1):
        if i % 3 == 0:
            x = 'fizz'
            if i % 5 == 0:
                x = 'fizzbuzz'
        elif i % 5 == 0:
            x = 'buzz'
        else:
            x = i
        print(x)
    

fizzbuzz(15)
            
        