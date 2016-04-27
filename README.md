#endpointSim

Python script to spin up some simple REST endpoints for simulating services. 

#Usage

To spin up an endpoint, create a Python script in the same directory, make sure there is a [web.py](http://webpy.org/) style URL mapping/class tuple structure to define the mapping and what endpoint class it should point to.
The only difference here is that the class name needs to be prefixed by the package name, like so:-

```python
urls = ('/Test', 'Test.test')
```

Add (as in [web.py](http://webpy.org/)) a class and add a method with the name of the method type of the expected request, e.g. _GET_ and specify behaviour.

```python
class test:        
    def GET(self):
    	print "TEST HIT"
        return "Test Endpoint!"
```

It is run by running the script followed by the port it should run on, followed by a list of endpoint packages you wish to spin up, e.g.

```
python endpointSim.py 8081 Test
```

#Limitations

So far it's a little rough and very limited.  For example, in [web.py](http://webpy.org/), the tuple _urls_ needs to be ordered by most specific first.  Otherwise all URLs will match '_/(.*)_' and all be routed to the _base_ class.  I'll need to maybe write an ordering method to make sure classes don't interfere with each other.
