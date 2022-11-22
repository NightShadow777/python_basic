import string
data = str(input("Type string: "))
res_list = []
for symbol in string.punctuation:
    if symbol in data:
        data = data.replace(symbol, " ")

data = data.split()
for word in data:
    res_list.extend(word.strip().title())
    result = "".join(res_list)

if len(result) > 140:
    new_result = result[:140-1]
    print("#{}".format(new_result))
else:
    print("#{}".format(result))