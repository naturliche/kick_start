# -*- coding: utf-8 -*-
"""
Created on Sat Jul 11 21:26:25 2020

@author: natur
"""
#计算列表中单词的频率
#首尾字母相同，并且单词出现的次数一样即可
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
def find_equ(dic_list,S_str):
    count = 0
    for z in range(len(dic_list)):
        for j in range(len(S_str)):
            if j <= len(S_str) - len(dic_list[z]):
                list_test = cal_word_fre(S_str[j:j+len(dic_list[z])])
                #print(list_test)
                #print(cal_word_fre(dic_list[z]))
                if list_test == cal_word_fre(dic_list[z]):
                    count += 1
                    #print(count)
                    break
    
    return count

if __name__ =="__main__":
    T = int(input())
    for t in range(T):
        L = int(input())
        dic_list = [s for s in input().split()]
        S1,S2,N,A,B,C,D = [s for s in input().split()]
    
        N = int(N)
        A = int(A)
        B = int(B)
        C = int(C)
        D = int(D)
        x1 = ord(S1)
        x2 = ord(S2)
        x = []
        x.append(x1)
        x.append(x2)
        S = []
        S.append(S1)
        S.append(S2)
        #自动生成测试所用的字符串
        for i in range(2,N):
            x.append((A*x[i-1] + B*x[i-2] + C) % D)
            S.append(chr(97+(x[i] % 26)))
        
        S_str = "".join(S)
        count = find_equ(dic_list,S_str)
        
        print("Case #{}: {}".format(t+1, count)) 
