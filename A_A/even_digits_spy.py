# -*- coding: utf-8 -*-
"""
Created on Tue Jul  7 15:24:35 2020

@author: natur
"""

def check_bit_com_big(num):
    num = str(num)
    big_num_test=""
    big_num = ""
    for i in range(len(num)):
        num_bit = num[i:i+1]
        num_bit = int(num_bit)
        big_num_test +=str(num_bit)
        if num_bit in odd_list:
            big_num += big_num_test[0:i]
            num_bit = num_bit + 1
            big_num += str(num_bit)
            big_num += str(0)*(len(num)-i-1)
            break
    return(big_num)

def special_9_check_bit_com_big(num):
    num = str(num)
    big_num_test=""
    big_num = ""
    for i in range(len(num)):
        num_bit = num[i:i+1]
        num_bit = int(num_bit)
        big_num_test +=str(num_bit)
        if num_bit == 9:
            #mett_89
            if int(num[i-1:i]) == 8:
                big_num += big_num_test[0:i]
                num_bit = 8
                big_num += str(num_bit)
                big_num += str(8)*(len(num)-i-1)
                break
            else:
                pre_bit = int(num[i-1:i]) + 2
                big_num += big_num_test[0:i-1]
                big_num += str(pre_bit)
                big_num += str(0)*(len(num)-i)
                break
        elif num_bit in odd_list:
            big_num += big_num_test[0:i]
            num_bit = num_bit + 1
            big_num += str(num_bit)
            big_num += str(0)*(len(num)-i-1)
            break
        else:
            return "0"
    return(big_num)
                
    
def check_bit_com_small(num):
    num = str(num)
    small_num_test=""
    small_num = ""
    for i in range(len(num)):
        num_bit = num[i:i+1]
        num_bit = int(num_bit)
        small_num_test +=str(num_bit)
        if num_bit in odd_list:
            small_num += small_num_test[0:i]
            num_bit = num_bit - 1
            small_num += str(num_bit)
            small_num += str(8)*(len(num)-i-1)
            break
        else:
            return "0"
    return(small_num)

def begin_num(num):
    big_num = int(special_9_check_bit_com_big(num))
    small_num = int(check_bit_com_small(num))
    big_button = big_num-num
    small_button = num-small_num
    if big_num == 0:
        true_button = 0
    elif big_button<0:
        true_button = small_button
    else:
        true_button = min(big_button,small_button)
    return true_button

if __name__ == "__main__":
    even_list = [0,2,4,6,8]
    odd_list = [1,3,5,7,9]
    round = int(input())
    for i in range(round):
        num = int(input())
        true_button = begin_num(num)
        print("Case #"+str(i+1)+":"+" "+str(true_button))