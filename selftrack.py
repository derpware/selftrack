import json
import eeml
import config
import time

def noOfOpenTabs():
	json_data=open(MOZILLA_SESSIONSTORE)
	data = json.load(json_data)
	tabs=0;
	for window in data["windows"]:
		tabs = tabs + len(window["tabs"])
	return tabs

def temperature():
	temperature = open("/proc/acpi/ibm/thermal").read().split()[1]
	return temperature

def loadavg():
	loadavg = open("/proc/loadavg").read().split()[0]
	return loadavg

feed = eeml.Pachube(config.API_URL, config.API_KEY)
while 1 :
	time.sleep(30)
	update_data = []
	update_data.append(eeml.Data("browser.tabs", noOfOpenTabs()))
	update_data.append(eeml.Data("cpu.temperature", temperature(), unit=eeml.Celsius()))
	update_data.append(eeml.Data("cpu.loadavg", loadavg()))

	feed.update(update_data)
	try:
		feed.put()
	except Exception, err:
		print "Couldn't send data to pachube: ", err
