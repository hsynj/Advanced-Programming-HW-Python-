str1 = input("Please enter first string-> ")
str2 = input("Please enter second string-> ")

max_length = 0

for i in range(len(str1)):
    for j in range(len(str2)):
        length = 0
        while i + length < len(str1) and j + length < len(str2) and str1[i + length] == str2[j + length]:
            length += 1
        max_length = max(max_length, length)

print(max_length)