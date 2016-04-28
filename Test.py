
print "Test imported..."

urls = ('/Test/(.*)', 'Test.test')

def getURLS():
	return urls

class test:        
    def GET(self):
    	print "TEST HIT"
        return "Test Endpoint!"