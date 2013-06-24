import config
import eeml
import eeml.unit
import eeml.datastream

feed = None

def init():
	global feed
	feed = eeml.datastream.Cosm(config.XIVELY_API_URL, config.XIVELY_API_KEY)

def push(data):
	update_data = []
	
	for key,value in data.iteritems():
		update_data.append(eeml.Data(key, value))
	
	feed.update(update_data)
	try:
		feed.put()
	except Exception, err:
		print "Couldn't send data to pachube: ", err
