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
	conn.request("POST", "/update", params, headers)
	
	response = conn.getresponse()
	print response.status, response.reason
	data = response.read()
	conn.close()
