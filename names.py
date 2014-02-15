#!/usr/bin/env python
#-*- coding:utf8 -*-

import csv
from collections import OrderedDict

F_Men = [u'P1Q1(text)', 23] #这里
E_Men = [u'P2Q1(text)', 24] # 这里

schema_reader = csv.reader(open("Yida_Mapping_Schema.csv")) #这里

##for i, line in enumerate(schema_reader):
##    for entries in line:
##        print entries.decode('gbk')
##        print entries

ORDER = []
for num, line in enumerate(schema_reader):
    ORDER.append(line[0].decode('gbk'))
    
import re
 
#判断字符串是否有中文    
def has_chinese_charactar(content):
    '''
    python判断是否是中文需要满足u'[\u4e00-\u9fa5]+'，
    需要注意如果正则表达式的模式中使用unicode，那么
    要匹配的字符串也必须转换为unicode，否则肯定会不匹配。
    '''
    iconvcontent = unicode(content)
    zhPattern = re.compile(u'[\u4e00-\u9fa5]+')
    match = zhPattern.search(iconvcontent)
    res = False
    if match:
        res = True
    return res

##print has_chinese_charactar(ORDER[2])

NAMES = {}
schema_reader = csv.reader(open("Yida_Mapping_Schema.csv"))
for num, line in enumerate(schema_reader):
    en = []
    zh = []
    Lan = {'zh':zh, 'en':en}
    for i, entries in enumerate(line):
        if i != 0 and has_chinese_charactar(entries.decode('gbk')):
            zh.append(entries.decode('gbk'))
##            print zh
        elif i != 0 and entries != '' and entries != 'zh' and entries != 'en':
            en.append(entries.decode('gbk'))
            
    Lan['zh'] = zh
    Lan['en'] = en
    NAMES[ line[0].decode('gbk')] = Lan
##    print 'en'
##    for i in en: print i
##    print 'zh'
##    for i in zh: print i
##    print '=='*10
##    for i in Names: print 'Names[%s] = ' % i, Names[i]
                       

        
##NAMES = {
##    u"可口可乐":{
##        'e':
##            [u"kekoukele", # Pinyin
##            u"cococola",   # English Name
##            u"Coke",       # Acronym
##            u"kou",
##             u"kekou"],       # In-group Identifier --- Not Suggested
##        'zh':
##            [u"可口",
##            u"口"],
##    },
##    u"百事可乐":{
##        'e':
##            [u"baishikele",
##            u"pepsi",
##            u"baishi",
##            u"baishi"],
##        'zh':
##            [u"百事",
##            u"白事",
##            u"白石"],
##    },
##    u"零度可乐":{
##        'e':
##            [u"lindukele",
##            u"zero",
##            u"lindu",
##            u"lin"],
##        'zh':
##            [u"零度",
##            u"零"],
##    },
##    u"百事极度":{
##        'e':
##            [u"baishijidu",
##            u"jd",
##            u"jidu",
##            u"jindu"],
##        'zh':
##            [u"极度",
##            u"极"],
##    },
##    u"雪碧":{
##        'e':
##            [u"xuebi",
##            u"sprite",
##            u"xvebi",
##            u"xue"],
##        'zh':
##            [u"雪",
##            u"碧"],
##    },
##    u"七喜":{
##        'e':
##            [u"qixi",
##            u"7up",
##            u"qi"],
##        'zh':
##            [u"七",
##            u"喜"],
##    },
##    u"美年达":{
##        'e':
##            [u"meinianda",
##            u"mirinda",
##            u"mnd",
##            u"mei"],
##        'zh':
##            [u"美",
##            u"年"],
##    },
##    u"芬达":{
##        'e':
##            [u"fenda",
##            u"fanta",
##            u"fengda",
##            u"feng",
##            u"fen"],
##        'zh':
##            [u"芬"],
##    },
##    u"激浪":{
##        'e':
##            [u"jilang",
##            u"mountaindew",
##            u"jilan",
##            u"lang",
##            u"lan"],
##        'zh':
##            [u"激"],
##    },
##    u"娃哈哈非常可乐":{
##        'e':
##            [u"wahahafeichangkele",
##            u"feichangkele",
##            u"feichang",
##            u"fei"],
##        'zh':
##            [u"非常"],
##    },
##    u"娃哈哈苏打水":{
##        'e':
##            [u"wahahasudashui",
##            u"wahahasoda",
##            u"suda",
##            u"su"],
##        'zh':
##            [u"苏打"],
##    },
##    u"娃哈哈格瓦斯":{
##        'e':
##            [u"wahahagewasi",
##            u"gewasi",
##            u"gewasi",
##            u"ge"],
##        'zh':
##            [u"格"],
##    },
##    u"汇源果汁果乐":{
##        'e':
##            [u"huiyuanguozhiguole",
##            u"huiyuan",
##            u"huiyuan",
##            u"hui"],
##        'zh':
##            [u"汇源"],
##    },
##    u"健力宝":{
##        'e':
##            [u"jianlibao",
##            u"jianlibao",
##            u"jlb",
##            u"jian",
##            u"jiang"],
##        'zh':
##            [u"健"],
##    },
##}
