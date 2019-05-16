#!/usr/bin/env python 
# -*- coding:utf-8 -*-
##############################################
#sentence generation

###########################################
grammar = """
sentence => noun_phrase verb_phrase
noun_phrase => Article Adj* noun
Adj* => null | Adj Adj*
verb_phrase => verb noun_phrase
Article =>  一个 | 这个
noun =>   女人 |  篮球 | 桌子 | 小猫
verb => 看着   |  坐在 |  听着 | 看见
Adj =>   蓝色的 |  好看的 | 小小的
"""
#################################3
#解析语法的函数
def parse_grammar(grammar_str, sep='=>'):
    grammar = {}
    for line in grammar_str.split('\n'):
        line = line.strip()
        #str.strip()就是把字符串(str)的头和尾的空格，以及位于头尾的\n \t之类给删掉

        if not line: continue
        target, rules = line.split(sep)
        #sep='=>'作为分隔符,返回list,元素都是'str'

        grammar[target.strip()] = [r.split() for r in rules.split('|')]
        #r首先是rules中的str元素，这个str元素在.split一下，变成list，因为这个str没有空格，所以就只是达到了把str变为list的效果
    return grammar

import random
#func of generate sentence
def gene(grammar_parsed, target='sentence'):
    if target not in grammar_parsed: return target
    rule = random.choice(grammar_parsed[target])
    return ''.join(gene(grammar_parsed, target=r) for r in rule if r != 'null')



#################################################
#最后随机生成几个句子

for i in range(2):
    print(gene(parse_grammar(grammar), 'sentence'))#句子
for i in range(2):
    print(gene(parse_grammar(grammar), 'Adj'))#形容词
