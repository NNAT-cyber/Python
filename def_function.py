def pay(hour, rate):
    if hour <= 40:
        no_ovt = hour*rate
        print("Your salary this month is:",no_ovt)
        quit()
    else:
        ovt_hour = hour-40
        ovt_rate = rate*1.5
        yes_ovt = 40*rate + ovt_hour*ovt_rate
        print("You've worked overtime, your salary this month is:",yes_ovt)
        quit()

hour = float(input("Enter hours:"))
rate = float(input("Enter rate:"))
monthly_salary = pay(hour, rate)

print(monthly_salary)