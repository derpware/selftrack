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
