# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 21:39:09 2024

@author: pc5
"""
n = int(input("Nhập số nguyên n: "))
if n>10 and n<=99:
    chuc= n//10
    donvi=n%10
    tong=chuc+donvi
    print("tongla", tong)
else:
    print("khonghople")    