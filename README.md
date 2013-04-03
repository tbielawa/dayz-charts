What is this?
=============

Nothing major. Just some crappy scripts I put together to make a chart
of players logged into [abutcher](https://github.com/abutcher)'s
[Day-Z server](http://afrolegs.com).

Why should I care?
==================

You probably shouldn't. But if you like pretty pictures and stuff then
this may appeal to you:

![Demo chart](https://raw.github.com/tbielawa/dayz-charts/master/images/abutcher-demo.png)

That's it, a line? Peace -- I'm out
===================================

I don't blame you.

Maybe I'll add a couple more charts here some time. Just depends on if
I get motivated.


I want to try it!
=================

You're still reading? *I'm flattered*. Here's the deal

* As far as I know, you need to be using hosting from http://dayz.st/
  Maybe you don't, I have no idea if other hosting solutions format
  their logs the same way.

* Mount your server logs, the admin panel on dayz.st will give you the
  info for this. You probably need to install ``fuse`` (filesystem in
  userspace) first. Put something like this in your ``/etc/fstab``
  then run ``mkdir -p /mnt/dayz; mount -a``:

```
curlftpfs#ftp://YOURNAME:YOURPASSWORD@HOSTNAMEORIP/ /mnt/dayz fuse defaults 0 0
```

* Install stuff (for making pretty pictures!):

```
# yum -y install rrdtool
```

* Clone this honkey:

```
# cd /srv
# git clone git://github.com/tbielawa/dayz-charts.git dayz
```

* Don't have root? *Deal with it*. Or clone the repo somewhere else
  and adjust the paths in the scripts in the ``bin`` directory. It's
  up to you.

* Create the initial RRD file:

```
# ./bin/create_rrd.sh
```

* Start filling it with data. If you're a lamer you can just run
  ``./bin/update_activity_chart.sh`` in a ``while`` loop:

```
# while [ true ]; do ./bin/inspect.py ; ./bin/update_activity_chart.sh; sleep 60; done
```

* If you're cool you could put it in a cron job. The RRD file is
  configured to expect data every 60 seconds. So the cron job should
  be pretty simple:

```
# EDITOR=emacs crontab -e
SHELL=/bin/bash
* * * * *    /srv/dayz/bin/update_activity_chart.sh
```

* And what of teh sweet pics I promised? As above, ``lame = while
  loop``, ``cool = cron job``. You can update the chart as
  (in)frequently as you wish. Here's how to update it every 5 minutes
  (showing crontab output as if you ran the last step already):

```
# EDITOR=emacs crontab -e
SHELL=/bin/bash
* * * * *    /srv/dayz/bin/update_activity_chart.sh
# This next step is new new new!!!
*/5 * * * *  /srv/dayz/bin/make_activity_graph.sh
```
