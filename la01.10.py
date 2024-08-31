# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 14:18:23 2024

@author: lebaotran
"""
so = int(input("nhập 4 số xe: "))
songuyen1 = so // 1000
sodu1 = so % 1000
songuyen2 = sodu1 // 100
sodu2 = sodu1 % 100
songuyen3 = sodu2 // 10
sodu3 = sodu2 % 10
songuyen4 = sodu3
tinh = songuyen1 + songuyen2 + songuyen3 + songuyen4
sonut = tinh % 10 + tinh // 10
print("số nút của xe là: ", sonut)
