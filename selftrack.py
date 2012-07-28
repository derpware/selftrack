#!/usr/bin/env python

#-*- coding: utf-8 -*-

from time import sleep
from json import load
import config
import eeml
import subprocess

def noOfOpenTabs():
	json_data=open(config.MOZILLA_SESSIONSTORE)
	data = load(json_data)
	json_data.close()
	tabs = 0
	for window in data["windows"]:
		tabs = tabs + len(window["tabs"])
	return tabs

def temperature():
	inputFile = open("/proc/acpi/ibm/thermal")
	temperature = inputFile.read().split()[1]
	inputFile.close()
	return temperature

def loadavg():
	inputFile = open("/proc/loadavg")
	loadavg = inputFile.read().split()[0]
	inputFile.close()
	return loadavg
	
def memory():
	memory = subprocess.check_output("free -m | grep Mem | awk '{print $3}'", shell=True)
	return memory

def swap():
	swap = subprocess.check_output("free -m | grep Swap | awk '{print $3}'", shell=True)
	return swap

def processes():
	processes = subprocess.check_output("ps aux | wc -l", shell=True)
	return processes

feed = eeml.Pachube(config.API_URL, config.API_KEY)
while 1 :
	sleep(30)
	update_data = []
	update_data.append(eeml.Data("browser.tabs", noOfOpenTabs()))
	update_data.append(eeml.Data("cpu.temperature", temperature(), unit=eeml.Celsius()))
	update_data.append(eeml.Data("cpu.loadavg", loadavg()))
	update_data.append(eeml.Data("os.memory", memory()))
	update_data.append(eeml.Data("os.swap", swap()))
	update_data.append(eeml.Data("os.processes", processes()))
	

	feed.update(update_data)
	try:
		feed.put()
	except Exception, err:
		print "Couldn't send data to pachube: ", err
