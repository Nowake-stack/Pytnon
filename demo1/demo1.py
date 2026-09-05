Python 3.14.7 (tags/v3.14.7:823f032, Aug  5 2026, 10:51:32) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> dir(_builtins_)
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    dir(_builtins_)
NameError: name '_builtins_' is not defined. Did you mean: '__builtins__'?
>>> dir(__builtins__)

>>> clc
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    clc
NameError: name 'clc' is not defined
>>> clear all
SyntaxError: invalid syntax
>>> x = 3
>>> print(x)
3
>>> 数字 =666
>>> print(数字)
666
>>> x=3
>>> y=5
>>> x,y = y,x
>>> print(x,y)
5 3
>>> print('i love china.')
i love china.
>>> print("let's go！")
let's go！
>>> print("\Life is short,let\'learn Python.\"")
\Life is short,let'learn Python."
>>> print("\"Life is short,let\'learn Python.\"")
"Life is short,let'learn Python."
>>> print("\Life is short,let\'learn Python.\nI love you")
\Life is short,let'learn Python.
I love you
