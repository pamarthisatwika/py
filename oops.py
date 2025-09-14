# classe example
class person:
   def __init__(self,name,age):
    self.name = name
    self.age = age
   def greet(self):
      return f"hello, my name is{self.name} and i am {self.age} years old"
person1 = person("satwika",20)

print(person1.greet())


# decrators
def example_decrator(func):
  def wrapper():
    print("hii")
    func()
    print("thank you")
  return wrapper
@ example_decrator
def printer():
  print("my name is satwika")
printer()

