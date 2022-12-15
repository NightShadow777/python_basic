def first_word(i_string):
    i_string = i_string.replace(".", " ").replace(",", " ")
    new_string = i_string.strip().split()
    return new_string[0]

print(first_word("Hello world"))
print(first_word("greetings, friends"))
print(first_word("don't touch it"))
print(first_word("... and so on ..."))
print(first_word("hi"))
print(first_word("Hello.World"))
print(first_word(" .Hello......World"))

