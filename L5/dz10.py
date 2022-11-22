import string
import keyword
'''
elif data.isupper() or data in string.punctuation:
    print("false")
elif "_" in data:
    print("true")
elif data in keyword.kwlist:
    print("false")
'''


data = str(input("Type string: "))

for char in data:
    if char.isdigit():
        print("false")
