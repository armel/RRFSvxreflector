#!/usr/bin/env python2
# -*- coding: utf-8 -*-

'''
RRFSentinel
Learn more about RRF on https://f5nlg.wordpress.com
73 & 88 de F4HWN Armel
'''

import settings as s

def readlog():    
    f = open('/tmp/svxreflector.log')

    print f.tell()

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

        if name != lastName:
            s.prov[name] = e[4][15:]
            lastName=name
            i += 1
    i = 0
    for key in sorted(s.prov.keys()) :
        s.links.append(key)
        s.ips.append(s.prov[key])
        i += 1

def main():
    
    # Boucle principale
    while(True):
        readlog()

        print s.prov

        exit(0)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        pass
