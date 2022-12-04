import string
data = input("Ввод: ")

clean_data = data.replace("-", "")
start = min(clean_data)
end = max(clean_data)

letters = string.ascii_letters
s = letters.find(start)
e = letters.find(end)

res = letters[s:e+1]
if not res:
    res = letters[e:s+1]
print(res)

