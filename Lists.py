newlist = list()

while True:
    inp = input("Enter a number: ")
    if inp == 'done':
        break
        
    try:
        finp = float(inp)
    except ValueError:
        print("Please enter a number.")
        continue

    newlist.append(finp)

average = sum(newlist)/len(newlist)

print(average)