#!/usr/bin/env python3
#-*- coding:utf-8 -*-

'a test module' #模块注释

__author__ = 'HD' #作者信息
__version__ = 'v2.0' #版本信息

def __Email():  #模块私有函数
    print('hedi1117@126.com')
    
def __Wechat_Official_Account():  #模块私有函数
    print('学长说python')
    
def hello(person = 'world'): #公有函数
    print('hello',person)
    
def test(): #测试代码
    hello()
    hello('China')
    print('Contact to me:',end=' ')
    __Email()
    print('Learn more with me:',end=' ')
    __Wechat_Official_Account()
    

#当直接运行该模块时，执行测试代码，而引入模块时不执行测试代码。
if __name__ == '__main__':
    test()
