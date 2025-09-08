# string built in functions..........
# 1.slicing()
s1 = (1,2,3,4,5)
print(s1[0:2:1])

# concentation()
s1 = 'hii'
s2 = 'hello'
print(s1 + s2)
# repetition()
s1 = "hello"
print(s1 * 2)
# strip()
s1 = " hello world  "
print(s1.strip())
# lower()
s1 = "HELLO world"
print(s1.lower())
# upper()
s1 = "hello WORLD"
print(s1.upper())
# find()
s1 = "hello world"
print(s1.find("hello"))
print(s1.find("hellor"))
# replace()
s1 = "i love python"
print(s1.replace("python","coding"))
# split()
s1 = ('a,b,c')
print(s1.split(','))
# join()
s1 = "h","e","l","l","o"
print(",".join(s1))
# startswith()
s1 = "hello world"
print(s1.startswith("hello"))
# endswith()
s1 = "hello world"
print(s1.endswith("rld"))
print(s1.endswith("dlr"))

# count()
s1 = "bananana"
print(s1.count("na"))

# set buit in functions()
# add()
s1 = {1,2,3}
s1.add(5)
print(s1)
# remove()
s1 = {1,2,3,4}
s1.remove(4)
print(s1)
# s1.remove(6)# it throws the error
# print(s1)
# discard()
s1 = {1,2,3,4}
s1.discard(4)
print(s1)
s1.discard(6) # it doesnot throw the error
print(s1)
# pop()
s1 = {1,2,3}
print(s1.pop())
# clear()
s1 = {1,2}
print(s1.clear())
# union()
s1 = {1,2,3}
s2 = {1,2}
print(s1.union(s2))
print(s2.union(s1))
# intersection()
s1 = {1,2,3}
s2 = {1,2}
print(s1.intersection(s2))
# difference()
s1 = {1,2,3}
s2 = {1,2}
print(s1.difference(s2))
# symmetric difference()
s1 = {1,2,3}
s2 = {2,3}
print(s1.symmetric_difference(s2))
# issubset()
s1 = {1,2,3}
s2 = {2,3}
print(s1.issubset(s2))
# issuperset()
s1 = {1,2,3}
s2 = {2,3}
print(s1.issuperset(s2))
# isdisjointset()
s1 = {1,2,3}
s2 = {2,3}
print(s1.isdisjoint(s2))
