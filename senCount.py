# -*- coding: utf-8 -*-
# @Time    : 2021/11/19 17:27
# @Author  : 沈振兴
# @FileName: senCount.py
# @Software: PyCharm

with open("khmer21.vert3", 'r', encoding='utf-8') as fr:
    cnt = 0
    for i in fr.readlines():
        if "<s>" in i:
            cnt += 1
print(cnt)

# vert1: 1383710
# vert2: 1378763
# vert3: 1387333

