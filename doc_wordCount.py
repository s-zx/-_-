# -*- coding: utf-8 -*-
# @Time    : 2021/11/20 15:34
# @Author  : 沈振兴
# @FileName: doc_wordCount.py
# @Software: PyCharm
with open("docmark_v1_s", 'r', encoding='utf-8') as fr:
    sentence_r = [i for i in fr.readlines()]
    Word = {}
    cnt = 0
    for i in sentence_r:
        if "<doc" in i or "</doc>" in i:
            continue
        block = i.split()
        for j in block:
            if j.split('/')[1] == "SYM":
                continue
            w = j.split('/')[0]
            if w not in Word:
                Word[w] = 1
                cnt += 1
            else:
                Word[w] += 1
    word_sorted = {k: v for k, v in sorted(Word.items(), key=lambda item: item[1], reverse=True)}

with open("wordCount_v1_s.csv", 'w+', encoding='utf-8') as fw:
    word = list(word_sorted.keys())
    for i in word:
        fw.writelines(str(i) + ',' + str(word_sorted[i]) + '\n')
