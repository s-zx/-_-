# -*- coding: utf-8 -*-
# @Time    : 2021/11/15 18:50
# @Author  : 沈振兴
# @FileName: posCount.py
# @Software: PyCharm
with open("khmer21.vert3", 'r', encoding='utf-8') as fr:
    pos_exist = []
    pos_num = []
    for i in fr.readlines():
        # if "<s" or "<p" or "</s>" or "</p>" or "<doc" or "</doc>" in i:
        #     continue
        if "<doc" in i:
            continue
        if "<p" in i:
            continue
        if "<s>" in i:
            continue
        if "</p>" in i:
            continue
        if "</s>" in i:
            continue
        if "</doc>" in i:
            continue
        ls = i.split()
        pos = ls[1]
        # print(pos)
        if pos not in pos_exist:
            pos_exist.append(pos)
            pos_num.append(1)
        else:
            pos_num[pos_exist.index(pos)] += 1

with open("/Users/mac/Desktop/test_posCount3.txt", 'w', encoding='utf-8') as fw:
    for i in range(len(pos_exist)):
        fw.writelines(pos_exist[i] + ' : ' + str(pos_num[i]) + '\n')
