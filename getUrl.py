# -*- coding: utf-8 -*-
# @Time    : 2021/11/15 19:40
# @Author  : 沈振兴
# @FileName: getUrl.py
# @Software: PyCharm
ls = ["khmer21.vert1", "khmer21.vert2", "khmer21.vert3"]
URL = {}
for f in ls:
    with open(f, 'r', encoding='utf-8') as fr:
        valid = {}
        for i in fr.readlines():
            u = ''
            start = 0
            end = 0
            if "<doc" in i:
                b = i.find("lang_diff")
                start = i.find("url", b) + 5
                end = i.find("enc_meta") - 3
                for j in range(start, end + 1, 1):
                    u += i[j]
                check = u
                u_e = check.find('/', 8)
                check = check[:u_e]
                if check == '':
                    print(u)
                    print(i)
                if check not in URL:
                    URL[check] = 1
                else:
                    URL[check] += 1
            else:
                continue
with open("/Users/mac/Desktop/url_all.csv", 'w', encoding='utf-8') as fw:
    cnt = 1
    url_sorted = {k: v for k, v in sorted(URL.items(), key=lambda item: item[1], reverse=True)}
    url = list(url_sorted.keys())
    for i in url:
        fw.writelines(str(cnt) + ',' + i + ',' + str(URL[i]) + '\n')
        cnt += 1
