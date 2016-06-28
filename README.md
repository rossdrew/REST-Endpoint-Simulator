 [![license](https://img.shields.io/github/license/mashape/apistatus.svg?maxAge=2592000)](MIT/Apache 2.0) 
 [![Build Status](https://travis-ci.org/rossdrew/endpointSim.py.svg?branch=master)](https://travis-ci.org/rossdrew/endpointSim.py) 
 [![Code Climate](https://codeclimate.com/github/rossdrew/endpointSim.py/badges/gpa.svg)](https://codeclimate.com/github/rossdrew/endpointSim.py)

#endpointSim

Python script to spin up some simple REST endpoints for simulating services. 

#Usage

To spin up an endpoint, create a Python script in the same directory, make sure there is a [web.py](http://webpy.org/) style URL mapping/class tuple structure to define the mapping and what endpoint class it should point to. Like so:-

```python
urls = ('/Test', 'test')
```

Add (as in [web.py](http://webpy.org/)) a class with a method with the name of the HTTP method type of the expected request, e.g. _GET_ and specify behaviour.

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

Unit tests are run automatically and halt the script if they fail but they can be run by themselves like so

```
python -m doctest endpointSim.py
```

#### Examples

 Included here are two examples:-

  Test.py : An example enpoint that provides a response
  AuthTest.py: An example endpoint with basic auth & JSON returned

