# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 18:52:44 2024

@author: lebaotran
"""
h=float(input("nhập số giờ: ")) 
m=float(input("nhập số phút: "))
s=float(input("nhập số giây: "))
if 0<=h<24:
    print("số giờ hợp lệ")
else:
    print("số giờ không hợp lệ")
if 0<=m<60:
    print("số phút hợp lệ")
else:
    print("số phút không hợp lệ")
if 0<=s<60:
    print("số giây hợp lệ")
else:
    print("số giây không hợp lệ")    
    