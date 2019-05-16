#!/usr/bin/env python 
# -*- coding:utf-8 -*-
##############################################
#copy from AwsomeName
#################################################
defined_patterns = {
    "I need ?X": ["Image you will get ?X soon", "Why do you need ?X ?"],
    "My ?X told me something": ["Talk about more about your ?X", "How do you think about your ?X ?"]
}

#pat开头是?且后面全是字母返回True
def is_variable(pat):
    return pat.startswith('?') and all(s.isalpha() for s in pat[1:])

#pattern[0]和saying[0]匹配;
# 如果pattern[0]是?, 返回[pattern[0], saying[0]]继续进行后续匹配;
# 如果pattern[0]!=saying[0], 返回[];
# pattern[0]==saying[0], 继续进行后续匹配
def pat_match(pattern, saying):
    if not pattern or not saying: return []
    if is_variable(pattern[0]):
        return [(pattern[0], saying[0])] + pat_match(pattern[1:], saying[1:])
    else:
        if pattern[0] != saying[0]:
            return []
        else:
            return pat_match(pattern[1:], saying[1:])

#把[('?X', 'iPhone')]形式的list转换为{'?X': 'iPhone'}形式的dict
def pat_to_dict(patterns):
    return {k: v for k, v in patterns}

#dict.get(key, default=None)：
# key -- 字典中要查找的键
# default -- 如果指定键的值不存在时，返回该默认值值
#parsed_rules是dict,
# parsed_rules.get(rule[0], rule[0])返回parsed_rule中rule[0]对应的value,
# 如果parsed_rules中没有key值是rule[0], 这时返回rule[0].
# 之后继续进行下一轮迭代subsitite(rule[1:], parsed_rules)
def subsitite(rule, parsed_rules):
    if not rule: return []
    return [parsed_rules.get(rule[0], rule[0])] + subsitite(rule[1:], parsed_rules)

#pat in rules中pat是rules的key值.
# 如果pat_match(pat.split(), saying.split())返回空就pass;
# 否则pat_match(pat.split(), saying.split())返回[('?X', 'iPhone')]形式的list.
# subsitite(ans.split(), pat_dict)中
# pat_dict是这种形式{'?X': 'iPhone'}; 最后返回pat_dict[ans.split()]或ans.split()
import random
def get_response(saying, rules=defined_patterns):
    for pat in rules:
        if not pat_match(pat.split(), saying.split()):
            pass
        else:
            got_patterns = pat_match(pat.split(), saying.split())
           # print(got_patterns)
            pat_dict = pat_to_dict(got_patterns)
           # print(pat_dict)
            ans = random.choice(rules[pat])
            return ' '.join(subsitite(ans.split(), pat_dict))
    pass

print(get_response('I need iPhone', defined_patterns))