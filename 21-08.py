# reverse number

num1 = 1476
str_num1 = str(num1)
print(len(str_num1))
sum = 0

for i in str_num1:
    sum = sum + int(i)

    print(sum)

 # or

num1 = 1476
sum = 0
count = 0
while num1 > 0:
   digit = num1 % 10
   sum += digit
   print (digit) 
   num1 = num1 // 10
   count += 1
   print(count)
   print(sum)