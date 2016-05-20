import web
import sys
import importlib
from operator import itemgetter #sorting urls

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

def sortURLs(urls):
	""" Order URLs by how specific they are so that they 
	are matched in the correct order, ordered by granualty, 
	most fine-grained first"""
	kv = zip(urls[::2], urls[1::2]) 
	s = sorted(kv, key=itemgetter(0), reverse=True)
	sortedUrls = tuple(x for pair in s for x in pair)
	return sortedUrls

allUrls = importAllEndpointFiles(sys.argv[2:], urls)
allUrlsSorted = sortURLs(allUrls)
print "Offering : \n{}".format(allUrlsSorted)

#Classes in 'urls' inside packages need to be prefixed with the package name, e.g. 'Test.test'
app = web.application(allUrls, locals())


################################
#  Endpoint Definition Classes #
################################

class base:        
    def GET(self, name):
        return programID

################
#  Entry Point #
################

if __name__ == "__main__":
	app.run()
