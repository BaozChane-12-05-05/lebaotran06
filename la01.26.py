# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 21:56:50 2024

@author: lebaotran
"""

#Câu a
a = int(input("Nhập số a: "))
b = int(input("Nhập số b: "))
c = int(input("Nhập số c: "))

if a > b:
    a, b = b, a
if a > c:
    a, c = c, a
if b > c:
    b, c = c, b
print("Các số theo thứ tự tăng dần là:", a, b, c)

#Câu b
N = input("Nhập số nguyên N: ")
print("Số có các con số theo thứ tự tăng dần là:", ''.join(sorted(N)))
