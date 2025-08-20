# num1 = float(input("Enter the first number: "))
# num2 = float(input("Enter the second number: "))
# num3 = float(input("Enter the third number: "))
# if num1 >= num2 and num1 >= num3:
#     greatest = num1
# elif num2 >= num1 and num2 >= num3:
#     greatest = num2
# else:
#     greatest = num3
#     print("The greatest number is:", greatest)


# year = int(input("Enter a year: "))
# if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#     print(year, "is a leap year.")
# else:
#     print(year, "is not a leap year.")

    
# print('leap year') if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0) else print('not leap year')('terintory')



# marks = float(input("Enter the student's marks (0-100): "))

# if 90 <= marks <= 100:
#     grade = "A"
# elif 80 <= marks <= 89:
#     grade = "B"
# elif 70 <= marks <= 79:
#     grade = "C"
# else:
#     grade = "Fail"

# print("The student's grade is:", grade)



# a = float(input("Enter the length of side 1: "))
# b = float(input("Enter the length of side 2: "))
# c = float(input("Enter the length of side 3: "))
# if (a + b > c) and (a + c > b) and (b + c > a):
#     print("The sides form a valid triangle.")
# else:
#     print("The sides do NOT form a valid triangle.")



input_ch = input('enter a character').lower()

def check_char(in_ch):
    if len(in_ch) !=1:
        return 'invalid input'
    
    if in_ch in 'aeiou':
        print('vowels')
    else:
        print('consonent')