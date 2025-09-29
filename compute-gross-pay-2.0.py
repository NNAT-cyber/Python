h1 = input("Enter working hours: ")
r1 = input("Enter working rates: ")

fh1 = float(h1)
fr1 = float(r1)

p1 = fh1 * fr1

if fh1 <= 40 :
    print("Regular")
    print("Your payment is",p1)

else :

    h2 = fh1 - 40
    r2 = fr1 * 1.5

    p2 = 40 * fr1 + float(h2) * float(r2)
    print("Overtime")
    print("Your payment is",p2)


    

