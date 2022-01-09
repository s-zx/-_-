# -*- coding: utf-8 -*-
# @Time    : 2021/11/20 10:04
# @Author  : 沈振兴
# @FileName: wordCount.py
# @Software: PyCharm
with open("khmer21.vert1", 'r', encoding='utf-8') as fr:
    flag_s = 0
    Word = {}
    ls = []
    cnt = 0
    for i in fr.readlines():
        if "<doc" in i:
            continue
        if "<s>" in i:
            flag_s = 1
            continue
        if "</p>" in i:
            continue
        if "</s>" in i:
            flag_s = 0
            continue
        if "</doc>" in i:
            continue
        if flag_s == 1:
            ls = i.split()   # ls[0]为词语，ls[1]为词性
            if ls[0] not in Word:
                Word[ls[0]] = 1
                cnt += 1
            else:
                Word[ls[0]] += 1
    word_sorted = {k: v for k, v in sorted(Word.items(), key=lambda item: item[1], reverse=True)}

with open("wordCount_v1.csv", 'w+', encoding='utf-8') as fw:
    word = list(word_sorted.keys())
    for i in word:
        fw.writelines(str(i) + ',' + str(word_sorted[i]) + '\n')
