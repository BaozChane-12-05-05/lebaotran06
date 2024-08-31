# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 18:46:12 2024

@author: lebaotran
"""
a=int(input("nhập số thứ nhất: "))
b=int(input("nhập số thứ hai: "))
c=int(input("nhập số thứ ba: "))
solonnhat=a
if b>solonnhat:
    solonnhat=b
if c>solonnhat:
    solonnhat=c
print("số lớn nhất là: ", solonnhat)    
