import time
#print(abs(-100))
def f1(a,b,c=0,*args,**kw):
    print(a)
    print(b)
    print(args[1])
    print(kw)

#f1(1,2,3,4,5,6,d=7)
# def trim(s):
#     while s!="":
#         if s[0]!=' ':
#             break
#         else:
#             s=s[1:]
#     while s!="":
#         if s[-1]!=' ':
#             break
#         else:
#             s=s[:-1]
#     return s
# if trim('hello  ') != 'hello':
#     print('测试失败!')
# elif trim('  hello') != 'hello':
#     print('测试失败!')
# elif trim('  hello  ') != 'hello':
#     print('测试失败!')
# elif trim('  hello  world  ') != 'hello  world':
#     print('测试失败!')
# elif trim('') != '':
#     print('测试失败!')
# elif trim('    ') != '':
#     print('测试失败!')
# else:
#     print('测试成功!')

# def findMinAndMax(L):
#     if L==[]:
#         return (None,None)
#     min=L[0]
#     max=L[0]
#     for i in L:
#         if i<min:
#             min=i
#         if i>max:
#             max=i
#     return (min,max)

# if findMinAndMax([]) != (None, None):
#     print('测试失败!')
# elif findMinAndMax([7]) != (7, 7):
#     print('测试失败!')
# elif findMinAndMax([7, 1]) != (1, 7):
#     print('测试失败!')
# elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
#     print('测试失败!')
# else:
#     print('测试成功!')

# def normalize(name):
#     return name[0].upper()+name[1:].lower()

# # 测试:
# L1 = ['adam', 'LISA', 'barT']
# L2 = list(map(normalize, L1))
# print(L2)

<<<<<<< HEAD
# import os
# def return_filelist(path):
#     return [x for x in os.listdir(path) if os.path.isfile(x)]

# def print_path(L1,s):
#     for file in L1:
#         if file.find(s)!=-1:
#             print(file)
#         else:
#             continue


# pwd=os.getcwd()
# print(pwd)
# s=input("请输入需要查找的文件名：")

# L1=return_filelist(os.getcwd())
# print_path(L1,s)
# for i in os.listdir(pwd):
#     if os.path.isdir(i):
#         print(i)
#         L2=return_filelist(pwd+"\\"+i)
#         print_path(L2,s)


# from datetime import datetime

# print(datetime.now())
# import hashlib

# md5 = hashlib.md5()
# md5.update('hoa to use md5 in python hashlib?'.encode('utf-8'))
# print(md5.hexdigest())
# from tkinter import *
# import tkinter.messagebox as messagebox

# class Application(Frame):
#     def __init__(self, master=None):
#         Frame.__init__(self, master)
#         self.pack()
#         self.createWidgets()

#     def createWidgets(self):
#         self.nameInput = Entry(self)
#         self.nameInput.pack()
#         self.alertButton = Button(self, text='Hello', command=self.hello)
#         self.alertButton.pack()

#     def hello(self):
#         name = self.nameInput.get() or 'world'
#         messagebox.showinfo('Message', 'Hello, %s' % name)

# app = Application()
# # 设置窗口标题:
# app.master.title('Hello World')
# # 主消息循环:
# app.mainloop()
# import socket
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# s.connect(('www.sina.com.cn',80))
# s.send(b'GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')

# # 接收数据:
# buffer = []
# count=0
# while True:
#     # 每次最多接收1k字节:
#     d = s.recv(1024)
#     if d:
#         buffer.append(d)
#         print(count)
#         count+=1
#     else:
#         break
# data = b''.join(buffer)
# header, html = data.split(b'\r\n\r\n', 1)
# print(header.decode('utf-8'))
# # 把接收的数据写入文件:
# with open('sina.html', 'wb') as f:
#     f.write(html)

# import os
# def return_filelist(path):
#     return [x for x in os.listdir(path) if os.path.isfile(x)]

# def print_path(L1,s):
#     for file in L1:
#         if file.find(s)!=-1:
#             print(file)
#         else:
#             continue


# pwd=os.getcwd()
# print(pwd)
# s=input("请输入需要查找的文件名：")

# L1=return_filelist(os.getcwd())
# print_path(L1,s)
# for i in os.listdir(pwd):
#     if os.path.isdir(i):
#         print(i)
#         L2=return_filelist(pwd+"\\"+i)
#         print_path(L2,s)

