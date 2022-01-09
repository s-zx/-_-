import re

pos_tag = {'/NN':3,'/AUX':4,'/VB':3,'/IN':3,'/JJ':3,
           '/CD':3,'/CC':3,'/SYM':4,'/RPN':4,'/DT':3,
           '/VCOM':5,'/RB':3,'/PRO':4,'/VB_JJ':6,'/KAN':4,
           '/PN':3,'/PA':3,'/QT':3,'/M':2,'/AB':3,'/UH':3}

pos_info = {'/NN':[0,0],'/AUX':[0,0],'/VB':[0,0],'/IN':[0,0],'/JJ':[0,0],
           '/CD':[0,0],'/CC':[0,0],'/SYM':[0,0],'/RPN':[0,0],'/DT':[0,0],
           '/VCOM':[0,0],'/RB':[0,0],'/PRO':[0,0],'/VB_JJ':[0,0],'/KAN':[0,0],
           '/PN':[0,0],'/PA':[0,0],'/QT':[0,0],'/M':[0,0],'/AB':[0,0],'/UH':[0,0]}



pos_counter = 0
word_single_counter = 0
word_repeat_counter = 0

with open ('vert1_cleaned',mode='r',encoding='utf-8') as source:
    read_file = source.readlines()
    for tag in pos_tag:
        word_recorder = {'word_begin': 0}
        pos_counter += 1
        print(f'----------这是第{pos_counter}次统计，本次统计{tag}标签----------')
        file_path = f'./dataset/POS_{tag[1:]}.csv'
        pattern = re.compile('[\u1780-\u17FF]+'+str(tag))

        with open(file_path,mode='w+',encoding='utf-8') as file:
            for sentence in read_file:
                target_perSentence = re.findall(pattern=pattern,string=sentence)
                word_repeat_counter += len(target_perSentence)
                for perTarget in target_perSentence:
                    if word_recorder.get(perTarget):
                        word_recorder[perTarget] += 1
                    else:
                        word_single_counter += 1
                        word_recorder.update({perTarget:1})
                        std_target = tag[1:]+'|'+str(perTarget[:-pos_tag[tag]])+'\n'
                        file.write(std_target)
                num_perSentence = len(target_perSentence)
                # print(f'第{pos_counter}次统计，统计{tag}标签，第{row_counter}行写入完成')
                #if row_counter == 1000:
                    #break
            pos_info[tag][0] = word_repeat_counter
            pos_info[tag][1] = word_single_counter
            print(f'----------词性{tag}统计完成，在数据集中重复出现{word_repeat_counter}次，独立出现{word_single_counter}次。----------')
            word_repeat_counter = 0
            word_single_counter = 0
             # 单词计数器归零
print('所有统计已完成，数据如下：')
for tag in pos_info:
    print(f'tag:{tag}, repeative:{pos_info[tag][0]}, non-repeative:{pos_info[tag][1]}')



