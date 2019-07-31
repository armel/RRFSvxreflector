#!/bin/sh

PATH_SCRIPT='/opt/RRFSentinel/RRFSentinel.py'
PATH_LOG='/tmp'
PATH_PID='/tmp'

case "$1" in
    start)
        echo "Starting RRFSentinel"
        nohup python $PATH_SCRIPT --salon RRF_V1 --declenchement 3 --plage 5 --ban 5 --fair-use 3 --log-path $PATH_LOG > $PATH_LOG/RRFSentinel.log 2>&1 & echo $! > $PATH_PID/RRFSentinel.pid
        ;;
    stop) 
        echo "Stopping RRFSentinel"
        kill `cat $PATH_PID/RRFSentinel.pid`
        ;;
    esac