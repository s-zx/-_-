# -*- coding: utf-8 -*-
# @Time    : 2021/11/16 11:03
# @Author  : 沈振兴
# @FileName: dataCleaning.py
# @Software: PyCharm
import copy
import re


# f = ["docmark_v1_s", "docmark_v2_s", "docmark_v3_s"]

def checkSen(ls):
    word_num = 0
    puc_num = 0
    point_num = 0
    for j in ls:
        if "/sym" not in j:
            word_num += 1
        else:
            puc_num += 1
    if word_num < 10 or puc_num / len(ls) > 1 / 3:
        return False
    if 'ទូរសារ' in ls and 'អ៊ីមែល' in ls:
        return False
    if 'រៀបរៀង ដោយ ៖ NA' in ls:
        return False
    if 'FN ៖' in ls:
        return False
    if 'តារា សម្តែង' in ls or 'ចម្រៀង' in ls:
        return False
    if '>>>>>' in ls or '!!' in ls:
        return False

    for j in ls:
        w = j.split('/')
        if re.search('[a-z]', w[0]):
            return False
        if w[0] != ".":
            point_num = 0
        if w[0] == ".":
            point_num += 1
        if point_num >= 3:
            return False

    return True


f = ["docmark_v1_s"]
for d in f:
    print(d, " 正在处理")
    with open(d, 'r', encoding='utf-8') as fr:
        sentence_r = [i for i in fr.readlines()]
        with open("docmark_v1_s_cleaned_noPos.txt", 'w+', encoding='utf-8') as fw:
            for sen in sentence_r:
                if "<doc" in sen:
                    # fw.writelines(sen)
                    continue
                if "</doc>" in sen:
                    # fw.write3ines(sen)
                    continue

                ls = sen.split()
                ls_w = copy.deepcopy(ls)
                if checkSen(ls):
                    flag = 0
                else:
                    flag = 1
                    # print(sen)
                if flag == 0:
                    for i in ls_w:
                        word_w = i.split('/')
                        # print(word_w[0], ' ')
                        fw.write(word_w[0])
                        fw.write(' ')
                    fw.write('\n')

                else:
                    continue
