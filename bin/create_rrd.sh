#!/bin/bash

rrdtool create data/activity.rrd --step 60 \
    DS:players_logged_in:GAUGE:300:0:U \
    RRA:MAX:0.75:5:4032
