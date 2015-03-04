#!/usr/bin/env python2.7
from datetime import *

def seconds_until_midnight():
    tomorrow = date.today() + timedelta(1)
    midnight = datetime.combine(tomorrow, time())
    now = datetime.now()
    return (midnight - now).seconds
    
def seconds_until_nexthour():
    nexthour = datetime.now() + timedelta(0,0,0,0,0,1)
    nexthour = datetime.combine(nexthour, time())
    now = datetime.now()
    return (nexthour - now).seconds

secsToMidnight = seconds_until_midnight()
print "Seconds till midnight: %d" % secsToMidnight

secsToNextHour = seconds_until_nexthour()
print "Seconds till next hour: %d" % secsToNextHour
