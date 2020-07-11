# -*- coding: utf-8 -*-
"""
Created on Sat Jul 11 23:41:57 2020

@author: natur
"""

S_str = 'aapxjdnrbtvldptfzbbdbbzxtndrvjblnzjfpvhdhhpxjdnrbt'

dic_list = ['axpaj', 'apxaj', 'dnrbt', 'pjxdn', 'abd']

def cal_word_fre(word):
    num = {}
    for i in range(26):
        num[chr(i+97)] = 0    #26个字母对应的value=0
    for i in range(len(word)):
        if word[i] in num.keys():
            num[word[i]] = num[word[i]] + 1
    num_list = []
    num_list.append(word[0])
    num_list.append(word[-1])
    num_list.extend(list(num.values()))
    return num_list



#针对所生成的字符串进行枚举
def begin_test(dic_list,S_str):
    count = 0
    for z in range(len(dic_list)):
        for j in range(len(S_str)):
            if j <= len(S_str) - len(dic_list[z]):
                list_test = cal_word_fre(S_str[j:j+len(dic_list[z])])
                #print(list_test)
                #print(cal_word_fre(dic_list[z]))
                if list_test == cal_word_fre(dic_list[z]):
                    count += 1
                    print(count)
                    break
    return count

if __name__ =="__main__":
    print(begin_test(dic_list,S_str))