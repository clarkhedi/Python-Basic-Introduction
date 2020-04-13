### **一、算术运算**


```python
1+(100-20)/4+5*2 #四则运算
```




    31.0




```python
2**10 #乘方运算
```




    1024




```python
7%5 #求模运算
```




    2




```python
7//5 #地板除法(整除)
```




    1




```python
abs(-1) #绝对值运算(适用于float、int和复数类型。返回是float和int类型)
```




    1




```python
import math
```


```python
math.fabs(-5) #绝对值运算(只适用于float、int类型。返回是float类型)
```




    5.0




```python
math.sin(math.pi/2) #三角函数运算
```




    1.0




```python
math.log(math.e) #对数运算(log默认以e为底)
```




    1.0




```python
math.factorial(5) # 阶乘运算
```




    120




```python
(1 + 2j) + (3 - 1j) #复数运算
```




    (4+1j)




```python
complex(2,1)/(2+1j) #复数运算
```




    (1+0j)




```python
#math.factorial(1000) + 2**100 #强大的计算器
```


### 二、输入输出
输入：input

输出：print

```python
#input 输入的都是字符串
weight = input('please input your weight:')
weight
```

    please input your weight: 60
    




    '60'




```python
#利用float函数将字符串转换成浮点数
weight = float(input('please input your weight:'))
weight
```

    please input your weight: 60
    




    60.0




```python
#利用eval函数将输入的字符串作为表达式进行计算
age = eval(input('please input your age:'))
age #算年龄
```

    please input your age: 2020-1998
    




    22




```python
#输出用print,print()里变量用逗号(,)隔开即有：默认的 sep=' '分隔符，end='\n'结尾符
print(f'your weight is:{weight}kg')
```




    'your weight is:60kg'




```python
#或者直接使用f-string(python3.6及以上版本)
f'your age is:{age}'
```




    'your age is:22'




### 三、导入模块
import ...

或 from ... import ...
或 import ... as ...

```python
### 以普通方式导入

import datetime
datetime.datetime.today() #获取当前时间
```




    datetime.date(2020, 4, 12)




```python
### 导入模块中某个对象

from datetime import datetime
datetime.today()
```




    datetime.datetime(2020, 4, 12, 1, 16, 44, 79453)




```python
### 导入模块中全部对象

from datetime import *
print(datetime.today())
date.today() #获取当前日期
```

    2020-04-12 01:54:03.982064
    




    datetime.date(2020, 4, 12)




```python
### 以简写方式导入模块

import datetime as dt
dt.datetime.today()
```




    datetime.datetime(2020, 4, 12, 1, 20, 44, 994886)




### 四、语法规则
1、标识符

标识符由字母、数字、下划线组成，区分大小写，不能以数字开头。
以下划线开头的标识符有特殊含义。以单下划线开头的(_foo)代表不能直接访问类属性，以双下划线开头的(__foo)代表类的私有成员；以双下划线开头和结尾的(__foo__)代表Python里特殊方法专用的标识，如__init__()代表类的构造函数。

```python
import numpy as np
np.__version__
```




    '1.18.2'


2、缩进

Python的代码块不使用大括号或者其他来控制类、函数、以及其他逻辑判断，而是使用缩进来实现代码分组。通常用四个空格来进行缩进。

```python
a, b = 1, 2
if a > b:
    x = a
else:
    x = b
print(x)
```

    2
    
3、注释

Python中单行注释采用 # 开头。多行注释在代码块首尾分别使用三个单引号(''')或三个双引号(""")。

```python
"""
author: HD
date: 2020-4-12
"""
def my_abs(x): #自定义绝对值函数
    if x > 0:
        return x
    else:
        return -x
my_abs(-5)
```




    5


4、一条语句粉多行显示

Python语句中一般以新行作为语句的结束符。
但是我们可以使用反斜杠(\)将一行的语句分为多行显示。
如果有{},[],()跨行则可以不使用\。

```python
print(1+2+3+4+5+6+\
+7+8+9+10)
a = [1,2,3,4,
    5,6,7,8]
a
```

    55
    




    [1, 2, 3, 4, 5, 6, 7, 8]


5、同一行显示多条语句

Python可以在同一行中使用多条语句，语句之间使用分号分割。

```python
a = 1; b = a + 5
print(a,b)
```

    1 6
    


### 五、Python数据结构概述

Python内建的数据结构有列表，元组，字符串，集合，字典等。

此外常用的还有numpy中的`array`，以及pandas中的`dataframe`和`series`。

**1、有序数据结构：**

`list`(列表)，是有序集合，没有固定大小，可以通过对偏移量以及其他方法修改列表大小。基本形式如：[1,2,3,4]

`tuple`(元组)，是有序集合、**不可变的**，可以进行组合和赋值运算后会生成一个新的元组。基本形式如：(1,3,5,7)

`str`(字符串)，是有序集合，基本形式如：'hello'


```python
#有序数据结构可通过下标访问数据
l = [1,2,3,4]
print(l[0]) 
l[0] = 9
l
```

    1
    




    [9, 2, 3, 4]



**2、无序数据结构**

`set`(集合)，是一个无序**不重复**元素的集合。基本功能包括关系运算和消除重复元素。基本形式如：{'apple','orange','banana'}

`dict`(字典)，是无序的键值对的集合。**键必须是互不相同的(在同一个字典之内)**，可通过键访问其值。基本形式如：{'ICBC':95588,'BOC':95566}


```python
d = {'ICBC':95588,'BOC':95566}
d['BOC']
```




    95566



**3、小知识：浅拷贝和深拷贝**

浅拷贝(不可变类型tuple利用赋值):只是原来对象的一个别名即做更改拷贝后的对象会改变原来的对象

深拷贝(可变类型利用copy()函数):会开辟新的内存空间即做更改拷贝后的对象不会改变原来的对象


#### `列表list`


```python
### 1、建立列表

fruits = ['apple','orange','banana'] #直接建立
a = list(range(1,11,2)) #利用list建立
b = [2**i for i in range(5)] #利用列表推导式(for循环内的语句写在前面)建立
c = [[i+j for i in range(3)] for j in range(2)] #利用列表推导式建立二维列表
print(fruits,a,b,c,sep='\n') 
```

    ['apple', 'orange', 'banana']
    [1, 3, 5, 7, 9]
    [1, 2, 4, 8, 16]
    [[0, 1, 2], [1, 2, 3]]
    


```python
### 2、访问列表
# 列表支持下标访问和切片访问---具体有顺序(从左往右)和逆序(从右往左)
# 比如：顺序从0开始，逆序从-1开始

l = [1,2,3,4,5]
print(l[0],l[-1],sep=',') #下标访问
#切片访问，中间用冒号隔开，前两位取值遵循左闭右开原则，第三位2表示步长
print(l[0:3:2],l[-5:-2:2],sep='\n') 
print(l[:])
print(l[:-1])
print(l[::2])
```

    1,5
    [1, 3]
    [1, 3]
    [1, 2, 3, 4, 5]
    [1, 2, 3, 4]
    [1, 3, 5]
    


```python
### 3、修改列表

l = [1,2,3,4,5]
l[0] = 0
print(l)
l.remove(2) #或者用del(l[1])删除元素值2
print(l)
l = l * 3 # *号有复制拷贝多份效果
print(l)
l = l + [6,7,8,9] # +号对序列有拼接作用
print(l)
```

    [0, 2, 3, 4, 5]
    [0, 3, 4, 5]
    [0, 3, 4, 5, 0, 3, 4, 5, 0, 3, 4, 5]
    [0, 3, 4, 5, 0, 3, 4, 5, 0, 3, 4, 5, 6, 7, 8, 9]
    


```python
### 4、列表常用函数

print(len(l)) #列表长度

print(max(l)) #列表中最大值

print(min(l)) #列表中最小值

print(sorted(l)) #列表中元素排序，默认从小到大
print(sorted(l,reverse=True)) #改为逆序(从大到小)
```

    16
    9
    0
    [0, 0, 0, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 7, 8, 9]
    [9, 8, 7, 6, 5, 5, 5, 4, 4, 4, 3, 3, 3, 0, 0, 0]
    


```python
### 5、列表常用方法

lt = [7,8,9]
lt.extend([10,11])
lt.append(12)
print(lt)
lt.insert(0,1)
print(lt)
```

    [7, 8, 9, 10, 11, 12]
    [1, 7, 8, 9, 10, 11, 12]
    


#### `字典dict`

字典在插入元素和查找元素方面很多时候比列表更加高效。


```python
### 1、创建字典

d = {1:3,2:4,3:6} #一般创建
a = dict([('a',1),['b',2]]) #利用dict创建
b = dict(x=1,y=2)
D = {i:i**2 for i in range(5)} #利用字典推导式创建
print(d,a,b,D,sep='\n')
```

    {1: 3, 2: 4, 3: 6}
    {'a': 1, 'b': 2}
    {'x': 1, 'y': 2}
    {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
    


```python
### 2、字典常用操作

a['a'] = 3 #通过键来改变和添加对应的值
a['c'] = 5
print(a)
a.update({'b':4,'d':8}) #通过update函数更新对应的键值
print(a)
```

    {'a': 3, 'b': 2, 'c': 5}
    {'a': 3, 'b': 4, 'c': 5, 'd': 8}
    


```python
a.keys()
```




    dict_keys(['a', 'b', 'c'])




```python
a.values()
```




    dict_values([3, 2, 5])




```python
a.items()
```




    dict_items([('a', 3), ('b', 2), ('c', 5)])




```python
d = {'a':3,'b':4,'c':5,'d':8}
print(d.get('b')) #获取键对应的值
d.get('e',0) #给没有的键设置默认值，没有添加进去
print(d)
d.setdefault('e',4) #给没有的键设置默认值并添加进去
print(d)
```

    4
    {'a': 3, 'b': 4, 'c': 5, 'd': 8}
    {'a': 3, 'b': 4, 'c': 5, 'd': 8, 'e': 4}
    


#### `字符串str`


```python
### 1、创建字符串

print(str(12345))
s1 = 'I\'m Clark.\nI just use Python to say:"hello world"!' #\为转义字符
print(s1)
```

    12345
    I'm Clark.
    I just use Python to say:"hello world"!
    


```python
s2 = "I'm Clark.\nI just use Python to say:\"hello world\"!"
print(s2)
```

    I'm Clark.
    I just use Python to say:"hello world"!
    


```python
s3 = '''I'm Clark.
I just use Python to say:"hello world"!
'''
print(s3)
```

    I'm Clark.
    I just use Python to say:"hello world"!
    
    


```python
### 2、字符串拼接(+,join)

s1 = "I'm Clark."
s2 = "I love Python."
s3 = 'I just use Python to say:"hello world"!'
print(s1+'\n'+s2+'\n'+s3) # +号拼接
```

    I'm Clark.
    I love Python.
    I just use Python to say:"hello world"!
    


```python
print('\n'.join([s1,s2,s3])) #join拼接
```

    I'm Clark.
    I love Python.
    I just use Python to say:"hello world"!
    


```python
'abc' * 5 #乘法有复制效果
```




    'abcabcabcabcabc'




```python
### 3、字符串的常用方法

#split()中第一个参数：分隔符--默认为所有的空字符，包括空格、换行(\n)、制表符(\t)等；第二个参数：分割次数--默认为 -1, 即分隔所有
print("Clark\t22\tmale".split())
"Clark\t22\tmale".split('\t',1) #分割完后的字符串个数=分割次数+1
```

    ['Clark', '22', 'male']
    




    ['Clark', '22\tmale']




```python
"\n123abc\t".strip() #strip()方法用于移除字符串头尾指定的字符（默认为空格或换行符）或字符序列
```




    '123abc'




```python
"$$$$abcdef$$$xyz".replace('$','') #用空字符串代替$
```




    'abcdefxyz'




```python
### 4、格式化字符串(%或format或f-string)

age = 22
weight = 60.5
hobby = 'travelling'
```


```python
fs = "I'm %d years old. My weight is %.2f kg. I like %s." %(age,weight,hobby) # %格式化
print(fs)
```

    I'm 22 years old. My weight is 60.50 kg. I like travelling.
    


```python
fs = "I'm {} years old. My weight is {:.2f} kg. I like {}." .format(age,weight,hobby) # format格式化
print(fs)
```

    I'm 22 years old. My weight is 60.50 kg. I like travelling.
    


```python
fs = f"I'm {age} years old. My weight is {weight:.2f} kg. I like {hobby}." # f-string格式化(python3.6版本及以上可以使用)
print(fs)
```

    I'm 22 years old. My weight is 60.50 kg. I like travelling.
    


#### `元组tuple`


```python
### 1、创建元组

t = (1,2,3)
t0 = ()
t1 = (1,)
x = 1,2
print(t,t0,t1,x,sep='\n')
```

    (1, 2, 3)
    ()
    (1,)
    (1, 2)
    


```python
y = tuple([1,2,3])
z = tuple('abc')
print(y,z,sep='\n')
```

    (1, 2, 3)
    ('a', 'b', 'c')
    


```python
### 2、使用元组

t = (1,2,2,1,1,3)
print(t.count(1))
print(t.index(3))
```

    3
    5
    


```python
#序列解包
a,b = 1,2
t1,t2,t3 = [1,2,3]
print(a,b,t1,t2,t3,sep='\n')
```

    1
    2
    1
    2
    3
    


```python
#元组可以作为字典的key

d ={(1,2):4}
print(d)
```

    {(1, 2): 4}
    

#### `集合set`


```python
### 1、创建集合

s = {1,2,3}
s0 = set() #创建空集合，{}是创建一个空字典
s1 = {x**2 for x in range(5)}
print(s,s0,s1,sep='\n')
```

    {1, 2, 3}
    set()
    {0, 1, 4, 9, 16}
    


```python
### 2、使用集合

# 去除重复对象，求交集、并集、补集等操作
a = [1,2,3,6,4,5,5,2,6,3,1]
set(a) #去重
```




    {1, 2, 3, 4, 5, 6}




```python
s1 = {1,2,3,5,6}
s2 = {2,5,6,7,8}
print(s1 & s2) #交集
print(s1 | s2) #并集
print(s1.difference(s2)) #补集
```

    {2, 5, 6}
    {1, 2, 3, 5, 6, 7, 8}
    {1, 3}
    


### 六、条件语句 if


```python
### 1、if语句
a,b = 3,2

if a>b:
    x = a
else:
    x = b
print(x)

#if...elif...elif...else...

#单行实现if语句
y = a if a>b else b
print(y)
```

    3
    3
    


```python
### 2、逻辑运算符

2>3 
1+2<100
3 == 4-1

2 != 3
not 2 == 3
```




    True




```python
### 3、and和or

2>3 and 4<5
2>3 or 4<5

# 短路计算
[] and [1,2] and {}
[] or [1,2] or {} 
```




    [1, 2]




```python
# 注意空字符串、空列表、空字典、空元组和空集合以及0的bool值为false
bool(''),bool([]),bool({}),bool(()),bool(set()),bool(0)
```




    (False, False, False, False, False, False)




### 七、循环语句 for,while


```python
### 1、for循环

l = [1,2,3,4,5,6]
for i in l:
    print(i,end=' ')
```

    1 2 3 4 5 6 


```python
d = {'a':1,'b':2,'c':3}
for k,v in d.items():
    print(k,':',v)
```

    a : 1
    b : 2
    c : 3
    


```python
# for循环实现九九乘法表
for i in range(1,10):
    for j in range(1,i+1):
        print(f'{j} x {i} = {i*j:2d}',end='  ')
    print() 
```

    1 x 1 =  1  
    1 x 2 =  2  2 x 2 =  4  
    1 x 3 =  3  2 x 3 =  6  3 x 3 =  9  
    1 x 4 =  4  2 x 4 =  8  3 x 4 = 12  4 x 4 = 16  
    1 x 5 =  5  2 x 5 = 10  3 x 5 = 15  4 x 5 = 20  5 x 5 = 25  
    1 x 6 =  6  2 x 6 = 12  3 x 6 = 18  4 x 6 = 24  5 x 6 = 30  6 x 6 = 36  
    1 x 7 =  7  2 x 7 = 14  3 x 7 = 21  4 x 7 = 28  5 x 7 = 35  6 x 7 = 42  7 x 7 = 49  
    1 x 8 =  8  2 x 8 = 16  3 x 8 = 24  4 x 8 = 32  5 x 8 = 40  6 x 8 = 48  7 x 8 = 56  8 x 8 = 64  
    1 x 9 =  9  2 x 9 = 18  3 x 9 = 27  4 x 9 = 36  5 x 9 = 45  6 x 9 = 54  7 x 9 = 63  8 x 9 = 72  9 x 9 = 81  
    


```python
### 2、while循环

# 求1+2+3+...+100的和
s,i = 0,1
while i<=100:
    s += i
    i += 1
print(s,i)
```

    5050 101
    


```python
# 打印斐波那契(Fibonacci)数列。这个数列前两项为 1，之后的每一个项都是前两项之和。
a, b = 0, 1
while b < 100:
    print(b,end=' ')
    a, b = b, a + b
```

    1 1 2 3 5 8 13 21 34 55 89 


```python
# while循环实现九九乘法表
i = 1
while i<10:
    j = 1
    while j<i+1:
        print(f'{j} x {i} = {i*j:2d}',end='  ')
        j +=1
    print()
    i += 1
```

    1 x 1 =  1  
    1 x 2 =  2  2 x 2 =  4  
    1 x 3 =  3  2 x 3 =  6  3 x 3 =  9  
    1 x 4 =  4  2 x 4 =  8  3 x 4 = 12  4 x 4 = 16  
    1 x 5 =  5  2 x 5 = 10  3 x 5 = 15  4 x 5 = 20  5 x 5 = 25  
    1 x 6 =  6  2 x 6 = 12  3 x 6 = 18  4 x 6 = 24  5 x 6 = 30  6 x 6 = 36  
    1 x 7 =  7  2 x 7 = 14  3 x 7 = 21  4 x 7 = 28  5 x 7 = 35  6 x 7 = 42  7 x 7 = 49  
    1 x 8 =  8  2 x 8 = 16  3 x 8 = 24  4 x 8 = 32  5 x 8 = 40  6 x 8 = 48  7 x 8 = 56  8 x 8 = 64  
    1 x 9 =  9  2 x 9 = 18  3 x 9 = 27  4 x 9 = 36  5 x 9 = 45  6 x 9 = 54  7 x 9 = 63  8 x 9 = 72  9 x 9 = 81  
    


```python
### 3、循环控制 continue，break

s = 'hello world'

# break跳出本层循环
for i in s:
    if i == ' ': #遇到空格就终止
        break
    print(i,end='')

print() #换行

# continue跳出本次循环
for i in s:
    if i == ' ':  #不打印空格
        continue
    print(i,end='')
```

    hello
    helloworld


```python
### 4、循环中的else

# 循环后面使用可选的 else 语句。它将会在循环完毕后执行，一旦有break终止就不会执行else后面的语句。
for i in range(0, 5):
    print(i,end=' ')
else:
    print("Bye bye")
```

    0 1 2 3 4 Bye bye
    
Python中循环的 else 子句给我们提供了检测循环是否顺利执行完毕的一种优雅方法

### 八、函数


```python
### 1、函数参数：普通参数，默认参数，可变参数，关键字参数
### 参数定义顺序：普通参数，默认参数，可变参数，关键字参数
# 普通参数 x(位置参数)

def my_abs(x):
    return x if x>=0 else -x

my_abs(-5)
my_abs(x = -5)
```




    5




```python
# 默认参数 n(参数缺失时赋默认参数且默认参数定义时必须写在普通参数后)

def my_power(x,n=2):
    return x**n

my_power(5)
my_power(5,3)
my_power(x=5,n=3)
```




    125




```python
# 可变参数 *args(可以传入不定长度的参数序列---元组或列表)

def my_sum(*args):
    s = 0
    for i in args:
        s += i
    return s

my_sum()
my_sum(1,2,3)
my_sum(*(1,2,3))
my_sum(*[1,2,3])
```




    6




```python
# 关键字参数 **kv(可以传入字典)

def student(name,age,**kv):
    d = {'name':name,'age':age}
    d.update(kv) #将传进的**kv参数更新到d中
    return d

student('HD',22,grade="一班",gender='male')
Clark = {'name':'Clark','age':22,'grade':"一班",'hometown':'hunan'}
student(**Clark)
```




    {'name': 'Clark', 'age': 22, 'grade': '一班', 'hometown': 'hunan'}




```python
### 2、递归函数
# 递归函数特点：调用自身

# 斐波那契(Fibonacci)数列。这个数列前两项为 1，之后的每一个项都是前两项之和。
def fib(n):
    if n in [1,2]: #前两项为 1
        return 1
    else:
        return fib(n-1) + fib(n-2)

fib(11)
```




    89




```python
### 3、装饰器

# 装饰器在不更改函数代码前提下赋予函数额外的功能
# 通常把函数非核心逻辑如插入日志、权限校验、性能测试放在装饰器中

import time
def decorater(func):
    def wrapper(*args,**kv):
        tic = time.time()
        ans = func(*args,**kv)
        toc = time.time()
        print(f'{func.__name__} is called. {toc-tic}s are used.')
        return ans
    return wrapper
```


```python
@decorater
def my_sum(*args):
    s = 0
    for i in args:
        s += i
    return s
# @decorater是一个语法糖
# 相当于 my_sum = decorater(my_sum)
```


```python
my_sum(*range(100))
```

    my_sum is called. 0.0s are used.
    




    4950




```python
my_sum(1,2,3) #相当于 decorater(my_sum)(1,2,3)
```

    my_sum is called. 0.0s are used.
    




    6




```python
@decorater
def fib(n):
    if n in [1,2]: #前两项为 1
        return 1
    else:
        return fib(n-1) + fib(n-2)

fib(4)
```

    fib is called. 0.0s are used.
    fib is called. 0.0s are used.
    fib is called. 0.0s are used.
    fib is called. 0.0s are used.
    fib is called. 0.0s are used.
    




    3



### 九、lambda匿名函数

lambda只是一个表达式，适合定义较为简单的函数,不可在里面写循环。  

lambda函数的定义语法是：

**fun = `lambda` 参数序列:返回值表达式**

一般来说通过使用lambda匿名函数可以节约程序开支并加快运行速度。


```python
my_abs = lambda x:x if x>=0 else -x
my_abs(-5)
```




    5




```python
my_power = lambda x,n=2:x**n
my_power(-5)
```




    25




```python
(lambda x,n=2:x**n)(-5,3)
```




    -125




```python
my_sum = lambda *args:sum(args)
my_sum(1,2,3)
```




    6




```python
student = lambda name,age,**kv:dict(name = name,age = age,**kv)
student('HD',22,grade='一班',gender='male')
```




    {'name': 'HD', 'age': 22, 'grade': '一班', 'gender': 'male'}




```python
fib = lambda n:1 if n in [1,2] else fib(n-1) + fib(n-2)
fib(11)
```




    89




### 十、高阶函数

以函数为参数的函数称为高阶函数。常用的内置高阶函数有：map,reduce,filter。

高阶函数和匿名函数搭配使用，堪称绝配。


```python
### 1、map将一个函数的方法作用到一个序列或者多个序列，且map返回的是map object
# map原意为：映射

list(map(lambda x:x**2,[1,2,3,4]))
```




    [1, 4, 9, 16]




```python
list(map(lambda x,y:x+y,'abc','123')) #字符串中+号是拼接作用
```




    ['a1', 'b2', 'c3']




```python
### 2、reduce将一个带有两个参数的函数的方法依次迭代作用到一个序列
# reduce原意为：减少
# reduce(f,[a,b,c,d]) 相当于 f(f(f(a,b),c),d)

from functools import reduce
reduce(lambda x,y:x+y,[1,2,3,4])
```




    10




```python
### 3、filter根据一个函数(函数返回值最好是bool值)的规则过滤序列中的元素，且filter返回值返回的是filter object
# filter原意为：过滤

list(filter(lambda x:x>0,[-1,1,-2,2]))
```




    [1, 2]




### 十一、Python推导式

Python中的推导式是我最喜爱的一类语法规则，没有之一。

Python推导式可以生成列表、字典和集合。

Python推导式虽然简单，但表达能力很强，可以实现map，filter等功能，并且可以多重遍历。

淋漓尽致地体现了Python语言的simple，readable，powerful的特点。


```python
### 1、列表推导式

# 语法规范：
# out_list = [out_express for out_express in input_list if out_express_condition]
# 其中的 if 条件判断根据需要可有可无。

# 生成平方数序列
[x**2 for x in range(5)]

# 求序列的绝对值
l = [-1,-2,3,5,-6]
[x if x>=0 else -x for x in l] # 函数在循环前
list(map(lambda x:x if x>=0 else -x,l))

# 过滤序列中某些元素(条件在循环后)
[x for x in l if x>0]
list(filter(lambda x:x>0,l))

# 多重遍历
girls = ['Mary','Lily']
boys = ['Jim','John']
[(b,g) for b in boys for g in girls] #out_express需用括号，顺序和不用推导式的原始for循环是一致的
```




    [('Jim', 'Mary'), ('Jim', 'Lily'), ('John', 'Mary'), ('John', 'Lily')]




```python
### 2、字典推导式

seasons = {'Spring','Summer','Autumn','Winter'}
{k:v for k,v in enumerate(seasons,start=1)}
```




    {1: 'Winter', 2: 'Summer', 3: 'Autumn', 4: 'Spring'}




```python
list(enumerate(seasons,start=1))
```




    [(1, 'Winter'), (2, 'Summer'), (3, 'Autumn'), (4, 'Spring')]




```python
keys = ['a','b','c']
values = [1,2,3]
{k:v for k,v in zip(keys,values)}
```




    {'a': 1, 'b': 2, 'c': 3}




```python
list(zip(keys,values))
```




    [('a', 1), ('b', 2), ('c', 3)]




```python
### 3、集合推导式

# 生成绝对值序列
{abs(x) for x in [-1,2,-2,-3,1]}

# 求两个集合的交集
a = {1,2,3,4}
b = {2,4,6,8}

a.intersection(b) #内置方法求交集
{x for x in a if x in b} #集合推导式求交集
```




    {2, 4}




### 十二、类和对象

1、面向对象基本概念

- 什么是面向过程编程和面向对象编程？

面向过程编程(POP：Process Oriented Programming).程序被看成一系列命令的依次执行。基本封装形式为函数。
设计函数的基本要点是IPO：输入input——>处理Process——>输出Output.

面向对象编程(OOP:Object Oriented Programming).程序被看成一系列对象的相互作用。基本的封装形式是类。
设计类的基本要点是RPM：关系Relation，属性Property，方法Method.

- 面向对象基本术语？

类：class，抽象数据结构，数据和算法的封装。如：定义一个类：dog。

对象：object，类的实例。如：dog类的一个实例：点点dot。

属性：properties，和对象关联的数据部分。如：weight体重，breed品种。

方法：methods，和对象关联的算法部分。如：run(),eat(),bark()。

- 面向对象编程的优点？

容易使用：封装，奇妙的句点符号。

容易扩展：继承，多态。

2、创建类和对象


```python
# 创建一个Dog类
class Dog(object):
    
    # 类的构造函数__init__
    def __init__(self,name,weight,breed,age):
        self.name = name
        self.weight = weight
        self.breed = breed
        
        # __age为私有属性
        self.__age = age
    
    def run(self):
        print(f'{self.name} is running...')
        
    def bark(self):
        print('Bowwow,Bowwow,Bowwow...')
        
    def eat(self,food):
        print(f'{self.name} is eating {food}...')
        
    def sleep(self):
        print('Zzz...Zzz...Zzz...')
        
    # __think为私有方法
    def __think(self):
        print("I think I'm a hero and very handsome!")
        
    # speak公有方法可以调用私有方法
    def speak(self,words=''):
        self.__think()
        if words:
            print(words)
            
# 实例化一个对象
gu = Dog('giao',3,'Husky',4) #调用类的构造函数__init__

# 调用公有属性和公有方法
print(gu.breed)
gu.run()
gu.bark()
gu.eat('meat')
gu.speak("HaHaHa!!!")
gu.sleep()

# 私有属性和私有方法不能够直接在类外部访问
# gu.__age
# gu.__think()
```

    Husky
    giao is running...
    Bowwow,Bowwow,Bowwow...
    giao is eating meat...
    I think I'm a hero and very handsome!
    HaHaHa!!!
    Zzz...Zzz...Zzz...
    

3、获取对象信息


```python
# Python中万物皆对象。对象由类创建而来，所有的类都是object基类的子类。

# type查看对象类别
type(1),type(False),type(gu),type(len),type([1,2,3])

# isinstance 测试某个对象是否属于某个类
isinstance({1,2,3},set) #输出：True
isinstance(max,object) #输出：True
isinstance(123,(list,str,float,int))
```




    True




### 十三、封装和继承

1、封装

奇妙的句点符号：通过奇妙的句点符号可以召唤对象的属性和方法。
私有属性和私有方法除外。

(1) 公有属性和公有方法

(2) 私有属性和私有方法：以双下划线开头

(3) 定制属性和定制方法：以双下划线开头和双下划线结尾

`__init__` 构造函数，通过类名调用

`__str__` 通过str函数调用

`__len__` 通过len函数调用

......

(4) 类属性和类方法：在`__init__`**外部定义**的为类属性，**第一个参数不是self参数**的方法为类方法。


```python
class Animal(object):
    
    #类属性
    home = 'earth'
    
    #类方法
    def dream():
        print('No deal,no hurt!')
        
    #定制方法
    def __str__(self): #从属于对象的，所以加self
        return f'An animal named {self.name}'
        
    #类的构造函数__init__
    def __init__(self,name,weight,breed,age):
        self.name = name
        self.weight = weight
        self.breed = breed
        
        # __age为私有属性
        self.__age = age
    
    def run(self):
        print(f'{self.name} is running...')
        
    def eat(self,food):
        print(f'{self.name} is eating {food}...')
        
    def sleep(self):
        print('Zzz...Zzz...Zzz...')
        
    # __think为私有方法
    def __think(self):
        print("I think I'm a hero and very handsome!")
        
    # speak公有方法可以调用私有方法
    def speak(self,words=''):
        self.__think()
        if words:
            print(words)

#类属性home
gu = Animal('giao',3,'Husky',4) #实例化一个对象gu
gu.home #输出为：'earth'
Animal.home #输出为：'earth'
Animal.home = 'Jupyter' #修改类属性home
gu.home #输出为：'Jupyter'

#增加对象gu的一个公有属性home，通过对象能够访问，但通过对象不能够修改类属性home
gu.home = 'moon' 
gu.home #输出为：'moon'
Animal.home #输出为：'Jupyter'
del gu.home #删除对象gu的一个公有属性home
gu.home #输出为：'Jupyter'

#类方法只能通过类名访问，不能通过对象访问
Animal.dream()

#通过类名也可以访问对象方法
Animal.run(gu) #参数self通过对象gu传递
gu.run() 

#定制方法有特殊的功能，通过str调用
str(gu) #参数self通过对象gu传递

#奇妙的句点符号
s = 'abc#123@def'

#面向过程必须记住非常多的函数名，如：replace,upper,find...

#面向对象只需要输入奇妙的句点符号后按下tab键
s.replace('#','').replace('@','') #输出为：'abc123def'
len(s) #输出：11
s.__len__() #调用其定制方法

# dir(s) #查看全部可用属性和方法
```

    No deal,no hurt!
    giao is running...
    giao is running...
    




    11



2、继承


```python
# 子类可以通过继承获得父类的属性和方法
# 可以继承多个父类，且可以增加新的属性和方法
class Cat(Animal):
    
    def call(self):
        print('MiaoMiaoMiao...') 

#实例化一个对象kitty
kitty = Cat('kitty',1,'Bose',5)
kitty.run()
kitty.call()
kitty.speak('MiaoMiaoMiao...')
```

    kitty is running...
    MiaoMiaoMiao...
    I think I'm a hero and very handsome!
    MiaoMiaoMiao...
    


```python
try:   
    !jupyter nbconvert --to python **.ipynb
    # python即转化为.py，script即转化为.html
    # **.ipynb即当前module的文件名
except:
    pass
```
