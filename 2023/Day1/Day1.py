# word = "1abc4"

# words =["1abc2",
# "pqr3stu8vwx",
# "a1b2c3d4e5f",
# "treb7uchet"]

values = {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}
value_keys = values.keys()
# print(value_keys)

def trebuchet_part_one():
    num_list = []
    with open('trebuchet.txt', 'r') as tb:
        for word in tb:
            num_arrs = []
            for text in word:
                if text.isnumeric(): 
                    num_arrs.append(text)
            num_list.append("".join([num_arrs[0], num_arrs[-1]]))
        final_list = [int(num) for num in num_list ]
    
    return sum(final_list)


def trebuchet_part_two():
    num_list = []
    with open('trebuchet_two.txt', 'r') as tb:
        for word in tb:
            for vkey in value_keys:
                if vkey in word:
                    print(vkey)
                    word = word.replace(vkey, values[vkey])
            print(word)
            num_arrs = []
            for text in word:
                if text.isnumeric(): 
                    num_arrs.append(text)
            num_list.append("".join([num_arrs[0], num_arrs[-1]]))
        final_list = [int(num) for num in num_list ]
    
    return sum(final_list)


    

# print(trebuchet_part_one())
print(trebuchet_part_two())