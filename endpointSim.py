import web
import sys
import importlib
from operator import itemgetter #sorting urls

programID = "Endpoint Simulator v0.1"
urls = ('/(.*)', 'base')

def prependPackageToClassnames(urls, packageName):
	"""Take web.py formatted url/endpoint tuples and prepend 
	a packageName to each of the endpoint classnames, e.g.

	('/Test/(.*)', 'test') becomes ('/Test/(.*)', 'Test.test')
	
	XXX There's probably a more Pythony way to do this"""
	lst = list(urls)
	for i in xrange(1, len(lst), 2):
  		lst[i] = packageName + "." + lst[i]

	return tuple(lst)

def importAllEndpointFiles(endpointDefinitions, urls):
	""" Import all python files from endpointDefinitions and 
	add their urls to the presented ones."""

	completeUrlList = ()
	for endpointFile in endpointDefinitions:
		print "Attempting to import {}".format(endpointFile)
		try:
			importlib.import_module(endpointFile)
			urlList = sys.modules[endpointFile].urls
			urlList = prependPackageToClassnames(urlList, endpointFile)
			completeUrlList += urlList
			print "Imported {}.py presenting the endpoints {}".format(endpointFile, urlList)
		except ImportError:
			print "Cannot import {}".format(endpointFile)

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

#TODO: Maybe remove the need for this by prepending it on import?
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
