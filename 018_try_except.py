nums = [1, 2, 3, 4]

for i in range(7):
    try:
        print(f"nums[{i}] = {nums[i]}")
    except IndexError:
        print(f"{i} - There's no such index in this list")
    except:
        print("Something went wrong")
    else: 
        print("and the next one is:")
    finally:
        print("finished the loop")
