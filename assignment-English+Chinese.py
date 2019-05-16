#!/usr/bin/env python 
# -*- coding:utf-8 -*-
#############################################################
#response in chinese+English
# response in English first
###########################################################
rule_responses = {
    '?*x hello ?*y': ['How do you do', 'Please state your problem'],
    '?*x I want ?*y': ['what would it mean if you got ?y', 'Why do you want ?y', 'Suppose you got ?y soon'],
    '?*x if ?*y': ['Do you really think its likely that ?y', 'Do you wish that ?y', 'What do you think about ?y', 'Really-- if ?y'],
    '?*x no ?*y': ['why not?', 'You are being a negative', 'Are you saying \'No\' just to be negative?'],
    '?*x I was ?*y': ['Were you really', 'Perhaps I already knew you were ?y', 'Why do you tell me you were ?y now?'],
    '?*x I feel ?*y': ['Do you often feel ?y ?', 'What other feelings do you have?'],
    '?*x 你好 ?*y': ['你好呀', '请告诉我你的问题'],
    '?*x 我想 ?*y': ['你觉得 ?y 有什么意义呢？', '为什么你想 ?y', '你可以想想你很快就可以 ?y 了'],
    '?*x 我想要 ?*y': ['?x 想问你，你觉得 ?y 有什么意义呢?', '为什么你想 ?y', '?x 觉得... 你可以想想你很快就可以有 ?y 了', '你看 ?x 像 ?y 不', '我看你就像 ?y'],
    '?*x 喜欢 ?*y': ['喜欢 ?y 的哪里？', '?y 有什么好的呢？', '你想要 ?y 吗？'],
    '?*x 讨厌 ?*y': ['?y 怎么会那么讨厌呢?', '讨厌 ?y 的哪里？', '?y 有什么不好呢？', '你不想要 ?y 吗？'],
    '?*x AI ?*y': ['你为什么要提AI的事情？', '你为什么觉得AI要解决你的问题？'],
    '?*x 机器人 ?*y': ['你为什么要提机器人的事情？', '你为什么觉得机器人要解决你的问题？'],
    '?*x 对不起 ?*y': ['不用道歉', '你为什么觉得你需要道歉呢?'],
    '?*x 我记得 ?*y': ['你经常会想起这个吗？', '除了 ?y 你还会想起什么吗？', '你为什么和我提起 ?y'],
    '?*x 如果 ?*y': ['你真的觉得 ?y 会发生吗？', '你希望 ?y 吗?', '真的吗？如果 ?y 的话', '关于 ?y 你怎么想？'],
    '?*x 我 ?*z 梦见 ?*y':['真的吗? --- ?y', '你在醒着的时候，以前想象过 ?y 吗？', '你以前梦见过 ?y 吗'],
    '?*x 妈妈 ?*y': ['你家里除了 ?y 还有谁?', '嗯嗯，多说一点和你家里有关系的', '她对你影响很大吗？'],
    '?*x 爸爸 ?*y': ['你家里除了 ?y 还有谁?', '嗯嗯，多说一点和你家里有关系的', '他对你影响很大吗？', '每当你想起你爸爸的时候， 你还会想起其他的吗?'],
    '?*x 我愿意 ?*y': ['我可以帮你 ?y 吗？', '你可以解释一下，为什么想 ?y'],
    '?*x 我很难过，因为 ?*y': ['我听到你这么说， 也很难过', '?y 不应该让你这么难过的'],
    '?*x 难过 ?*y': ['我听到你这么说， 也很难过',
                 '不应该让你这么难过的，你觉得你拥有什么，就会不难过?',
                 '你觉得事情变成什么样，你就不难过了?'],
    '?*x 就像 ?*y': ['你觉得 ?x 和 ?y 有什么相似性？', '?x 和 ?y 真的有关系吗？', '怎么说？'],
    '?*x 和 ?*y 都 ?*z': ['你觉得 ?z 有什么问题吗?', '?z 会对你有什么影响呢?'],
    '?*x 和 ?*y 一样 ?*z': ['你觉得 ?z 有什么问题吗?', '?z 会对你有什么影响呢?'],
    '?*x 我是 ?*y': ['真的吗？', '?x 想告诉你，或许我早就知道你是 ?y', '你为什么现在才告诉我你是 ?y'],
    '?*x 我是 ?*y 吗': ['如果你是 ?y 会怎么样呢？', '你觉得你是 ?y 吗', '如果你是 ?y ，那一位着什么?'],
    '?*x 你是 ?*y 吗':  ['你为什么会对我是不是 ?y 感兴趣?', '那你希望我是 ?y 吗', '你要是喜欢， 我就会是 ?y'],
    '?*x 你是 ?*y' : ['为什么你觉得我是 ?y'],
    '?*x 因为 ?*y' : ['?y 是真正的原因吗？', '你觉得会有其他原因吗?'],
    '?*x 我不能 ?*y': ['你或许现在就能 ?*y', '如果你能 ?*y,会怎样呢？'],
    '?*x 我觉得 ?*y': ['你经常这样感觉吗？', '除了到这个，你还有什么其他的感觉吗？'],
    '?*x 我 ?*y 你 ?*z': ['其实很有可能我们互相 ?y'],
    '?*x 你为什么不 ?*y': ['你自己为什么不 ?y', '你觉得我不会 ?y', '等我心情好了，我就 ?y'],
    '?*x 好的 ?*y': ['好的', '你是一个很正能量的人'],
    '?*x 嗯嗯 ?*y': ['好的', '你是一个很正能量的人'],
    '?*x 不嘛 ?*y': ['为什么不？', '你有一点负能量', '你说 不，是想表达不想的意思吗？'],
    '?*x 不要 ?*y': ['为什么不？', '你有一点负能量', '你说 不，是想表达不想的意思吗？'],
    '?*x 有些人 ?*y': ['具体是哪些人呢?'],
    '?*x 有的人 ?*y': ['具体是哪些人呢?'],
    '?*x 某些人 ?*y': ['具体是哪些人呢?'],
    '?*x 每个人 ?*y': ['我确定不是人人都是', '你能想到一点特殊情况吗？', '例如谁？', '你看到的其实只是一小部分人'],
    '?*x 所有人 ?*y': ['我确定不是人人都是', '你能想到一点特殊情况吗？', '例如谁？', '你看到的其实只是一小部分人'],
    '?*x 总是 ?*y': ['你能想到一些其他情况吗?', '例如什么时候?', '你具体是说哪一次？', '真的---总是吗？'],
    '?*x 一直 ?*y': ['你能想到一些其他情况吗?', '例如什么时候?', '你具体是说哪一次？', '真的---总是吗？'],
    '?*x 或许 ?*y': ['你看起来不太确定'],
    '?*x 可能 ?*y': ['你看起来不太确定'],
    '?*x 他们是 ?*y吗？': ['你觉得他们可能不是 ?y？'],
    '?*x': ['很有趣', '请继续', '我不太确定我很理解你说的, 能稍微详细解释一下吗?']
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
    return {k: ' '.join(v) if isinstance(v, list) else v for k, v in patterns}

# 返回parsed_rules.get(rule[0], rule[0])返回parsed_rule中rule[0]对应的value,
# 如果parsed_rules中没有key值是rule[0], 这时返回rule[0].
# 之后继续进行下一轮迭代subsitite(rule[1:], parsed_rules)
def subsitite(rule, parsed_rules):
    if not rule: return []
    return [parsed_rules.get(rule[0], rule[0])] + subsitite(rule[1:], parsed_rules)
#######################################################################################################################

#pattern开头是'?*'且后面全是字母返回True
def is_pattern_segment(pattern):
    return pattern.startswith('?*') and all(a.isalpha() for a in pattern[2:])

#rest, saying都是空，返回True；
#rest[0]不全是字母，返回True；
#saying空，rest不空，返回False；
#rest[0] != saying[0]返回False；
# 继续迭代，直到全为空返回True
def is_match(rest, saying):
    if not rest and not saying:
        return True
    if not all(a.isalpha() for a in rest[0]):
        return True
    if rest and not saying:
        return False
    if rest[0] != saying[0]:
        return False
    return is_match(rest[1:], saying[1:])

#############################################################################################################这两个函数功能有重复

# 对于enumerate函数
# seasons = ['Spring', 'Summer', 'Fall', 'Winter']
# list(enumerate(seasons))
# [(0, 'Spring'), (1, 'Summer'), (2, 'Fall'), (3, 'Winter')]
#seg_pat= pattern[0],
# rest= pattern[1:]
#i, token in enumerate(saying):#i是saying中元素的编号，token是对应的元素
#rest[0] == token找到跟rest[0]相同的saying中的词且rest[1:]==saying之后的词，返回pattern[0]和相同词之前的saying的segment
def segment_match(pattern, saying):
    seg_pat, rest = pattern[0], pattern[1:]
    seg_pat = seg_pat.replace('?*', '?')
    if not rest: return (seg_pat, saying), len(saying) #返回元组形式((seg_pat, saying), len(saying))
    for i, token in enumerate(saying):
        if rest[0] == token and is_match(rest[1:], saying[(i + 1):]):
            return (seg_pat, saying[:i]), i
    return (seg_pat, saying), len(saying)


def pat_match_with_seg(pattern, saying):
    if not pattern or not saying: return []
    pat = pattern[0]
    if is_variable(pat):#判断是否有?匹配单个单词
        return [(pat, saying[0])] + pat_match_with_seg(pattern[1:], saying[1:])
    elif is_pattern_segment(pat):#判断?*
        match, index = segment_match(pattern, saying)#match是(seg_pat, saying)，index是len(saying)
        if len(pattern) - 1 > 0 and len(saying) - index == 0:
            return 'fail'
        return [match] + pat_match_with_seg(pattern[1:], saying[index:])
    elif pat == saying[0]:#后边继续迭代
        return pat_match_with_seg(pattern[1:], saying[1:])
    else:
        return 'fail'
########################################################################################################################################

#是中文返回True，否则返回False
def isZN(a):
    if a == '*' or a == '?' or (a >= 'a' and a <= 'z') or (a >='A' and a <= 'Z'):
        return False
    return True




#jieba分词对中文和英文都有效
# '?*x 我想吃东西 ?*y'.split()，
# ['?*x', '我想吃东西', '?*y']
import random
import jieba
def get_response(saying, rules=rule_responses):
    text = str(jieba.cut(saying, cut_all=True))
    for pat in rules:
        patspl = pat.split()#pat是rules的key值, spilt()后返回的是list类型的，
        patspll = []
        for x in patspl:
            if all(isZN(a) for a in x):
                for xx in str(jieba.cut(x, cut_all=True)).split():
                    patspll.append(xx)#中文添加进patspll=[]中
            else:
                patspll.append(x)#英文单词添加进patspll[]中
        if pat_match_with_seg(patspll, text.split()) == 'fail':#不匹配或者后边没有了就fail
            pass
        else:
            got_patterns = pat_match_with_seg(patspll, text.split())
            pat_dict = pat_to_dict(got_patterns)
            ans = random.choice(rules[pat])
            if all(a.isalpha() for a in saying):
                s = ''.join(subsitite(ans.split(), pat_dict))
                return s.replace(' ', '')
            return ' '.join(subsitite(ans.split(), pat_dict))
    pass



print(get_response('你为什么不爱他'))
print(get_response('I want Iphone'))
