# -*- coding: utf-8 -*-
"""
Created on Wed Jul  8 13:03:41 2020

@author: natur
"""
#T是案列的数量
#N代表包裹里的数量
#K代表放回重取的机会，如果进行到K+1，则最后为K+1的value
#V代表包裹里每个元素的值
T = int(input())
for i in range(T):
    #print("请输入包裹里包含的数量N和K值")
    N,K = [int(num) for num in input().split()]
    item_v= [int(num) for num in input().split()]
    if K==0:
        E = sum(item_v)/N
    else:
        item_v.sort(reverse=True)  #降序
        
        pre_sum = [item_v[0]]
        for j in range(1,N):
            pre_sum.append(pre_sum[-1] + item_v[j])
        dp = []
        dp.append(pre_sum[-1]/N)  #均值
        
        for k in range(1,K+1):
            j = 0
            while j<N and item_v[j] >= dp[-1]:  #大于我们所求的期望
                j = j +1  #j=2时跳出循环
            dp.append((dp[-1]*(N-j)+pre_sum[j-1])/N) 
            #N-j=4,pre_sum[]
        E = dp[-1]
    print("Case #{}: {}".format(i+1,E))
          
