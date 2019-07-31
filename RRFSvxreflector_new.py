#!/usr/bin/env python2
# -*- coding: utf-8 -*-

'''
RRFSentinel
Learn more about RRF on https://f5nlg.wordpress.com
73 & 88 de F4HWN Armel
'''

import settings as s

import time

def readlog():
    with open('/tmp/svxreflector.log') as f:
        for line in f:
            if 'Login' in line:
                element = line.split(':')
                s.prov[element[3].strip()] = element[4][15:]

def main():
    
    # Boucle principale
    while(True):
        readlog()

        print s.prov
        print '-----'
        
        time.sleep(5)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        pass
