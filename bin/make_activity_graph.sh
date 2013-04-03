#!/bin/bash

RRD_OUTPUT=/srv/dayz/data/players.png
RRD_FILE=/srv/dayz/data/activity.rrd
VLABEL="--vertical-label 'connected players'"
FORMAT="-a PNG"
TITLE="--title \"Logged in Players Over Time\""

rrdtool graph ${RRD_OUTPUT} ${FORMAT} --title "Connected players (last day)" \
    -w 600 -h 150 \
    -c BACK#000000 -c CANVAS#000000 -c GRID#C0C0C0 -c FONT#C0C0C0 \
    --vertical-label "connected players" \
    DEF:players=${RRD_FILE}:players_logged_in:MAX \
    LINE1:players#00FF00
