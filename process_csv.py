#!/usr/bin/env python
#-*- coding:utf-8 -*-


import csv
import string
from names import NAMES, E_Men, F_Men, ORDER
import time




def edits1(word):

    if len(word) < 4:
        return set([word])

    splits     = [(word[:i], word[i:]) for i in range(len(word) + 1)]
    deletes    = [a + b[1:] for a, b in splits if b]
    transposes = [a + b[1] + b[0] + b[2:] for a, b in splits if len(b)>1]
    replaces   = [a + c + b[1:] for a, b in splits for c in string.lowercase if b]
    inserts    = [a + c + b     for a, b in splits for c in string.lowercase]
    return set(deletes + transposes + replaces + inserts)


for k in NAMES.keys():
    tmp = set([])
    for i in NAMES[k]['en']:
        tmp |= edits1(i)
    NAMES[k]['en'] = tmp

def get_letters(st):
    return (''.join([s for s in st if s in string.letters or s.isnumeric()])).lower()


def get_ok_ones(st):
    st = st.decode('gbk')
    st += u'###' + get_letters(st)
    for o in ORDER:
        for s in (list(NAMES[o]['en']) + NAMES[o]['zh']):
            if st.find(s) != -1:
                yield o
                break


def print_for_check(*args):
    for st in args:
        print ''
        print st
        print '*'*10
        for i in get_ok_ones(st):
            print i,
        print ''
        print ''


def get_first_match(st):
    min_match_place, match_st = 9999, u"最初什么都没匹配到"
    st = st.decode('gbk')
    st += u'###' + get_letters(st)
    for o in ORDER:
        for s in (list(NAMES[o]['en']) + NAMES[o]['zh']):
            place = st.find(s)
            if place != -1:
                if place < min_match_place:
                    min_match_place, match_st = place, o
    return match_st



def main():
    ans = []
    reader = csv.reader(open("Yida_Answer_Sheet.csv"))
    writer = csv.writer(open("output.csv", 'w'))
    

    for i, row in enumerate(reader):
        if i == 0:
            new_cols = [(u"P1Q1(text)(%s)" % j).encode('gbk') for j in ORDER] +  [(u"P2Q1(text)(%s)" % j).encode('gbk') for j in ORDER]
            new_cols.insert(len(ORDER), E_Men[0])

        else:
            """
            print_for_check(row[31], row[32])
            """
            new_cols = []
            first_match = get_first_match(row[F_Men[1]])
            
            for j in ORDER:
                new_cols.append(1 if j == first_match else 0)
            new_cols.append(row[E_Men[1]])

            ok_ones = [k for k in get_ok_ones(row[E_Men[1]])]
            for j in ORDER:
                new_cols.append(1 if j in ok_ones else 0)

            
        ans.append(row[:F_Men[1]+1] + new_cols + row[E_Men[1]+1:])


        

    writer.writerows(ans)

if __name__ == '__main__':
    start = time.clock()
    print "TextQ Processor Running Now!!"
    print "Please check your parameters, are they ready??"
    main()
    secs = int(time.clock() - start)
    print "Overall Time Cost:", secs, "secs"
    print "Any bug please contact me ---> Dumas Dong"

