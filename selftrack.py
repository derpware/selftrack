#!/usr/bin/env python

#-*- coding: utf-8 -*-

from time import sleep
import config
import sys

import xively
import thingspeak

if sys.platform.startswith("linux"):
	import linux as collector
elif sys.platform == "darwin":
	import macosx as collector
else:
	print >> sys.stderr, "Platform not supported. Aborting"
	sys.exit(1);

xively.init()

while 1 :
	data = {}
	data["browser.tabs"] = collector.noOfOpenTabs()
	data["cpu.temperature"] = collector.temperature()
	data["cpu.loadavg"] = collector.loadavg()
	data["os.memory"] = collector.memory()
	data["os.swap"] = collector.swap()
	data["os.processes"] = collector.processes()

	thingspeak.push(data)
	xively.push(data)
	
	sleep(30)

