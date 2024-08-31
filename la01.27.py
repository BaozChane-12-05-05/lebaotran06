# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 18:18:37 2024

@author: lebaotran
"""

#hinhvuong
canh=float(input("nhập cạnh hình vuông "))
Pv=canh*4
Sv=canh*canh
print("Chu vi hình vuông là: ", Pv)
print("Diện tích hình vuông là: ", Sv)

#hinhchunhat
d=float(input("nhập chiều dài từ bàn phím: "))
r=float(input("nhập chiều rộng từ bàn phím: "))
Pn=(d+r)*2
Sn=d*r
print("Chu vi hình chữ nhật là: ", Pn)
print("Diện tích hình chữ nhật là: ", Sn)

#hinhtron
bk=float(input("nhập bán kính từ bàn phím: "))
Pt=2*3.14*bk
St=3.14*bk**2
print("Chu vi hình tròn là: ", Pt)
print("Diện tích hình tròn là: ",St)
