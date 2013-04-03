#!/bin/bash

RRD_FILE=/srv/dayz/data/activity.rrd
INSPECTER=/srv/dayz/bin/inspect.py

# Get the timestamp:value to feed to rrdupdate
UPDATE_VALUE=`${INSPECTER}`

rrdtool update ${RRD_FILE} ${UPDATE_VALUE}
