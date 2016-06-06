#!/usr/bin/env python
# -*- coding: utf-8 -*-

a = 100
if a >= 0:
    print a
    a = a-1
else:
    print 0

print 3 > 2
print True and True
print not True
classmates = ['Michael', 'Bob', 'Tracy']
print classmates[0]
print classmates[-1]
addclass = raw_input()
classmates.append(addclass)
print classmates[-1]
classmates.pop(-1)
print classmates[-1]
print len(classmates)
