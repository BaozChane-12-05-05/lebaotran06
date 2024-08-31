# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 21:31:01 2024

@author: pc5
"""

a = int(input("Nhập số nguyên a: "))
b = int(input("Nhập số nguyên b: "))

tong = a + b
hieu = a - b
tich = a * b

if b != 0:
    thuong = a / b
    thuong = round(thuong, 3)
else:
    thuong = 'Không thể chia cho 0'
print("Tổng của a và b là: ",tong)
print("Hiệu của a và b là: ",hieu)
print("Tích của a và b là: ", tich)
print("Thương của a và b là: " ,thuong)
