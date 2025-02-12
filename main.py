""" Strings Problems """
import copy
import shlex

# Checking Alphabet
# string1 = "Ha@r)(un"
# def remove_char(string1):
#     string2 = str()
#     string3 = str(string1)
#     print(string3)
#     for i in string1:
#         if 65 <= ord(i) <= 90 or 97 <= ord(i) <= 122:
#             string2 = string2 + i
#         else:
#             print(f'removing {i} -> {string1}')
#     return string2
#
# print(remove_char(string1))

# Removing white spaces from the string
# string1 = " Har un K     umar Milind Bansode "
# print(string1)
# string2 = str()
# for i in string1:
#     if i == " ":
#         continue
#     string2 = string2 + i
# print(string2)

# string1 = " Har un K     umar Milind Bansode "
# string1 = "".join(string1.split())
# print(string1)

# exp = "(a-b)+[c*d]+{e/f}"
# pop1 = ['(', ')', '{', '}', '[', ']']
# exp1 = str()
# for i in exp:
#     print(i)
#     if i in pop1:
#         continue
#     exp1 = exp1 + i
# print(exp1)

# Exp = "(a-b)+[c*d]+{e/f}"
# # initialize an empty string
# Equation = ''
# # traversing through string
# for i in Exp:
#     # checking for brackets
#     if ord(i) == 41 or ord(i) == 40 or ord(i) == 91 or ord(i) == 93 or ord(i) == 123 or ord(i) == 125:
#         # If True
#         pass
#     else:
#         # if False
#         # add it to empty String
#         Equation = Equation + i
# # print the string
# print(' String without bracket is ' + Equation)

# Checking number and sum the number
# word = "4PREP2INSTAA6"
# num = 0
# for i in word:
#     if i.isalpha():
#         pass
#     else:
#         num += int(i)
# print(num)

# word = "harun"
# word1 = str()
# for i in range(0, len(word)):
#     if i == 0 or i == int(len(word)-1):
#         word1 = word1 + word[i].upper()
#     else:
#         word1 = word1 + word[i]
# print(word1)
#
# word = "harun"
# word1 = word[0:1].upper() + word[1:len(word) - 1] + word[len(word) - 1: len(word)].upper()
# print(word1)

# string = "YOLO LIFE"
#
# res = {}
#
# for key in string:
#     # if item doesn't exist res.get(key, 0) returns 0 as result
#     # we use res.get(key, 0) + 1 so as to initialize value as 1 on first occurrence
#     # if item exits then res.get(key, 0) + 1 just increments the previously held value
#     res[key] = res.get(key, 0) + 1
#
# # printing result
# print (res)

# from collections import Counter
# string = "Yolo Life"
#
# output = Counter(string)
#
# print(output)


# dict1 = {}
# word = "aaabbc"
#
# for i in word:
#     dict1[i] = dict1.get(i, 0) + 1
#
# print(dict1)



# dict1 = {}
# word = "aaabbc"
#
# for i in word:
#     if i in dict1:
#         dict1[i] += 1
#     else:
#         dict1[i] = 1
#
# print(dict1)


# dict1 = {}
# word = "aaabbc"
#
# for i in word:
#     if i in dict1:
#         dict1[i] += 1
#     else:
#         dict1[i] = 1
#
# print(dict1)


# word1 = 'maam'
# word2 = 'aamm'
#
# string1 = sorted(word1.lower())
# string2 = sorted(word2.lower())
# print(string1)
# print(string2)
#
# if string1 == string2:
#     print("anagram")
# else:
#     print('Not an anagram')


# string=input("Enter String :\n")
# str1=input("Enter substring which has to be replaced :\n")
# str2=input("Enter substring with which str1 has to be replaced :\n")
# string=string.replace(str1,str2)
# print("String after replacement")
# print(string)

#
# string0 = "Hello World"
# string1 = string0.replace("World", "Python")
# print(string1)


