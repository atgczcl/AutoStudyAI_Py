#!/usr/bin/env python
# coding=utf-8

abc = "你好!Hello Python3 world! I love YOU!"

'''
i = 0
while i+1 < 30:
    print(abc)
    i += 2
print('aaa')
'''


# i = 3
# while i >= 0:
#     print i
#     i = i - 1
# while 1 == 1:
#     print "in the loop"

words = ["spam", "egg", "spam", "sausage"]
# print("spam" in words)
# print("egg" in words)
# print("tomato" in words)

nums = [1, 23, 2342, 88, 1, ]
# print nums
# print 0 in nums
# print 0 in words
# print not 0 in nums
# print not 1 in nums
# print 1 not in nums
# print 0 not in nums
# rollBall = (2, 3, 4)
# print rollBall
# print len(rollBall)
# print nums.count(1)
# nums.append(77)
# print nums
# try:
#     print nums.index(2)
# except:
#     print "not exists"
# print "ok world"
nums = set(range(100))
# print nums
nums = list(range(3, 800, 100))
# print nums
# counter = 0;
# while counter < nums.__len__():
#     print nums[counter]
#     counter += 1
#
# for i in range(5):
#     print ("hello!="+str(i))
#


# 定义一个funcion
def my_func():
    for i in nums:
        if 3 in nums:
            print("99 in list nums")
    for i in range(10):
        if not i%2 == 0:
            print(i+1)
my_func()
print("spam\n" * 3)
# user_info() 定义在前，使用在后，没有定义就去使用就会出错
# 测试函数型输入


def user_info():
    age = input("age?")
    name = input("name?")
    address = input("address?")
    zipcode = input("what's your zipcode?")
# print user_info()


def user1_info():
    age = input("What's your age?")
    name = input("what's your name?")
    address = input("whats your address?")
    zipcode = input("what's your zipcode?")
# print(user1_info())


# 函数定义保持两个空行，保持代码清晰
# '#'开头的话留一个空格，看起来很舒服
def num_get_max(xStr, yStr):
    if xStr > yStr:
        return yStr
    else:
        return xStr
# x = (input("Enter the first value:"))
# y = (input("Enter the first value:"))
# print 'great = ', max(x, y)


def shout(str_say):
    """
    Print a word with an exclamation mark following it;
    :param str_say: 
    :return: 
    """
    print(str_say + "!")
shout("spam")
print(shout.__doc__)

# 引入模块一般写在文件最上面
# from math import pi
import math as mm
print(mm.pi)

# print range(3)
def sum_num(number):
    result = 0
    for index in range(number):
        result += index
        print(result)
    return result;
# print sum_num(3)
from random import randint
print(randint(6, 34))


# 异常处理列子
try:
    print(45/2)
except(ZeroDivisionError):
    print("ok i know")
    # print(e)
else:
    print("fucking good job@")
finally:
    print("\133 Bitch you are not going away! hhhhhhaaaaaa!")
# 测试raise处理异常，主动抛出异常
# print 99/0
# try:
#     print 99/0
# except:
#     raise
# print 1
# raise ValueError("adsfadfasdf")
# print 2


# 特殊异常断言处理，为真不抛异常，假抛出异常
# assert 2 + 2 == 6, "fuck bitch man you not good!"
# assert 2 + 2 == 4, "fuck bitch women you not good!"
# print "asdfsdf"

# 测试with 阅读语句
# with open("./study.py") as my_file:
#     print my_file.mode
#     for line in my_file:
#         print line

# 三元组异常(异常类，异常类的实例，跟中记录对象)
# try:
#     1/0
# except:
#     import sys
#     tuple = sys.exc_info()
#     print tuple

# r+, w+, a+ append
def save_to_file(name, data):
    """
    保存数据到文件呀
    :param name:
    :param data:
    :return:
    """
    with open(name, "a+") as file_:
        amount_writen = file_.write(data)
        print(type(amount_writen))
        print("write len =" + str(amount_writen))
        print("read=" + file_.read(3))
        # 如果使用with打开文件，在with结束的时候回自动关闭文件，无需开发者关闭
        # file_.close()
    with open(name, "r") as myFile:
        # print(myFile.read())
        print(myFile.read(1))
        print(myFile.read(2))
        print(myFile.read(4))
        print(myFile.read(7))
        # print myFile.read()
        # # no close()  re-read()是空的
        # print "re-reading=" + myFile.read()

        # 数组方式读出
        print(myFile.readlines())
        # myFile.close()
    # 立马就会清空文件，fucking bad!
    # with open(name, "w") as myFile:
    #     myFile.close()
save_to_file("./sss.py", "print('abc')\n")

# 动态生成一个Python执行文件然后执行它，自动生成可执行代码
import ssss
ssss

import os
print(os.path.exists("./sss.py"))
if os.path.exists(""):
    print("exist sss.py")
# with open("unknow.txt", "r") as f:
#     print(f.read())

None
print(None)


bad_dict = {
    1: "one two three, i love it!",
    3:3,
    7:78878,
    8:[90, 78, 0, 5]
}
print(bad_dict)
good = (23, 23,43,34,54,45)
print(good)
bad = [23, 33,4, 34, 34]
bad.append("adsfasfas")
print(bad)
print(2 in bad_dict)
if 1 in bad_dict:
    print(bad_dict[1])
# in or not in可以用来判断一个字典里面是否存在这个key
print(78878 not in bad_dict)
print(bad_dict[8])
print(bad_dict.get(2))

my_tuple_test_list = "one", "two", "three"
print(my_tuple_test_list[2])
print(my_tuple_test_list)


playerListId = list(range(17))
# tuple不可以改变
playerListId = tuple(range(17))
print(playerListId[4])
assert "--------------------------"
# 闭开区间，playerListId[3],不会添加进去,三元组是一种间隔获取方式
print(playerListId[::2])
print(playerListId[0:3])
# 这个不会旋转列表
print(playerListId[:-1])
# 这样会旋转这个list
print(playerListId[::-1])
print(playerListId[1:1])
print(len(playerListId))

# 逆向
print(playerListId[15:7:-1])
# 一二参数也要逆向
print(playerListId[7:15:-1])
# 正向第一个大了，列表为空，
print(playerListId[15:7:1])

# a list comprehension
cubes = [i**3 for i in range(5)]
print(cubes)
evens = [i**2 for i in range(10) if i**2 % 2 == 0]
print(evens)

# 可以进行数组匹配，也就是重复数字
msg = "Numbers:{0}{1}{2}[00000]".format(evens[0], evens[1], evens[2])
print(msg)
print("{good}, {bitch}".format(good="ok world", bitch="unbelievable!"))

print(all(evens))
if all(i > -2 for i in evens):
    print("All Larger than 5")
# for v in enumerate(evens):
#     print(v)

print(enumerate([evens]))

def text_get_file_text():
    """
    动态读取文件获取文件内容
    :return: 
    """
    filename = input("Enter a fileName:")
    with open(filename) as f:
        return f.read()

# Text Analiyzer
def count_char(text, char):
    """ 计数指定文件的数量 """
    count = 0
    for tempChar in text:
        if tempChar == char:
            count += 1

    return count

# print(count_char(text_get_file_text(), "r"))
# print(text_get_file_text().count("r"))

def test_text_count():

    text = text_get_file_text().lower()
    totalPerc = 0
    for char in "abcdefghijklmnopqrstuvwxyz":
        perc = 100 * count_char(text, char)/len(text)
        # i know round函数是进行数字格式化
        totalPerc += round(perc, 2)
        print("{0}->{1}".format(char, round(perc, 2)))
    print("字母占有百分比是：{0}".format(totalPerc))

    print(text[-1::])
print(evens[:2])

nums = (55, 44, 33, 22)
print(max(min(nums[:2]), abs(-42)))

import random
print(random.random())

def my_func(f, arg):
    return f(arg)
# print(my_func(lambda x: 2*x*x, 5))

# 可以支持双函数
print((lambda x, y: x**2 + 5*y + 4)(-4, 8))
# lambda表达式变量，
multiple_two = lambda x: x * 2
print(multiple_two(7))

nums = (11, 22,33,44,55)

# 每个元素 *2
print(list(map(lambda x: x*2, nums)))
# 保留小于22的所有元素
print(list(filter(lambda x: x < 22, nums)))


def countdown():
    i = 5
    while i > 0:
        yield i
        print(">", i)
        i -= 0.5

import time
for tmpValue in countdown():
    print("==", tmpValue)

# def get_primes():
#     num = 2
#     while True:
#         if num // 2+1:
#             yield num
#         num += 1
# for tmpNum in get_primes():
#     print(tmpNum)
print(list([x*3 for x in "spam"]))


def make_word():
    print()
    word = ""
    for ch in "spam":
        word += ch
        yield word

# print(list(make_word()))


# Decorators 函数加壳,改变原有函数
def decorrrr(func):
    def wrap():
        print("------------")
        func()
        print("------------")
    # 不要写错 wrap()不是调用，函数传参数只用函数名
    return wrap


"""
decorators可以用@xxx来代替，这样更加方便
"""
@decorrrr
def print_text():
    print("Hello world!")
# 不要写错 wrap()不是调用，函数传参数只用函数名
# de = decorrrr(print_text)
# de()
# print_text()


def decor(func):
    def wrap():
        print("============")
        func()
        print("============")
    return wrap


def decor1(func):
    def wrap1():
        print("**************")
        func()
        print("**************")
    return wrap1


@decor
@decor1
@decor1
def print_text():
    """
    内部嵌套decorators测试
    :return: 
    """
    print("Hello world!")

print_text()


# decorators测试，显示他的作用
def basic(func):
 def modified():
  x=int(input(':'))
  y=int(input(':'))
  func(x,y)
 return modified

@basic
def ad(x,y):
 print("add=", x+y)

@basic
def prd(x,y):
 print("mult=", x*y)

@basic
def diff(x,y):
 print("div=", x-y)

# ad()
# prd()
# diff()


count_recursion = 0


# Recursion递归测试, 求x的阶乘
def factorial(num_x):
    # 为假的时候才会抛异常，为真不抛出异常
    assert (num_x > 0), "必须大于0"
    # 主动抛出异常
    # raise(num_x >= 0, "asdfasdff")

    global count_recursion
    count_recursion += 1
    print(count_recursion)
    if count_recursion > 1003:
        return 1
    if num_x == 1:
        return 1
    else:
        return num_x*factorial(num_x - 1)

# print(factorial(500))
# print(factorial(0))


def is_even(x):
    print("even=", x)
    if x == 0:
        return True
    else:
        return is_odd(x-1)

def is_odd(x):
    print("odd=", x)
    return not is_even(x)


# print(is_odd(7))
# print(is_even(23))

# 递归求和
def fib(x):
    tmp_sum = 0
    if x == 0 or x == 1:
        return 1
    else:
        # print("x={0}|{1}".format(x, tmp_sum))
        tmp_sum = fib(x - 1) + fib(x - 2)
        print("x={0}|{1}".format(x, tmp_sum))
        return tmp_sum
print(fib(4))

# 集合和运算, 集合元素不能重复
set_a = set('abcc')
print(set_a)
set_b = set('bcdef')
set_c = set("boy")
# print(set("boy"))
print(set_a & set_b & set_c)
print(set_a | set_b & set_c)
# 求差集，减去相同的留下不同的，补集
print("a-b=", set_a - set_b)
# print(set_a.pop())
# print(set_a.pop())
# print(set_a.pop())
# 异或 = 求不同的
print(set_a^set_b)

# count从某个值开始算起
from itertools import count
from itertools import cycle
for i in count(3):
    print(i)
    if i >= 11:
        break
# print(list(cycle("sss", 5)))


# x=1,2,3
# for i in count(3):
#     for n in x:
#         print (x)
#         cycle(x)
#     print(i)
#     if i >=11:
#         break

from itertools import takewhile
nums = [2,4,6,7,9,8]
aa = list(takewhile(lambda x: x % 2 == 0, nums))
print(aa)
# [2, 4, 6] takewhile != while, takewhile会在不满足条件的时候自动中断
aa = list(x for x in nums if x % 2 == 0)
aa = list(map(lambda x: x % 2 == 0, nums))
print(aa)
aa = list(filter(lambda x: x % 2 == 0, nums))
print(aa)
# [2, 4, 6, 8]

from itertools import *
# 排列组合，combinations组合, permutations排列, product乘机
letters = ("A", "B", "x")
print(list(product(letters, range(2))))
print(list(permutations(letters, 1)))

# print(list(permutations((1,2,3))))
# print('============================')
# print(list(product((1,2,3),range(2))))
# print('+++++++++++++++++++++++++++++++')
# print(list(combinations((1,2,3,4,5),3)))

print(list(range(3)))

# 递归求幂运算
def power(x, y):
  if y == 0:
    return 1
  else:
    return x * power(x, y-1)

print(power(2, 3))

a=(lambda x:x*(x+1))(6)
print(a)

import sys
sys.stdout.write("asdfa\n")


# python定义类
class Cat:
    dig = 99

    def __init__(self, color, legs):
        self.color = color
        self.legs = legs
        self.dig = legs

    # def __init__(self):
    #     self.aa = 0

    def tostring(self):
        print(self.color+"|", self.legs, )

felix = Cat("ginger", 4)
felix.tostring()

# felix.dig = 1
Cat.dig = 0
print(felix.dig)
print(Cat.dig)
# print("end", end="\s", file=sys.stderr, flush=True)
# print("aaaaaa")
class Tigger(Cat):

    def attack(self):
        print("Beat it!")
        self.tostring()
        return 8
my_tigger = Tigger("yellow", 4)
my_tigger.tostring()
print(my_tigger.attack())


# magic methods python的魔术函数操作
class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __mul__(self, other):
        return Vector2D(self.x * other.x, self.y * other.y)
    """def __mult__(self,other): #this gives an error because "*" is associated with default name mul and not mult#
        return Vector2D"""
    def __add__(self,other):
        return Vector2D(self.x+other.x,self.y+other.y)

first = Vector2D(5, 7)
second = Vector2D(3, 9)
result = first + second
result1 = first * second
print(result1.x)
print(result1.y)
print(result.x)
print(result.y)

# __sub__ for -
# __mul__ for *
# __truediv__ for /
# __floordiv__ for //
# __mod__ for %
# __pow__ for **
# __and__ for &
# __xor__ for ^
# __or__ for |


class SpecialString:
    def __init__(self, content):
        self.content = content

    def __truediv__(self, other):
        line = len(other.content) * "="
        return "\n".join([self.content, line, other.content])

    def __add__(self, other):
        return self.content + other.content

spam = SpecialString("spam")
hello = SpecialString("Hello world!")

print(spam/hello)

# join是联合，连接的意思，cc-》bb-》ff， 连接成一个长的string
print("-》".join(["cc", "bb", "ff"]))
# print(spam.cmp(hello))
# print(spam + hello)

# if spam > hello:
#     print("da大")

class SpecialString:
    def __init__(self, cont):
        self.cont = cont

    def __gt__(self, other):
        for index in range(len(other.cont)+1):
            result = other.cont[:index] + ">" + self.cont
            result += ">" + other.cont[index:]
            print(result)

    def _testPrivateMethod(self):
        print("I am private!")


spam = SpecialString("spam")
eggs = SpecialString("eggs")
# spam > eggs
print(spam.__str__())
print(spam._testPrivateMethod())

a = 42  # Create object <42>
b = a  # Increase ref. count  of <42>
c = [a]  # Increase ref. count  of <42>

del a  # Decrease ref. count  of <42>
# b = 100  # Decrease ref. count  of <42>
# c[0] = -1  # Decrease ref. count  of <42>
print(b)
xx = 90/45


class ClassMethod:
    def __init__(self, cls):
        print("From Other class method!")


class Queue:
    inner_per = 99
    def __init__(self, contents):
        self._hiddenlist = list(contents)

    def push(self, value):
        self._hiddenlist.insert(0, value)

    def pop(self):
        return self._hiddenlist.pop(-1)

    def __repr__(self):
        return "Queue({})".format(self._hiddenlist)

    @property
    def myMethod(self):
        print("My method!=")

    # @property  # read-only 只读的
    @myMethod.setter
    def testMethod(self):
        self.myMethod = "9999999"
        print("Inner Class method!")
        return False

    def __testPrivateMethod(self):
        print("I am private!")

    # 测试类函数, 简单说就是静态函数
    @classmethod
    # @Classmethod
    def testClassMethod(cls):
        print("Class method bingo!!")

    @staticmethod
    def testStaticMethod():
        print("static method")



queue = Queue([1, 2, 3])
print(queue)
queue.push(0)
print(queue)
queue.pop()
print(queue)
queue._hiddenlist[0]=77
print(queue._hiddenlist)
# 私有方法可以通过 下划线+类名+函数名进行访问
queue._Queue__testPrivateMethod()
# queue.__testPrivateMethod()  # 类的私有函数不能通过这种方式访问
Queue.testClassMethod()  # 类的静态函数

print(queue.testMethod)
# queue.testMethod = 0  # read-only 属性不能更改


# class Pizza:
#   def __init__(self, toppings):
#     self.toppings = toppings
#     self._pineapple_allowed = False
#
#   @property
#   def pineapple_allowed(self):
#     return self._pineapple_allowed
#
#   @pineapple_allowed.setter
#   def pineapple_allowed(self, value):
#     if value:
#       password = input("Enter the password: ")
#       if password == "Sw0rdf1sh!":
#         self._pineapple_allowed = value
#       else:
#         raise ValueError("Alert! Intruder!")
#
# pizza = Pizza(["cheese", "tomato"])
# print(pizza.pineapple_allowed)
# pizza.pineapple_allowed = True
# print(pizza.pineapple_allowed)


# def get_input():
#     commands = input("input cmd: ").split()
#     verb_word = commands[0]
#     if verb_word.lower() in action_dict:
#         verb = action_dict[verb_word]
#     else:
#         print(("Unknow ver {}".format(verb_word)))
#         return
#
#     if len(commands) >= 2:
#         noun_word = commands[1]
#         print(verb(noun_word))
#     else:
#         print(verb("nothing"))
#
#
# def say(noun):
#     return "You said {}".format(noun)
#
#
# action_dict = {
#     "say": say,
#     "good": say,
# }
#
# while True:
#     get_input()

import re, pathlib

pattern = r"spam"
print(re.match(pattern, "spamspamspam"))
print(pathlib.PurePath('a/b.py').match('*.py'))

print(pathlib.PurePath('./ssss.py'))
str_words = "eggspameggspameggspameggspameggspam"
if re.match(pattern, str_words):
    print("Match")
else:
    print("No match")

if re.search(pattern, str_words):
    print("Searched")
else:
    print("No match")

if re.findall(pattern, str_words):
    print("Findalled")
else:
    print("No match")

print(re.findall(pattern, str_words))

search_match = re.search(pattern, str_words)
if search_match:
    print(search_match.group())
    print(search_match.start())
    print(search_match.end())
    print(search_match.span())

pattern = r"^gr.y$"  # ^以什么开始，$以什么结尾
pattern = r"[aeiou]"  # [xxx],包含[]内的任何一个字符即可
pattern = r"[ae][iou]"  # [xxx][xx],包含[][]内的任何一个字符拼凑的字符串，比如ai
pattern = r"[0-9]"  # 搜索包含0-9的数字
pattern = r"[A-Za-z]"  # 搜索包含所有大小写英文字符
pattern = r"[A-Z]"  # 搜索包含所有大小写英文字符, match模式以大写字母开头
pattern = r"[A-Z][A-Z][0-9]"  #  match模式以 两个大写字母+ 一个数字开头
pattern = r"[^A-Z]"  # 不包含大写字符的任何字符，取反
pattern = r"[^0-9]"  # 不包含大写字符的任何字符，取反
pattern = r"egg(spam)*"  # 开始 与egg, 包含0个spam 以上额 spam, * 号不限长度

# *	匹配前面的子表达式零次或多次。例如，zo* 能匹配 "z" 以及 "zoo"。* 等价于{0,}。
pattern = r"sppam*"  # 开始 与egg, 包含0个spam 以上额 spam, * 号不限长度 egg 这里等价于eg
pattern = r"(42)+$"  # 一个或多个g， match就是 g+ 开头
pattern = r"ice(-)?cream"  # ?意思是零个或一个对应的匹配字符(-),
pattern = r"9{1,3}$"  # "9{1,3}$" matches string that have 1 to 3 nines.
pattern = r"g+"  # 一个或多个g， match就是 g+ 开头, * 表示0个以及以上
pattern = r"a(bc)(de)(f(g)h)i"  # groups
pattern = r"(?P<first>abc)(?:def)(ghi)"  # group命名first, Non-capturing groups (?:xx)不能进行group获取，隐藏了
pattern = r"gr(a|e)y"  # |= a或e, 不包括ae
pattern = r"(.+) \1"  # (.+)代表一个或多个字符， \1表示重复第一组的内容，也就是重复2次第一group, 当然\1前面还有一个空格
# pattern = r"(.+)(.+)"  # (.+)代表一个或多个字符， \1表示重复第一组的内容，也就是重复2次第一group
pattern = r"(\D+\d)"  # \d,\s 和\w === 数字，空格，任意字符， \D，\S,\W表示和小写相反，不是数字，不是空格，不是字母
pattern = r"[1-6!]"  # 含有1到6的数字和感叹号 其中任何一个
pattern = r"(\d*\w)+"  # 1个或多个的（0个或多个数字和字符的拼接组），
pattern = r"(\D+\s?)+"  # 1个或多个的 (1或多个非数字和0-1个空格的拼接组)
pattern = r"\b(cat)\b"  # \b是特殊字符包裹起来的字符匹配(单词边界)中文符号,英文符号,空格,制表符,换行
pattern = r"\B(cat)\B"  # \B是非特殊字符边界
                        # \A  and \Z differs from ^ and $ only in multiline mode
                        # . 代表任何字符包括它自己
pattern = r"([\w\.-]+)@([\w\.-]+)(\.[\w\.]+)"  # 检测邮件地址是否合法[\w\.-]+ 表示一个或多个字符，点或破折号
pattern = r"([\w\.-]+)@([\w\.-]+)(\.[\w]+)"  # 修正结尾..双点好问题
pattern = r"(\w)+([\.-](\w+))*@(\w)+([\.-]\w)*(\.(\w+))"  # 修正..@...
pattern = r"[01]+0$"  # 以多个01，，，并以0结尾


# match = re.match(pattern, "abc abcdefghi42sppeg5g99XX9xVV642xX8spam")
# print(match.group("first"))
# print(match.groups())
# 这里通过search可以用来搜索到第一个对应的email地址， 通过match方法来匹配验证结果的合法
# search, findall, match
match = re.search(pattern, "Please contact -@-.- info@sololearn.com.ab.cc.oo cc@mm.cc for assistance")
if match:
    print(match.group())

# match = re.match(pattern, "a abc@163.com.cn")
match = re.match(pattern, "10101111001010")



if match:
    print("Match 1")
if re.match(pattern, "!cat!787"):
    print("Match 4")
if re.match(pattern, "ice-cream42e42ice"):
    print("Match 2")
elif re.search(pattern, "565656！你好cat你好！5656"):
    print("search ok  2!")
elif re.search(pattern, "EgraiyE8S"):
    print("search ok  1!")
elif re.search(pattern, "gray!cat!gray"):
    print("search ok  3!")
else:
    print("not match")


# **kwargs是一个可以自定义添加函数参数的一个设置
def my_func(x, y=7, *args, **kwargs):
    print(x)
    print(y)
    print(args)
    print(kwargs)
    print(kwargs["a"])
my_func(2, 3, 4, 5, 6, a=7, b=8)  # 这里a=7, b=8是自定义的参数


# import this
"""
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!

PEP

Python Enhancement Proposals (PEP) are suggestions for improvements to the language, made by experienced Python developers. 
PEP 8 is a style guide on the subject of writing readable code. It contains a number of guidelines in reference to variable names, which are summarized here:
- modules should have short, all-lowercase names; 
- class names should be in the CapWords style; 
- most variables and function names should be lowercase_with_underscores; 
- constants (variables that never change value) should be CAPS_WITH_UNDERSCORES;
- names that would clash with Python keywords (such as 'class' or 'if') should have a trailing underscore.

PEP 8 also recommends using spaces around operators and after commas to increase readability. 
However, whitespace should not be overused. For instance, avoid having any space directly inside any type of brackets.

python增强建议：
模块名字所有的都要小写
类名首字母要大写 MyClassName
大多数的变量和函数名字应该 小写下划线，小写_小写_下划线
静态变量不变的变量应该 大写_大写_大写
与python关键字冲突的命名应该加下划线 _class,  _if,,,,,
x = (5*2) 😃😀😄 is BETTER than
x=( 5 * 2 ) 😞😢😭
空格也不应该被乱用


Other PEP 8 suggestions include the following:
- lines shouldn't be longer than 80 characters; 
- 'from module import *' should be avoided; 
- there should only be one statement per line.
一行不要超过80个字符
避免使用 from module import *, 导入所有，，，这回导致潜在的冲突bug，
缩进 尽量用 空格 不要用tab,

遵守pep8原则，避免，不能向后兼容和与周围代码不一致，，，有这些原则就能大大提高代码质量


"""


# Tuple Unpacking, 元组可以直接为内值起名
numbers = (1, 2, 3)
a, b, c = numbers
print(a, b, c)
a, b, c = b, a, c  # 内容交换
print(a, b, c)

# Ternary Operator 三元运算符
a = 7
b = 1 if a >= 5 else 42
print(b)

# else for while try/except也可以用
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

def function():
   print("This is a module function")

if __name__ == "__main__":
    print("This is a script!")

print("?????????????")
print(list(range(10)))
# packages python的包
"""
SoloLearn/
   LICENSE.txt
   README.txt
   setup.py  必须含有的文件
   sololearn/
      __init__.py  包名必须含有的文件
      sololearn.py
      sololearn2.py

setup.py:
from distutils.core import setup

setup(
   name='SoloLearn', 
   version='0.1dev',
   packages=['sololearn',],
   license='MIT', 
   long_description=open('README.txt').read(),
)

After creating the setup.py file, upload it to PyPI, or use the command line to create a binary distribution (an executable installer).
To build a source distribution, use the command line to navigate to the directory containing setup.py, and run the command python setup.py sdist.
Run python setup.py bdist or, for Windows, python setup.py bdist_wininst to build a binary distribution. 
Use python setup.py register, followed by python setup.py sdist upload to upload a package.
Finally, install a package with python setup.py install.

"""

for i in range(10):
  try:
    if 10 / i == 2.0:
      break
  except ZeroDivisionError:
    print(1)
  else:
    print(2)





























