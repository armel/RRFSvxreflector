#!/usr/bin/env python2
# -*- coding: utf-8 -*-

'''
RRFSentinel
Learn more about RRF on https://f5nlg.wordpress.com
73 & 88 de F4HWN Armel
'''

import settings as s

import time

links=list()
ips=list()
log=list()
bip=dict()
prov=dict()
memeIP=list()

def fctSort(e):
    """ Cette fonction renvoie le nom du link afin de trier la liste. """
    n=e.split(":")
    return n[3].strip()

def readbip():
    """ readbip lit le fichier BIP.txt pour alimentre le dictionnary bip"""
    f=open("/root/BIP.txt",'r')
    for x in f:
      e=x.split(":")
      bip[e[0]]=e[1]
    f.close()

def readlog():
    with open('/tmp/svxreflector.log') as f:
        for line in f:
            if 'Login' in line:
                element = line.split(':')
                prov[element[3].strip()] = element[4][15:]

    with open('/tmp/BIP.txt') as f:
        for line in f:
            element = line.split(':')
            if element[0] not in prov:
                prov[x]='---.---.---.---'

    for key in sorted(prov.keys()):
        links.append(key)
        ips.append(prov[key])

def main():
    
    readlog()

    for l in links:
        print l

    for i in ips:
        print i     

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        pass
