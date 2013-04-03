#!/usr/bin/env python
import re
import sys
import codecs
LOG = '/mnt/dayz/server_console.log'

# Matches an [H]H:MM:SS time stamp at the beginning of a log entry, the players name, and their activity
#                                    |  0         :    38  :   13                  Player EarlDribbles                    connected               (id=62660166).
join_part_activity = re.compile(r'(?P<timestamp>( |[0-9])?[0-9]:[0-9]{2}:[0-9]{2}) Player (?P<player>.*) (?=(?P<activity>(disconnected|connected)))')

# First byte is the Byte-Order-Marker
#
# fucking Windows-using assholes....
f = codecs.open(LOG, 'r', 'utf-8')
BOM = f.read(1)

# Nobody is here, until the log file tells me different
logged_in = 0

for row in f.readlines():
    r = row.strip()
    state_match = join_part_activity.search(r)
    if state_match:
        state_match_parts = state_match.groupdict()
        if state_match_parts['activity'] == 'disconnected':
            logged_in -= 1
        else:
            logged_in += 1

# 'rrdupdate' expects new entries in the format: N:value (where 'N' is
# accepted to mean "NOW")
RRD_UPDATE = "N:%s" % logged_in

sys.stdout.write(RRD_UPDATE)

f.close()
