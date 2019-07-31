#!/usr/bin/env python2
# -*- coding: utf-8 -*-

'''
RRFSentinel
Learn more about RRF on https://f5nlg.wordpress.com
73 & 88 de F4HWN Armel
'''

import settings as s


# lecture du svxreflector.log
'''
def readlog():    
    f = open('/tmp/svxreflector.log')
    i = 0
    for x in f:
        e = x.split(':')
        name = e[3].strip()
        if 'Login' in x:
            s.log.append(x)

    f.close()

    lastName = ''
    name = ''
    i = 0
    for x in s.log:
        e = x.split(':')
        name=e[3].strip()

        print name, e[4][15:]

        if name != lastName:
            s.prov[name] = e[4][15:]
            lastName=name
            i += 1
    i = 0
    for key in sorted(s.prov.keys()) :
        s.links.append(key)
        s.ips.append(s.prov[key])
        i += 1
'''

def readlog():
    with open('/tmp/svxreflector.log') as f:
        line = f.readlines()
        if 'Login' in line:
            print line
            element = line.split(':')
            s.prov[element[3].strip()] = element[4][15:]

