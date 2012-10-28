import subprocess
import config
from json import load


def noOfOpenTabs():
	json_data=open(config.MOZILLA_SESSIONSTORE)
	data = load(json_data)
	json_data.close()
	tabs = 0
	for window in data["windows"]:
		tabs = tabs + len(window["tabs"])
	return tabs

def temperature():
	temperature = 0
	return temperature

def loadavg():
	loadavg = -1
	return loadavg
	
def memory():
	memory = -1
	return memory

def swap():
	swap = -1
	return swap

def processes():
	processes = subprocess.check_output("ps aux | wc -l", shell=True)
	return processes
