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

import os
def return_filelist(path):
    return [x for x in os.listdir(path) if os.path.isfile(x)]

def print_path(L1,s):
    for file in L1:
        if file.find(s)!=-1:
            print(file)
        else:
            continue


pwd=os.getcwd()
print(pwd)
s=input("请输入需要查找的文件名：")

L1=return_filelist(os.getcwd())
print_path(L1,s)
for i in os.listdir(pwd):
    if os.path.isdir(i):
        print(i)
        L2=return_filelist(pwd+"\\"+i)
        print_path(L2,s)
