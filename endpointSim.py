import web
import sys
import importlib
import unittest, doctest
from operator import itemgetter #sorting urls

programID = "Endpoint Simulator v1.0"
urls = ('/(.*)', 'base')

def prependPackageToClassnames(urls, packageName):
	"""Take web.py formatted url/endpoint tuples and prepend 
	a packageName to each of the endpoint classnames, e.g.

	('/Test/(.*)', 'test') becomes ('/Test/(.*)', 'Test.test')

	>>> prependPackageToClassnames(('/Test/(.*)', 'test'), 'PACKAGE')
	('/Test/(.*)', 'PACKAGE.test')
	>>> prependPackageToClassnames(('/Test/(.*)', 'test', '/Test/Test2', 'test2'), 'PACKAGE')
	('/Test/(.*)', 'PACKAGE.test', '/Test/Test2', 'PACKAGE.test2')"""
	newList = []
	for url, endpoint in zip(urls[::2], urls[1::2]):
		newList += [url, "{}.{}".format(packageName, endpoint)]
	return tuple(newList)

def importAllEndpointFiles(endpointDefinitions, urls):
	""" Import all python files from endpointDefinitions and 
	add their urls to the presented ones.

	>>> importAllEndpointFiles(['Test'], ('/existing/(.*)', 'existing'))
	Attempting to import Test
	Imported Test.py presenting the endpoints ('/Test/(.*)', 'Test.test')
	('/Test/(.*)', 'Test.test', '/existing/(.*)', 'existing')"""

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
	most fine-grained first

	>>> sortURLs(('/(.*)','base', '/a/(.*)','sub', '/a/b/(.*)','subsub'))
	('/a/b/(.*)', 'subsub', '/a/(.*)', 'sub', '/(.*)', 'base')"""
	kv = zip(urls[::2], urls[1::2]) 
	s = sorted(kv, key=itemgetter(0), reverse=True)
	sortedUrls = tuple(x for pair in s for x in pair)
	return sortedUrls

allUrls = importAllEndpointFiles(sys.argv[2:], urls)
allUrlsSorted = sortURLs(allUrls)
print "{} - Providing Endpoints :- \n{}".format(programID, allUrlsSorted)
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
	import doctest
	failed, attempted = doctest.testmod()
	if failed > 0:
		print "Script terminated: {} of {} tests failed.".format(failed, attempted)
		sys.exit()
	app.run()
