#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 17:02:06 2019
"""

def gen_word_list(file_name, n):
    file = open(file_name, 'r')
    content = file.readlines()
    words = []
    for word in content:
        if len(word) == n + 1:
            words.append(word[:-1])   
    return words

print(gen_word_list('sowpods.txt', 4))