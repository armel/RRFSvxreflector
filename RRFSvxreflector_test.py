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
logged=dict()
memeIP=list()

def readlog():
    df=open("/tmp/svxreflector.log")
    i=0
    for x in f:
        e=x.split(":")
        name = e[3].strip()
        if 'Login' in x:
            log.append(x)
            logged[name]=1
        elif 'disconnected' in x:
            if 'Client' not in name:
                logged[name]=0
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
    
    # Boucle principale
    while(True):
        readlog()

        print prov
        print '-----'
        
        time.sleep(5)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        pass
