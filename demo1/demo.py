"""用Python设计一个游戏"""
temp  =  input("猜我想的数字是几？")
guess = int(temp)

if guess == 8:
    print("你猜对了！")
else:
    print("错了！是8")
print("游戏结束！")
    