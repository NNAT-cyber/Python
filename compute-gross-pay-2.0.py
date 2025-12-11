h1 = input("Enter working hours: ")

try :
    h1 = float(h1)

except :
    print("Please enter a numeric number.")
    quit()

r1 = input("Enter working rates: ")

try :
    r1 = float(r1)

except :
    print("Please enter a numeric number.")
    quit()

fh1 = float(h1)
fr1 = float(r1)

if fh1 <= 40 :
    
    p1 = fh1 * fr1
    print("Regular")
    print("Your payment is",p1)

else :

    h2 = fh1 - 40
    r2 = fr1 * 1.5
    p2 = 40 * fr1 + float(h2) * float(r2)

    print("Overtime")
    print("Your payment is",p2)


    

