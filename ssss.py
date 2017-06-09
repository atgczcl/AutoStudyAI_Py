# !/usr/bin/env python 3
# coding=utf-8

# from study import text_get_file_text
# text = text_get_file_text()
#
# dic = {}
# for c in "abcdefghijklmnopqrstuvwxyz":
#     dic[c] = 0
#
# doc = text.lower()
# for c in doc:
#     for char in "abcdefghijklmnopqrstuvwxyz":
#         if c == str(char):
#             dic[str(char)] += 1
#
# for char in "abcdefghijklmnopqrstuvwxyz":
#     perc = 100 * dic[char] / len(text)
#     print("{0} - {1}%".format(char, round(perc, 2)))

def my_func(x, y=7, *args, **kwargs):
    print(x)
    print(y)
    print(args)
    print(kwargs)


my_func(2, 3, 4, 5, 6, a=7, b=8)

for i in range(10):
   if i == 999:
      break
else:
   print("Unbroken 1")

for i in range(10):
   if i == 5:
      break
else:
   print("Unbroken 2")