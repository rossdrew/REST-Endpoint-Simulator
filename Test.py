
print "Test imported..."

urls = ('/Test/(.*)', 'test')

def getURLS():
	return urls

class test:        
    def GET(self, name):
        return "Test Endpoint!"