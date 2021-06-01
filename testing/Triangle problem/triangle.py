def checkTriangle (a,b,c):
    if a == b and b == c:
        print ("equilateral")
        return 'equilateral'
    
    elif a == b or b == c or a == c:
        print ("Isosceles")
        return 'isosceles'

    else:
        print ("Irregular")
        return 'irregular'

# Matthew Everitt
