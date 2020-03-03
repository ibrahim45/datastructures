input_str = "DBCABA"


letter_counter = {}

for i in input_str:
    if letter_counter.get(i):
        letter_counter[i] += 1
        if letter_counter[i] > 1:
            print("First repeating character is {0}".format(i))
            break;
    else:
        letter_counter[i] = 1

