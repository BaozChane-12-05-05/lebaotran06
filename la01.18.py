# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 16:55:50 2024

@author: pc5
"""
h1=int(input("nhập số giờ thứ nhất: "))
m1=int(input("nhập số phút thứ nhất: "))
s1=int(input("nhập số giây thứ nhất: "))
t1= h1*3600 + m1*360 +s1

h2=int(input("nhập số giờ thứ hai: "))
m2=int(input("nhập số phút thứ hai: "))
s2=int(input("nhập số giây thứ hai: "))
t2= h2*3600 + m2*360 +s2

tong2gio= t1+t2
print("tổng 2 giờ là : ", tong2gio) 
hieu2gio= t1-t2
print("hiệu 2 giờ là: ", hieu2gio)
print(f"{h1+h2}giờ{m1+m2}phút{s1+s2}giây")
print(f"{h1-h2}giờ{m1-m2}phút{s1-s2}giây") 


