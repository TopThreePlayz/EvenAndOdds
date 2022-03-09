i = 0
even = 0
odd = 0

a = int(input("How many numbers do you need to check? "))
for i in range(a) :
    number = int(input("Enter number: "))
    i = i + 1
    if (number % 2 == 0):
        even = even + 1
        print(number, "is an even number.")
    if (number % 2 == 1):
        odd = odd + 1
        print(number, "is an odd number.")
print("You entered", even, "even number(s).")
print("You entered", odd, "odd number(s).")       
