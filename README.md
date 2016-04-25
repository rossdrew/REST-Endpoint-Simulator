#endpointSim

Python script to spin up some simple endpoints for simulating services. 

#Usage

To spin up an endpoint, create a Python script in the same directory, make sure there is a web.py style URL mapping/class tuple structure to define the mapping and what class it should point to.

```python
urls = ('/Test', 'Test.test')
```

Add (as in webpy) a class and add a method with the name of the method type of the expected request, e.g. _GET_ and specify behaviour.

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