import httplib, urllib
import config
 
def push(data):
	fields = {}
	
	for idx,value in enumerate(data.values(), start=1):
		fields["field" + str(idx)] = value
		
	fields["key"] = config.THINGSPEAK_API_KEY
	params = urllib.urlencode(fields)
	headers = {"Content-type": "application/x-www-form-urlencoded","Accept": "text/plain"}
	
	conn = httplib.HTTPConnection("api.thingspeak.com:80")
	try:
		conn.request("POST", "/update", params, headers)	
		response = conn.getresponse()
		data = response.read()
	except Exception, err:
		print "Couldn't send data to ThingSpeak: ", err
	conn.close()
