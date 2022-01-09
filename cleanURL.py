# -*- coding: utf-8 -*-
# @Time    : 2021/11/20 12:19
# @Author  : 沈振兴
# @FileName: cleanURL.py
# @Software: PyCharm

with open("web_selected.csv", 'r', encoding='utf-8') as fr:
    good_url = []
    for i in fr.readlines():
        ls = i.split(',')
        if ls[3] == "可以":
            good_url.append(ls[1])

with open("docmark_vert1", 'r', encoding='utf-8') as fr:
    res = []
    flag = 0
    for i in fr.readlines():
        u = ''
        start = 0
        end = 0
        if "<doc" in i:
            b = i.find("lang_diff")
            start = i.find("url", b) + 5
            end = i.find("enc_meta") - 3
            if end == -4:
                end = i.find("title") - 2
            for j in range(start, end + 1, 1):
                u += i[j]
            check = u
            u_e = check.find('/', 8)
            check = check[:u_e]
            if check == '':
                print(u)
                print(i)
            if check in good_url:
                flag = 1
        if "</doc>" in i and flag == 1:
            flag = 0
            res.append("</doc>\n")
        if flag == 1:
            res.append(i)

with open("docmark_v3_s", 'w', encoding='utf-8') as fw:
    fw.writelines(res)
