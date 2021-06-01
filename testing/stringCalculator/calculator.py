def Add(stringNumbers):
    sum_digit = 0
    for x in stringNumbers:
        if x.isdigit() == True:
            z = int(x)
            sum_digit = sum_digit + z
    return sum_digit
    
