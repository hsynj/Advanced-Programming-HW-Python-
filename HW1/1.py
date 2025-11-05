def checkDigit(n):
    try:
        float(n)
        return True
    except Exception:
        return False

list = []
while True:
    n = input("Enter foods price(\"-1\" for exit): ")
    if n == "-1":
        print("Okay, here is your list of prices: ", list)
        break
    if checkDigit(n):
        list.append(float(n))
    else:
        print("Enter a valid price.")
        continue
tax = 0
tip = 0
total = 0
for i in list:
    tax += i * 0.07
    tip += i * 0.18
    total += i
total += (tax + tip)
print("Tax: ", tax)
print("Tip: ", tip)
print("Total: ", total)
