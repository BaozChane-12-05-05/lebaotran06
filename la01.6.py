# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 12:30:51 2024

@author: lebaotran
"""

y=int(input("nhap nam sinh cua ban:"))
if 0< y<=2024:
    namhientai=2024
    tuoi=namhientai-y
    print("neu ban sinh nam:", y ,"vay ban",tuoi)
else:
    print("nam sinh k hop le")
