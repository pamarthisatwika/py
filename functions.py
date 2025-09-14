# map
# def sqaure (x):
#     return x **  2
# print(list(map(lambda a: a**2,[1,2,3,4])))

# # filter
# print(list(filter(lambda x :x % 2 == 0,[1,2,3,4,5])))

# # REDUCE
# print(reduce(lambda a,b : a+b,[1,2,3,4,5]))

# # print reverse number using slicing......
# k = 3
# list1 = [1,2,3,4,5]
# print(list1[0:3])
# print(list1[k:])
# list1 = list1[k:]+ list1[0:3]
# print(list1)

# built- in functions of the list..........
# 1.len(list)
# to get a length of the list
# ex: 
# num1 = [1,2,3,4]
# print(len(num1))
# #2.list.apend
# # to add a element in a list
# # syntax: 
# # list_name.append(value)
# # ex: 
# num1 = [1,2,3,4,5]
# num1.append(6)
# print(num1)
# # 3.list.remove()
# # to remove a value or element from a tuple........
# # syntax:
# # list_name_remove(value)
# # ex:
# # num1 = [1,2,3,4,5]
# # num1.remove(num1)
# # print(num1[2])
# # num1.remove(5)
# # num1.remove() #not defined argument its throw error
# # num1.remove(7) # number not defined
# # 4.list.pop(index)
# # remove or delete a element from a list by using index
# # syntax: list_name.pop(index)        
# #ex:
# num1 = [1,2,3,4,5] 
# num1.pop(2)
# print(num1) # its remove index number
# # 5. list .pop()
# # syntax: list_name.pop()
# num1 = [1,2,3,4,5] 
# num1.pop()
# print(num1) # its remove last index

# # 6.list.extend(iterable_value)
# # to add multiple itearable values in list
# # syntax: list_name.extend(list2)
# # ex:
# num1 = [1,2,3,4,5] 
# num2 = [6,7,8,9]
# num1.extend(num2)
# print(num1)
# # 7.sort()
# # to arrange elements in non decreasing order.......
# # total 9 sorts best usage sort is merge sort
# # syntax: list_name.sort() increasing order
# # syntax: list_name.sort(reverse = true)decreasing order
# # ex:
# num1 = [1,4,2,5,3]
# num1.sort()# it is used for the asscending order
# num1.sort(reverse = True)# it is uesd for the reverse or descending order
# # key parameters of sort():
# num1.sort(key=len)#it is used for length of the input
# num1.sort(key=str.lower) # it is uesd for the print lower letters to upper letters
# print(num1)
# # 8.insert()
# # to add an element in particular position
# # we cannont give first(value,index)
# #syntax: list_name.insert(index,value)
# # ex:
# n1= [1,2,4,5] 
# n1.insert(2,3)
# print(n1)
# # 9. index()
# l1= [1,2,3]
# l1.index()
# # to find particular value
# # # 10.count()
# # to find count of the particular element
# # # 11.copy
# # one list to copy another list
# # if we perform any operations on copied list,it will be effect the original these called as shallow copy.
# list1 = [1,2,3]
# list2 = list1
# print(list1,list2)
# list1.pop()
# print(list1,list2)
# # if we perform any operations on copied list,it wont be effect the original these called as deepcopy.
# # ex:
# import copy
# original = [[1,2,3],[4,5,6]]
# shallow = copy.copy(original)
# shallow[0][0]=99
# print(original,shallow)
# original = [[1,2,3],[4,5,6]]
# deepcopy = copy.deepcopy(original)
# deepcopy[1][0]=55
# print(original,deepcopy)
# #  12.min()
# # to find the minimum element
# #  13.max()
# # to find the maximum element
# # 14.sum()
# # to add two numbers
# # 15.clear()
# # to clear the elements
# # ...................................
# #  dictionary bult in functions:
# # 1. get():
# # to get value of particular key...
# # syntax:
# #  dict.get(key)  o/p: value
# d = {'apple':1,'ball':2,'cat':3,'dog':4}
# print(d.get('dog'))
# # (or)
# # dict.get(key,"output")
# # when key is not in dictionary
# # 2. keys():
# # to get all keys of dict(list).......
# # syntax:
# # dict.key() o/p(keys1,key2.......)
# d = {'apple':1,'ball':2,'cat':3,'dog':4}
# print(list(d.key()))# when we wont use list o/p print like dict_keys(output)
# # 3. values..
# # to get all values of dict(list)
# # syntax:
# #   dict.values() o/p:[value1,value2]
# d = {'apple':1,'ball':2,'cat':3,'dog':4}
# print(list(d.values()))
# # 4. items()
# # to get key value pairs(tupple)
# # syntax:
# # dict_name.items() o/p:(key1,value1,key2,value2.....)
# d = {'apple':1,'ball':2,'cat':3,'dog':4}
# print(list(d.items()))# olp values was tupple
# # 5.update():
# # to add key and value pair to a dictionary
# # syntax:
# # dict.update({key:value})
# d = {'apple':1,'ball':2,'cat':3,'dog':4}
# d.update({'elephant':5})
# print(d)
# # 6.pop()
# #  to delete or remove particular key,value.....
# # syntax:
# #  dict.pop(key)
# d = {'apple':1,'ball':2,'cat':3,'dog':4}
# d.pop('cat')
# print(d)
# # 7.clear():
# # to delete  entire dictionary elements
# # syntax:
# # dict.clear()
# d = {'apple':1,'ball':2,'cat':3,'dog':4}
# d.clear()
# print(d)
# # 8.copy()
# # to copy a dictionary to another variable...........
# # syntax:
# # dict2 = dict.copy()
# d = {'apple':1,'ball':2,'cat':3,'dog':4}
# d2 = d.copy()
# print(d2)
# # 9.from keys()
# # to convert list elemnts as key and to initalize common value to all keys in a dictionary
# # syntax1:
# # d = {}
# # d.fromkeys(list,1)
# # syntax2:
# # d = dict.fromkeys(list1,1)
# list_keys = ['apple','ball']
# d=dict.fromkeys(list_keys)
# print(d)
# # 10.zip():
# # to convert 2 lists as dictionary(key,value pair)
# # syntax:
# # d = dict(zip(list_keys,list_values))
# list_keys = ['apple','ball']
# list_values = [1,2,3]
# d=dict(zip(list_keys,list_values))
# print(d)


# string built in functions
# 1.strip():its remove space from first and last edges
# l1 = ' hi '
# print(l1.strip())
# # 2.lower(): it gives output lower string
# text = "Hello"
# print(text.lower())
# # 3.upper():it gives upper letters output
# text = "HELLO"
# print(text.upper())
# # 4.find(): it gives -ve  index number of the string
# text = "hello, world"
# print(text.find("w"))
# print(text.find('rld',1,9))
# # 5.replace: it replace the string
# text = "i love python"
# print(text.replace("python","coding"))
# # 6.startswith(): it startswith only start strings
# text = "hello"
# print(text.startswith("el"))
# # 7.endswith(): it endswith only end strings
# text = "hello"
# print(text.endswith("lo"))
# print(text.count("l"))
# # 8.count(): it counts the how many strings
# text = "bananana"
# print(text.count("n"))
# print(text.startswith("ba"))
# print(text.endswith("an"))
# # print(text.count())
# # 9.split():its splits the numbers
# text = "a$b,c"
# print(text.split("b"))
# num1,num2,num3 = map(int,input("enter the number of csv mode").split(","))
# print(type(num1),num1)
# # 10.join()
# list1 = ['hi','hello','namasthe']
# print(','.join(list1))
# set built in functions....
# 1.add()
# set = {1,2,3,4,(1,2,3)}
# set.add(9)
# # 2.remove()
# set.remove(1)
# # set.remove(2)
# # 3.discard()
# set.discard(2)
# # clear()
# set.clear()
# # pop()
s1 = {2,3,4,5,(2,3,4)}
s1.pop()
# union()s or we use |
s1 = {1,2}
s2 = {3,4}
print(s1.union(s2))
print(s1|s2)
# intersection() or we use &
s1 = {1,2}
s2 = {3,4}
print(s1.intersection(s2))
# symmetric difference = union set- intersection set or we use "-"
# is subset() and is.superset()
set1 = {1,2,3}
set2 = {1,2,}
print(set1.issuperset(set2))
print(set1.issubset(set2))
# this is for tupple
t1 = (1,2,3,4)
t1 += (5,6)
print(t1)
