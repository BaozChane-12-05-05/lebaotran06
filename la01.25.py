# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 19:11:20 2024

@author: lebaotran
"""
chucai=input("nhập một chữ cái từ bàn phím: ")
if len(chucai) == 1 and chucai.isalpha():
    chuyendoi= chucai.swapcase()
    print("chữ cái sau khi chuyển đổi là: ", chuyendoi)
else:
    print("chỉ nhập chữ cái từ bàn phím ")
