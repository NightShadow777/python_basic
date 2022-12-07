def say_hi(name, age):
    if name and age:
        result = "Hi. My name is {name} and I'm {age} years old".format(name = str(name), age = str(age))
    else:
        result = "Error!"
    return result

name = input("Name: ")
age = input("Age: " )

say = say_hi(name, age)
print(say)