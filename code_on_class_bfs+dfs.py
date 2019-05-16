#!/usr/bin/env python 
# -*- coding:utf-8 -*-
######################################################################################################################
#BFS和DFS--树结构数据遍历的两种方法

#########################################################################
#给BEIJING。。。等变量赋值
BEIJING, CHANGCHUN, MULUMUQI, WUHAN, GUNAGHZOU, SHENZHEN, BANGKOK, SHANGHAI, NEWYORK = """
BEIJING CHANGCHUN MULUMUQI WUHAN GUANGZHOU SHENZHEN BANGKOK SHANGHAI NEWYORK
""".split()

#定义用于networkx的字典connection
connection = {
    CHANGCHUN: [BEIJING],
    MULUMUQI: [BEIJING],
    BEIJING: [MULUMUQI, CHANGCHUN, WUHAN, SHENZHEN, NEWYORK],
    NEWYORK: [BEIJING, SHANGHAI],
    SHANGHAI: [NEWYORK, WUHAN],
    WUHAN: [SHANGHAI, BEIJING, GUNAGHZOU],
    GUNAGHZOU: [WUHAN, BANGKOK],
    SHENZHEN: [WUHAN, BANGKOK],
    BANGKOK: [SHENZHEN, GUNAGHZOU]
}
#利用networkx中的Graph函数，把dict链接为网络图，g = nx.Graph(graph)
import networkx as nx
#import matplotlib.pyplot as plt
graph = connection
g = nx.Graph(graph)
nx.draw(g)
#plt.show()
#这个显示连接图其实没啥用，就是展示一下
##########################################################################
#没明白这个有啥用，是啥意思
def nagivator(start, destination, connection_graph):
    pathes = [[start]]
    seen = set()

    while pathes:
        path = pathes.pop(0)
        froniter = path[-1]
        if froniter in seen: continue
        successors = connection_graph[froniter]
        for s in successors:
            if s == destination:
                path.append(s)
                return path
            else:
                pathes.append(path + [s])
            #    print(pathes)
             #   print('################################')

        #pathes = sorted(pathes, key=len) # 最小换成
        seen.add(froniter)
       # print(pathes)
       # print('########################################')

##########################################################################

#广度优先
def nagivator_bfs(start, destination, connection_graph):
    pathes = [start]
    seen = set()

    while pathes:
        froniter = pathes.pop(0)
        if froniter in seen: continue
        successors = connection_graph[froniter]
       # print('standing on {} Looking forward {}'.format(froniter, successors))

        pathes = pathes + successors
        seen.add(froniter)
#pathes = pathes + successors保证了下一轮的起始节点是继续之前的pathes


#深度优先
def nagivator_dfs(start, destination, connection_graph):
    pathes = [start]
    seen = set()

    while pathes:
        froniter = pathes.pop(0)#删除pathes第一个元素
       # print('pathes.pop(0):', pathes)
        if froniter in seen: continue
        successors = connection_graph[froniter]#查找上一轮结束时pathes的第一个元素的连接节点（城市）
      #  print('successors:', successors)
        print('standing on {} Looking forward {}'.format(froniter, successors))

        pathes = successors + pathes
      #  print('successors + pathes:', pathes)
        seen.add(froniter)

        # 相比于广度优先，深度优先的pathes起始应该是下一层次的节点，
        # 所以有successors + pathes而不是广度优先中的pathes + successors
        # 把上一轮得到pathes的第一个元素添加到seen（set）中
        #set.add()不添加已有元素，添加顺序随机







