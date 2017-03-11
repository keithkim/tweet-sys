#!/usr/bin/env python
#
# tweet-sys.py
# 
#
import sys, syslog

from TwitterAPI import TwitterAPI
from MiscServices import MiscServices

args_num = len(sys.argv) - 1

if args_num <= 0:
    print "Error: pass argument of 'start', 'shutdown', 'status'"
    sys.exit(1)

arg1 = sys.argv[1].upper()
#print "arg=%s" % arg1

sc = MiscServices()
ip = sc.getExternalIp()
host = sc.getHostName()
temp = sc.getTemperature()
dt = sc.getCurrentDateTime()
tz = sc.getTimezone()

# Ex) "[STARTUP:rpiweb] (time timezone) IP=1.2.3.4, Temp=51'c
msg = "[%s:%s @ %s %s] IP=%s, Temp=%s" % (arg1, host, dt, tz, ip, temp)
print msg
syslog.syslog(msg)

tw = TwitterAPI()
tw.tweet(msg)
