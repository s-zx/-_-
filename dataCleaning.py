# -*- coding: utf-8 -*-
# @Time    : 2021/11/16 11:03
# @Author  : 沈振兴
# @FileName: dataCleaning.py
# @Software: PyCharm
import copy
import re
# f = ["docmark_v1_s", "docmark_v2_s", "docmark_v3_s"]
f = ["docmark_v1_s"]
for d in f:
    print(d, " 正在处理")
    with open(d, 'r', encoding='utf-8') as fr:
        sentence_r = [i for i in fr.readlines()]
        with open("docmark_v1_s_cleaned_noPos", 'w+', encoding='utf-8') as fw:
            for sen in sentence_r:
                flag = 0
                if "<doc" in sen:
                    # fw.writelines(sen)
                    continue
                if "</doc>" in sen:
                    # fw.write3ines(sen)
                    continue
                word_num = 0
                puc_num = 0
                ls = sen.split()
                ls_w = copy.deepcopy(ls)
                for j in ls:
                    if "/sym" not in j:
                        word_num += 1
                    else:
                        puc_num += 1
                if word_num >= 10 and puc_num / len(ls) <= 1/3:
                    for j in ls:
                        word = j.split('/')
                        if re.search('[a-z]', word[0]):
                            flag = 1
                            break
                else:
                    continue
                if flag == 0:
                    for i in ls_w:
                        word_w = i.split('/')
                        # print(word_w[0], ' ')
                        fw.write(word_w[0])
                        fw.write(' ')
                    fw.write('\n')
