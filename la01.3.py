# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 21:20:51 2024

@author: pc5
"""

a= int(input("nhap so nguyen a="))
b= int(input("nhap so nguyen b="))
if a<=0 or b<=0:
    print("ca hai so phai la so ngyen duong")
else:
    phannguyen= a//b
    phandu=a%b
    print("phannguyenla", phannguyen, "phandu la:", phandu)
