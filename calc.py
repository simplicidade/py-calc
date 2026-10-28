num1 = int(input("Enter Your First Number: "))
num2 = int(input("Enter Your Second Number: "))

print("(1) +")
print("(2) -")
print("(3) *")
print("(4) /")

valinta = input("Make Your Choice (1-4): ")

if valinta == "1":
    print("The Result is:", num1 + num2)
elif valinta == "2":
    print("The Result is:", num1 - num2)
elif valinta == "3":
    print("The Result is:", num1 * num2)
elif valinta == "4":
    print("The Result is:", num1 / num2)
else:
    print("Selection not recognized.")