# num1=5
# num2=3
# if num1%5==0 and num2%3==0:
#     print('it is multiple')
# else:
#     print('it is not multiple')

# num1=-1
# if num1>0:
#   print('it is positive')
# else:
#  if num1==0:
#   print('it is zero')
#  else:
#     if num1==-1:
#       print('it is negative 1')
#     else:
#       print('it is negative')

# num1=15
# if num1%15==0:
#     print('it is buzz')
# elif num1%5==0:
#     print('it is prebuzz')
# elif num1%3==0:
#     print('it is fizzbuzz')
# else:
#     print('it is not buzz')

# units=int(input('enetr the number'))
# if units>=300:

#     print(units*5)
# else:
#    if  units>=200:
#      print(units*3)
#    else: 
#       if units>=100:
#        print(units*2)
#       else:
#          print('it is not elecrticity')
       
# num1=int(input('enter the number'))
# num2=int(input('enter the number'))
# op=input('enter the operator')
# if op=='+':
#     print(num1+ num2)
# else:
#     if op=='-':
#         print(num1-num2)
#     else:
#         if op=='*':
#             print(num1*num2)
#         else:
#             if op=='/':
#                 print(num1//num2)

#             else:
#                 print('it is other operator')

# loop example:
# for loop
# for i in range(1,101):
#     print(i)
#     print('sorry sasi')
# n=100
# for i in range(1,n+1):
 
#  if i%2==0:
#   print(i)

# for num1 in range(1,101):
  
#   if num1%15==0:
#    print('it is fizzbuzz')
#   elif num1%5==0:
#     print('it is buzz')
#   elif num1%3==0:
#     print('it is fizz')
#   else:
#     print('it is not buzz')

# str1='happy birthday'
# for i in str1:
#  if i in('aeiou'):
    
#   print('it is ovels')
# if i not in ('aeiou'):
#    print ('it is not ovel')

#while loop:
# num1=10
# while num1<20:
#     print('hii')
#     print(num1)
#     num1 +=1

# num1=1
# while num1<=100:
    
#     print(num1)
#     num1 +=1
   
# else:
#     print('execution ended')

# num1=1
# while num1<=100:
     
#      print(num1)
#      num1 +=2

# n1=(17)
# for i in range(1,21):
#  print(n1,'x',i,'=',n1*i)

# n1=17
# i=1
# while i<=20:
#  print(n1,'x',i,'=',i*n1)
#  i +=1


for class_no in range(1,11):
  print(class_no,'class')
  for roll_no in range(1,31):
     print('class',class_no,'rollno',roll_no)
