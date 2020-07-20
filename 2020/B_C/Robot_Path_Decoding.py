# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 08:56:06 2020

@author: natur
"""

def ClosingBracket(index_front,str_pro):
    for i in range(index_front+1,len(str_pro)):
        if str_pro[i] == ")":
            return i
        
def expanded(str_pro):
    str_test = ""
    #找到最后一个（
    #这一部分一直在递归
    index_front = str_pro.rfind("(")
    if index_front != -1:
        index_behind = ClosingBracket(index_front,str_pro)
        num_index = index_front - 1
        num = str_pro[num_index]
        str_test = str_test + str_pro[index_front+1:index_behind]*int(num)
        str_pro = str_pro.replace(str_pro[num_index:index_behind+1],str_test)
        #print(str_pro)
        return expanded(str_pro)
    return str_pro

if __name__ =="__main__":
    T = int(input())
    for t in range(T):
        str_pro = input()
        str_exp_pro = expanded(str_pro)
        N_count = str_exp_pro.count("N")
        #print(N_count)
        S_count = str_exp_pro.count("S")
        #print(S_count)
        W_count = str_exp_pro.count("W")
        #print(W_count)
        E_count = str_exp_pro.count("E")
        #print(E_count)
        x = (1 + E_count - W_count)%10**9
        y = (1 + S_count - N_count)%10**9
        if x == 0:
            x = 10**9
        if y == 0:
            y = 10**9
            
        print("Case #{}: {} {}".format(t+1, x, y)) 