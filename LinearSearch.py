arr = [3753, 8634, 424537, 59, 1, 7, 212, 4, 8, 10, 294, 391, 294, 5, 6, 2]

def linearSearch(num):
    count = 0
    for item in arr:
        if item == num:
            print(count) 
            return
        count += 1
    print("Numri nuk ekziston ne array")

linearSearch(1)

