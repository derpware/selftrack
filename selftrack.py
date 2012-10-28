#!/usr/bin/env python

#-*- coding: utf-8 -*-

from time import sleep
import config
import eeml
import sys

if sys.platform.startswith("linux"):
	import linux as collector
elif sys.platform == "darwin":
	import macosx as collector
else:
	print >> sys.stderr, "Platform not supported. Aborting"
	sys.exit(1);

feed = eeml.Pachube(config.API_URL, config.API_KEY)
while 1 :
	sleep(30)
	update_data = []
	update_data.append(eeml.Data("browser.tabs", collector.noOfOpenTabs()))
	update_data.append(eeml.Data("cpu.temperature", collector.temperature(), unit=eeml.Celsius()))
	update_data.append(eeml.Data("cpu.loadavg", collector.loadavg()))
	update_data.append(eeml.Data("os.memory", collector.memory()))
	update_data.append(eeml.Data("os.swap", collector.swap()))
	update_data.append(eeml.Data("os.processes", collector.processes()))
	

	feed.update(update_data)
	try:
		feed.put()
	except Exception, err:
		print "Couldn't send data to pachube: ", err
