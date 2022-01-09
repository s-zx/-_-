# -*- coding: utf-8 -*-
# @Time    : 2021/11/16 20:43
# @Author  : 沈振兴
# @FileName: doc_posCount.py
# @Software: PyCharm
with open("docmark_v1_s", 'r', encoding='utf-8') as fr:
    sentence_r = [i for i in fr.readlines()]
    pos_exist = []
    pos_num = []
    for i in sentence_r:
        block = i.split()
        for j in block:
            pos = j.split('/')[-1]
            if pos not in pos_exist:
                pos_exist.append(pos)
                pos_num.append(1)
            else:
                pos_num[pos_exist.index(pos)] += 1

with open("posCount_v1_s.txt", 'w', encoding='utf-8') as fw:
    for i in range(len(pos_exist)):
        fw.writelines(pos_exist[i] + ',' + str(pos_num[i]) + '\n')
