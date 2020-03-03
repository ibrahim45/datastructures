import string

inputstr = "aaabceeedecf"

output = [0]*26


alphabets_hash = dict((i, index) for index, i in enumerate(string.ascii_letters))

for i in inputstr:
    output[alphabets_hash[i]] += 1
alphabets_keys = list(alphabets_hash.keys())
print(output)
for index, i in enumerate(output):
    if i == 1:
        print("first non repeating character is")
        print(alphabets_keys[index])
        break;
