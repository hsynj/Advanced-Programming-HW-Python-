def check(str1, str2):
    if sorted(str1) == sorted(str2):
        return 1
    
    str1_c = set(str1)
    str2_c = set(str2)
    if str1_c == str2_c:
        return 2
    
    if str1_c.issubset(str2_c) and len(str1_c) < len(str2_c):
        return 3
    
    if str2_c.issubset(str1_c) and len(str2_c) < len(str1_c):
        return 4
    
    return 5

str1 = input(" ")
str2 = input(" ")

print(f"=> {check(str1, str2)}")