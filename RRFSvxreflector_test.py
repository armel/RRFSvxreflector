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
    f=open("/tmp/svxreflector.log")
    i=0
    for x in f:
        e=x.split(":")
        name = e[3].strip()
        if 'Login' in x:
            log.append(x)

    f.close()
    log.reverse()
    log.sort(key=fctSort)
    
    lastName=""
    name=""
    i=0
    for x in log:
        e=x.split(":")
        name=e[3].strip()
        if name != lastName:
            prov[name]=e[4][15:]
            lastName=name
            i+=1
    readbip()
    for x in bip:
        if x not in prov:
            prov[x]="---.---.---.---"
    i=0
    for key in sorted(prov.keys()) :
        links.append(key)
        ips.append(prov[key])
        i+=1

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
