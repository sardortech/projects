# -*- coding: utf-8 -*-
"""
Created on Sun Oct 30 14:36:49 2022

"SONNI TOPISH" O'YINI

@author: Sardorbek
"""

import random as r

def sontop(x=10):
    """Kompyuter son o'ylaydi va foydalanuvchi topishi kerak bolgan funksiya"""
    tasodifiy_son = r.randint(1,x)
    print(f"Men 1 dan {x} gacha son o'yladim. Topa olasizmi?")
    taxminlar = 0
    while True:
        taxminlar += 1
        taxmin = int(input(">>>"))
        if taxmin < tasodifiy_son:
            print("Xato. Men o'ylagan son bundan kattaroq. Yana harakat qiling: ")
        elif taxmin > tasodifiy_son:
            print("Xato. Men o'ylagan son bundan kichikroq. Yana harakat qiling: ")
        else:
            break
    print(f"\nTabriklaymiz. {taxminlar} ta taxmin bilan topdingiz!")
    return taxminlar


def sontop_pc(x=10):
    """Foydalanuvchi oylagan sonni kompyuter topshi kerak bo'lgan funksiya"""
    input(f"1 dan {x} gacha son o'ylang va istalgan tugmani bosing. Men topaman: ")
    quyi = 1
    yuqori = x
    taxminlar = 0
    while True:
        taxminlar += 1
        if quyi != yuqori:
            taxmin = r.randint(quyi, yuqori)
        else:
            taxmin = quyi
        javob = input(f"\nSiz {taxmin} sonini o'yladingiz: to'gri (t),"
                      f" men o'ylagan son bundan katttaroq (+), yoki kichikroq (-): ").lower()
        if javob == "-":
            yuqori = taxmin - 1
        elif javob == "+":
            quyi = taxmin + 1
        else:
            break
    print(f"\nMen {taxminlar} ta taxmin bilan topdim!")
    return taxminlar

def play(x=10):
    yana = True
    while yana:
        taxminlar_user = sontop(x)
        taxminlar_pc = sontop_pc(x)
        if taxminlar_user > taxminlar_pc:
            print("Men yutdim!")
        elif taxminlar_user < taxminlar_pc:
            print("Siz yutdingiz!")
        else:
            print("Durrang!")
        yana = int(input("Yana o'ynaysizmi? Ha(1)/Yo'q(0): "))   