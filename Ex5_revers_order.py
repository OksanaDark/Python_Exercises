str_1 = input("Write here your First and Last names")


def convert(string):
    li = list(string.split(" "))
    return li


converted_list = convert(str_1)
converted_list.reverse()

print(converted_list)
