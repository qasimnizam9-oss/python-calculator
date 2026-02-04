#thsis si my calcualtor begienr project

number_1 = int(input("Enter the first numer: "))
number_2 = int(input("Enter the second number: "))


print("choose the operation you wantt to perfom")
print("1. Addition")
 
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = input("enter your choice (1/2/3/4):")
if choice == '1':
    print(number_1 + number_2)
elif choice == '2':
    print(number_1 - number_2)
elif choice == '3':
    print(number_1 * number_2)
elif choice == '4':
    if number_2 != 0:
        print(number_1 / number_2)
    else:
        print("Error: Division by zero is not allowed.")