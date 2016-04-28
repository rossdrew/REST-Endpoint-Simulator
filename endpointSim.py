import web
import sys
import importlib

programID = "Endpoint Simulator v0.1"
urls = ('/(.*)', 'base')

def importAllEndpointFiles(endpointDefinitions, urls):
	""" Import all python files from endpointDefinitions and 
	add their urls to the presented ones."""

	completeUrlList = ()
	for enpointFile in endpointDefinitions:
		print "Attempting to import {}".format(enpointFile)
		try:
			importlib.import_module(enpointFile)
			urlList = sys.modules[enpointFile].urls
			completeUrlList += urlList
			print "Imported {}.py presenting the endpoints {}".format(enpointFile, urlList)
		except ImportError:
			print "Cannot import {}".format(enpointFile)

	completeUrlList += urls
	return completeUrlList

#TODO Need to order these 
#So I'll want to be able to add to this and have them ordered by granualty, most fine-grained first
allUrls = importAllEndpointFiles(sys.argv[2:], urls)
print "Offering : \n{}".format(allUrls)

#Classes in 'urls' inside packages need to be prefixed with the package name, e.g. 'Test.test'
app = web.application(allUrls, locals())



################################
#  Endpoint Definition Classes #
################################

class base:        
    def GET(self, name):
        return programID

if __name__ == "__main__":
	app.run()