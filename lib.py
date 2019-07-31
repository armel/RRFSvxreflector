#!/usr/bin/env python2
# -*- coding: utf-8 -*-

'''
RRFSentinel
Learn more about RRF on https://f5nlg.wordpress.com
73 & 88 de F4HWN Armel
'''

import settings as s


# Cette fonction renvoie le nom du link afin de trier la liste.
def fctSort(e):
    n = e.split(':')
    return n[3].strip()

# readbip lit le fichier BIP.txt pour alimentre le dictionnary bip
def readbip():
    f = open('/root/BIP.txt','r')
    for x in f:
      e = x.split(":")
      s.bip[e[0]] = e[1]
    f.close()

# lecture du svxreflector.log
def readlog():    
    f = open('/tmp/svxreflector.log')
    i = 0
    for x in f:
        e = x.split(':')
        name = e[3].strip()
        if 'Login' in x:
            s.log.append(x)
            s.logged[name] = 1
        elif 'disconnected' in x:
            if 'Client' not in name:
                s.logged[name] = 0
    f.close()
    s.log.reverse()
    s.log.sort(key = fctSort)

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
    readbip()
    for x in s.bip:
        if x not in s.prov:
            s.prov[x]='---.---.---.---'
    i = 0
    for key in sorted(s.prov.keys()) :
        s.links.append(key)
        s.ips.append(s.prov[key])
        i += 1
