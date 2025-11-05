inp = open("1.txt", 'r')
oup = open("2.txt", 'w')

FOR_CONVERT = 'DLRGFAUOWPEZNXHTMYIBJKVQSC'
def convert(my_str):
    convert_str = ""
    for c in my_str:
        if 'a' <= c <= 'z':
            a = ord(c) - 97
            convert_str += FOR_CONVERT[a]
        else:
            convert_str += c
    return convert_str
        
def un_convert(convert_str):
    my_str = ""
    for c in convert_str:
        if c in FOR_CONVERT:
            a = FOR_CONVERT.index(c) + 97
            my_str += chr(a)
        else:
            my_str += c
    return my_str

my_str = inp.read()
a = convert(my_str)
b = un_convert(a)
oup.write(f"Converted:\n{a}\nUn Converted:\n{b}")
print("Success!!")
inp.close()
oup.close()
