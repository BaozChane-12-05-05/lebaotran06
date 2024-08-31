# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 18:33:59 2024

@author: lebaotran
"""
a=int(input("nhập số nguyên thứ nhất: "))
b=int(input("nhập số nguyên thứ hai: "))
c=int(input("nhập số nguyên thứ ba: "))
d=int(input("nhập số nguyên thứ tư: "))
smallest=a
if b<smallest:
    smallest=b
if c<smallest:
    smallest=c
if d<smallest:
    smallest=d
print("số nhỏ nhất là: ", smallest)
    
