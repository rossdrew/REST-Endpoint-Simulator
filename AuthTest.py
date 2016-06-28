import web
import base64

urls = ('/TestAuth/(.*)', 'testAuth')

def getURLS():
  return urls

allowed_users = ( #XXX Only works with two entries for some reason
    ('test','test'),
    ('test','test')
)

class testAuth:
    def GET(self, name):
        auth = web.ctx.env.get('HTTP_AUTHORIZATION')
        auth_success = False

        if auth is not None:
            username, password = base64.decodestring(auth[6:]).split(':')
            print "AUTH: {} -> '{}':'{}'".format(auth, username, password)

            if (username, password) in allowed_users:
                auth_success = True
        else:
            print "No username, password supplied!"

        if not auth_success:
            web.header('WWW-Authenticate','Basic realm="Test Authentication"')
            web.header('Cache-Control','no-cache,no-store,max-age=0,must-revalidate')
            web.header('Connection','keep-alive')
            web.header('Expires','0')
            web.header('Pragma','no-cache')
            web.header('X-XSS-Protection','1; mode=block')
            web.ctx.status = '401 Unauthorized'
            return None

        web.header('Content-Type', 'application/json') 
        return "{\"Response\":\"OK\"}"
