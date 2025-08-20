while True :
    print('1.addition 2.subtraction 3.multiplication 4.divison')
    choice = input('enter the number')

    if choice == '1' or choice == 'addition':
        input_num1 = float(input('enter the number'))
        input_num2 = float(input('enter the number'))
        print(input_num1+input_num2)

    elif choice == '2' or choice == 'subtraction':
        input_num1 = float(input('enter the number'))
        input_num2 = float(input('enter the number'))
        print(input_num1-input_num2)
    elif choice == '2' or choice == 'multiplication':
        input_num1 = float(input('enter the number'))
        input_num2 = float(input('enter the number'))
        print(input_num1*input_num2)

    elif choice == '2' or choice == 'division':
        input_num1 = float(input('enter the number'))
        input_num2 = float(input('enter the number'))
        print(input_num1/input_num2)


    else:
        print('no valid option picked')
        print('existing')
        break

    # factorial using while loop
    n = int(input("Enter a number: "))
    fact = 1
    i = 1
while i <= n:
    fact *= i
    i += 1
print(f"Factorial of {n} is: {fact}")

# 1 to 100 divisible by 3 and 5 using loop
for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print(i)

# login system
correct_password = "python123"
attempts = 3
while attempts:
    password = input("Enter password: ")
    if password == correct_password:
        print("Login successful ")
        break
    attempts -= 1
if attempts == 0:
    print("Account locked ")