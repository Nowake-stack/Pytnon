"""用Python设计一个游戏"""
"""改进版本"""

import random

counts = 10
answer = random.randint(1, 20)

while counts >0:

    temp  =  input("猜我想的数字是几？")
    guess = int(temp)
    if guess == answer:
        print("你猜对了！")
        counts = 0
    else:
        if guess < answer:
            print("你猜的数字小了！")
        else:
            print("你猜的数字大了！")
        counts = counts - 1
print("游戏结束！")