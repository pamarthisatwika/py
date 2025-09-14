# 1 to 5 tables
# for i in range(1,6):
#     for j in range(1,11):
#         print(i,'x',j,'=',i*j)

# print product of the list

# product = 1
# l1=[1,2,3]
# for n in l1:
#     product *= n
# print( product)
#  print the duplicate numbers
# num1 = [1,1,1,2,3,4,5,5]
# d = []
# u = []
# for i in num1 :
#     if num1.count(i)>1:

#      if i not in d:
#         d.append(i)
#      else : u.append(i)
# print("duplicate :",*d)
# print("unique :",*u)
# # using the dictionary
# num = [1,1,1,2,3,4,5,5]
# duplicate = []
# unique = []
# dictionary = {}
# for i in num:
#    if i not in dictionary:
#       dictionary[i] = 1
#    else:dictionary[i] += 1
#    for i in dictionary:
#       if dictionary[i]>1:
#          duplicate.append(i)
#          unique.append(i)
# print("duplicate:",*duplicate)
# print("unique:",*unique)

# reverse a list
num1 = [1,1,1,4,3,2,5,5]
print(num1[::-1])
#second  method
num1 = [1,1,1,4,3,2,5,5]
i = 0
j = len(num1)-1
while i<j:
    num1[i],num1[j] = num1[j],num1[i]
    j-= 1
    i+= 1
print(num1)
# third method
num1 = [1,1,1,4,3,2,5,5]
rev = []
for i in range(len(num1)-1,-1,-1):
    rev.append(num1[i])
print(rev)

# print smallest and largest elements
l = [100,1000,999,99,9,10]
max = l[0]
min = l[0]
for i in l :
  if i>max:
     max = i
  elif i<min :
     min = i
  print(min,max)
