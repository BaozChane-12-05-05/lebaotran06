# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 18:12:33 2024

@author: pc5
"""

so= int(input("nhập 1 số nguyên từ 0 đến 9: "))
sothanhchu=["không","một", "hai","ba","bốn","năm","sáu","bảy","tám","chín"]
if 0 <= so <= 9:
    print(sothanhchu[so])
else:
    print("không đọc được")    
  
    