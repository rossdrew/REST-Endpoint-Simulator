#This file is here to be an example of an enpoint file and to be used by unit tests loading them

urls = ('/Test/(.*)', 'test')

def getURLS():
	return urls

class test:        
    def GET(self, name):
        return "Test Endpoint!"