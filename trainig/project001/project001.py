# -*- coding: utf-8 -*-
"""project001.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1IB7GvBVjGdWZE7m-b8G6FzO0w0kU7285

***data type:***


---


*   int 
*   float
*   str 
*   bool
*   complex
*   list
*   tuple 
*   dict
*   set
"""

'''
Data type:
'''
i = 5
print(type(i))
print(i) 
print(i)

f = 5.0
print(type(f))
print(f)

s = 'hello world!'
print(type(s))
print(s)

b = True
print(type(b))
print(b)

c = 5 + 0j
print(type(c))
print(c)

l = ['amir' , 'ali' , 'sara']
print(type(l))
print(l)

t = ('amir' , 'ali' , 'sara')
print(type(t))
print(t)

d = {'amir' : '40018263' , 'mehrabani' : 'your last name'}
print(type(d))
print(d)

se = {'amir' , 'ali' , 'sara' , 'ali'}
print(type(se))
print(se)

"""
var name
"""
print('2a'.isidentifier())
print('a2'.isidentifier())
print('_var'.isidentifier())
print('a_var'.isidentifier())
print('a-var'.isidentifier())
print('2a_var'.isidentifier())
print('a var'.isidentifier())
print('&var'.isidentifier())
print('#var'.isidentifier())

from keyword import iskeyword

"""
keyword
"""
print(iskeyword('True'))
print(iskeyword('if'))
print(iskeyword('true'))
print(iskeyword('while'))
print(iskeyword('for'))
print(iskeyword('While'))
print(iskeyword('str'))

"""
type Casting
"""
a = 5
print(float(a))
print(complex(a))
print(bool(a))

print()

srt = '13'
print(srt + '1')
print(int(srt) + 1)
print(float(srt) + 1)

# Commented out IPython magic to ensure Python compatibility.
"""
# %i & %f & %e
"""
n = 123.3423
print('%i' %n)
print('%f' %n)
print('%e' %n)

print()

m = 0.000234
print('%i' %m)
print('%f' %m)
print('%e' %m)

"""
a = 5  ,  b = 1
f --> {a , b} --> 6 
"""
a = 5
b = 1
print('five plus one = {a + b}')
print()
print(f'five plus one = {a , b}')
print()
print(f'filve plus one = {a + b}')

"""
swap
"""
a = 5
b = 10
a , b = b , a
print(a)
print(b)

print()

x = 5 
y = 10
x , y = y , y + x
print(x)
print(y)

"""
--- string slicing ---
"""
v = "Amirreza Mehrabani"
print(v[0:5])
print(v[:])
print(v[4:])
print(v[5:8])
print(v[3:7])
print(v[0:])
print(v[0:8])
print(v[-9:-1])
print(v[-1])

"""
Reciving input
"""
g = int(input('enter first integer: '))
h = int(input('enter second integer: '))
print(g + h)