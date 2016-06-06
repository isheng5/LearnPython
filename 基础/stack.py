#!/usr/bin/env python
# -*- coding: utf-8 -*-

stack = []
def pushit():
    stack.append(raw_input('please some key:\n').strip())

def popit():
    if len(stack)==0:
        print 'can not pop an empty stack'
    else:
        print 'removed [',stack.pop(),']'

def viewstack():
    print stack

CMDs = {'u': pushit,'o':popit,'v':viewstack}

def showmenu():
    pr="""
p(U)sh
p(O)p
(V)iew
(Q)uit

enter choice:"""


while True:
    while True:
        try:
            pr = """
p(U)sh
p(O)p
(V)iew
(Q)uit

enter choice:"""
            choice = raw_input(pr).strip()[0].lower()
        except(EOFError,KeyboardInterrupt,IndexError):
            choice = 'q'

        print '\nyou picked:[%s]' % choice
        if choice not in 'uovq':
            print 'invalid opion,try again'
        else:
            break

    if choice =='q':
        break

    CMDs[choice]()


if __name__ == '__main__':
    showmenu()