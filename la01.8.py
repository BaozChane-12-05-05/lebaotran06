# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 12:56:18 2024

@author: pc5
"""

w=float(input("nhap can nang:"))
h=float(input("nhap chieu cao:"))
BMI = w/(h**2)
print("chi so BMI cua ban la:", round(BMI,2))
if BMI <18.5:
    print("bann dang trong tinh trang thieu can")
elif 18.5<= BMI <24.9:
    print("bann dang trong tinh trang binh thuong")
elif 25<= BMI <29.9:
    print("bann dang trong tinh trang thua can")
else:
    print("ban dnag trong tinh trang beo ")


    