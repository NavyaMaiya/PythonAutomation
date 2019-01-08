
string1 = '''HiI'mNavya'''
print(len(string1))
for i in range(len(string1)):
    print()
    i=i+1
    print(string1[-i])

print()

for i in range(len(string1)):
    print(string1[i])


print()

print(string1[3:-2])
print("Success")


def reverse(string1):
    str1 = ""
    for i in string1:
        str1 = i + str1
    return str1




print("The original string is:",end="")
print(string1)

print("The reversed string(using loops) is : ", end="")
print(reverse(string1))
string1.capitalize()
print(string1)
s=string1.isalpha()
print(s)
