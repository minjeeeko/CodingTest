#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Solution 1 

def solution(num):
    answer = []
    for i in range(len(num)-1):
        for j in range(1, len(num)):
            if i != j:
                answer.append(num[i] + num[j])
    return sorted(list(set(answer)))


# In[ ]:


# Solution 2

def solution(numbers):
    answer = []
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            answer.append(numbers[i] + numbers[j])
    return sorted(list(set(answer)))

