# for i in range (1,101):
#   print (i)


# 2...............
# n = 25
# sum = 0
# for i in range (1,101):
#     sum = sum+i

#     print(sum)
#   (or)

# print((n*(n+1))/2)
# sum of squares............
# ( n(n+1)(2 n+1)/6)


# 3..................
# i= range(1,51)
# while i%2==0:

#     print (i)

# 4........................
# n1=8
# i=1
# while i<=20:
#  print(n1,'x',i,'=',i*n1)
#  i +=1


# 7..................

# while True:
#     num1 = int(input('enter the number'))
#     print(num1)
#     if num1<=0:
#         print('non positive entered')
#         break

# 8..................
# while True :
#     print('1.square 2.cube 3.exit')
#     choice = input('enter the number')

#     if choice == '1' or choice == 'square':
#         input_num = float(input('enter the number or sqaure'))
#         print(input_num **2)

#     if choice == '2' or choice == 'cube':
#         input_num = float(input('enter the number or cube'))
#         print(input_num **3)
#     else:
#         print('no valid option picked')
#         print('existing')
#         break

# reverse number..............
# n1 = -1476
# rev_num = 0
# while n1 > 0:
#    digit = n1 % 10
#    print (digit)
#    rev_num = rev_num * 10 + digit
#    n1 = n1//10
# print(rev_num)

# n1 = -1476
# flag = True
# if n1 < 0:
#    flag = False
#    n1 = n1 * -1 
# rev_num = 0
# while n1 > 0:
#    digit = n1 % 10
#    print (digit)
#    rev_num = rev_num * 10 + digit
#    n1 = n1//10
# print(rev_num)
# if flag:
#    print (rev_num)
# else:
#    print(rev_num * -1)


# prime numbers............
# num1 = 35
# count = 0
# for i in range(1,num1+1):
#    if num1 % i == 0:
#       count += 1

# print('prime') if count == 2 else print('not prime')


# metod2...........

# num1 = 45
# flag = True
# if num1 <= 1:
#    print('not a prime')
# else:
#  for i in range(2,num1):
#     if num1 %i == 0:
#      flag = False
#      print('not a prime')
#      break
# if flag == True:
#    print('it is prime')


# # functions method 3..........
# def check_prime(num1):
#   if num1 <= 1:
#     return 'not a prime'
#   for i in range(2,num1):
#     if num1 % i == 0:
#       return 'not a prime'
#   return  'prime'

# print(check_prime(7))
# # method 4...........
# def check_prime(num1):
#   if num1 <= 1:
#     return 'not a prime'
#   for i in range(2,num1 // 2 + 1):
#     if num1 % i == 0:
#       return 'not a prime'
#   return  'prime'

# print(check_prime(7))

# # method 5.................
# def check_prime(num1):
#   if num1 <= 1:
#     return 'not a prime'
#   for i in range(2,int(num1 ** 0.5)+1):
#     if num1 % i == 0:
#       return 'not a prime'
#   return  'prime'

# print(check_prime(7))

# # armsrong number
# # 153 => 1+25+27=153 armstrong
# # 1642=>1+1296+256+16=1596 not armstrong
# # not use strings.........
# num1 = 153
# dup_num1 = num1
# count = 0
# while num1 > 0:
#      count += 1
#      num1 = num1 // 10
# print(count)
# num1 = dup_num1
# sum = 0
# while num1 > 0:
#   digit = num1 % 10
#   print(digit)
#   sum += digit ** count
#   num1 = num1 // 10
  
# num1 = dup_num1
# if sum == num1:
#   print('armstrong')
# else:
#   print('not armstrong')

# # use strings.........
# num1 = 153
# dup_num1 = num1
# count = len(str(num1))

# print(count)
# num1 = dup_num1
# sum = 0
# while num1 > 0:
#   digit = num1 % 10
#   print(digit)
#   sum += digit ** count
#   num1 = num1 // 10
  
# num1 = dup_num1
# if sum == num1:
#   print('armstrong')
# else:
#   print('not armstrong')

# # swap.............
# # method1.......
# num1 = 10
# num2 = 20
# num1,num2 = num2,num1
# # method 2 => using third variable
# num1 = 10
# num2 = 20
# temp = num2
# num2 = num1
# num1 = temp
# # method 3..........
# num1 = 10
# num2 = 20
# num1 = num1 + num2
# num2 = num1 - num2
# num1 = num1 - num2

# # method 4 # using xor
# # when you xor two same numbers ouput was zero
# # when you xor one number with zero then you  get same number
# num1 = 10
# num2 = 20
# num1 = num1 ^ num2 # (10 ^ 20)
# num2 = num1 ^ num2 # (10 ^ 20) ^ 20 # 10 ^ 0 # 10
# num1 = num1 ^ num2 # (10 ^ 20) ^ 10 # 0 ^ 20 # 20

# #  every number twise except one finf that odd one
# list1 = [1,1,2,2,3,3,4,4,5,5,6,6]
# res = 0
# for i in list1:
#   res = res ^ i
#   print(res)

# fibnocci number
# 0,1 
# fib(n) = fib(n-1) + fib(n-2)

num1, num2 = 0,1
n = 10
for i in range (n):
   temp = num1 + num2
   print(num1)
   num1 = num2
   num2 = temp
   
#  not using third variable......
num1, num2 = 0,1
n = 10
for i in range(n):
   print(num1)
   num1,num2 = num2, num1 + num2

# perfect number means take a number  all the factors of that number add factors and get some number
num1 = 6
sum = 0
for i in range(1,num1):
     if num1 % i == 0:
        sum = sum + i   
if sum == num1:
   print(num1,'it is a perfect number')
else:
   print('not a perfect number')

# scope is also called as lifetime
num1 = 10
def test_function():
   num1 = 20
   def inner_function():
      num1 = 45
      print(num1)
   inner_function()
   print(num1)

test_function()
print(num1)

#  only change num1
num1 = 10
def test_function():
   global num1
   num1 = 20
   print(num1)

test_function()
print(num1)
#   (or)
num1 = 10
def test_function():
   global num1
   num1 = 20
   globals()['num1'] = 50
   print(num1)

test_function()
print(num1)

# local, global want then the code was
num1 = 10
def test_function():
  
   num1 = 20
   globals()['num1'] = 50
   print(num1)

test_function()
print(num1)

# nonlocal
num1 = 10
def test_function():
   num2 = 20
   def inner_function():
      nonlocal num2
      num2 = 45
      print(num2)
   inner_function()
   print(num2)

test_function()
print(num1)
