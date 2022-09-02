### Conceptual Exercise

Answer the following questions below:

- What are important differences between Python and JavaScript?
Python is able to connect with frameworks that create servers, and create sessions in a way that JavaScript can't:  
* Store more data then JS localStorage with Flask Sessions
* There are more ways in Python to store data like sets, tuples, dictionaries.
* You can code in virtual environments. 
* You can access, read, and write into files with Python. 
* By default, Python uses ASCII encoding while JS is UTF-7 encoding 
* JavaScript is browser front-end native while Python is not, it's a back-end langauge. 

- Given a dictionary like ``{"a": 1, "b": 2}``: , list two ways you
  can try to get a missing key (like "c") *without* your programming
  crashing.  

get(key,def_val) method is useful when we have to check for the key. If the key is present, the value associated with the key is printed, else the def_value passed in arguments is returned. You can push another key value pair onto that dictionary as well. 

- What is a unit test?  
A unit test is for testing a singular function that is merely part of a larger project to see if it really returns what we want it to. 
They don't test the framework itself. You primarily use a tool called assert, that isn't really a function. You can use various keywords to test for whichever you result you expect your function to return, for example self.assertEqual. In order to use such keywords, you must import the with _from unittest import TestCase_. And you can run the test through _ipython_ typing _python -m unittest NAME-OF-FILE.py_  

- What is an integration test?  
  
In integration tests the parts work together. Program units are combined and tested as groups in multiple ways

- What is the role of web application framework, like Flask?  

Flask brings together mulitply programming languages together like CSS, HTML, and JavaScript. Python brings all of those together and creates "routes" that can be separate html pages that are access with events. In other words, you can manipulate urls and perform http server GET and POST requests. It can also act as template engine using jinja, which can easily connect different html files together. 

- You can pass information to Flask either as a parameter in a route URL
  (like '/foods/pretzel') or using a URL query param (like
  'foods?type=pretzel'). How might you choose which one is a better fit
  for an application? 

  Route URL is what you'd use to create POST request for a question form, and a URL query param would most likely handle GET requests like searching for something specific like on a search form on Reddit. 

- How do you collect data from a URL placeholder parameter using Flask?  

Request.form

- How do you collect data from the query string using Flask?  

Request.args

- How do you collect data from the body of the request using Flask?  

Use request.form to get data when submitting a form with the POST method. Use request.args to get data passed in the query string of the URL, like when submitting a form with the GET method.

- What is a cookie and what kinds of things are they commonly used for?

The client sends cookies to the server with each request. Cookies are name/string-value pair stored by the client (browser).   
Cookies are a way to store small bits of info on client (browser). What pages you viewed, client ids, number of visits are what cookies store. When we make a http request for reviews or latest, whatever it is, those cookies are going to be automatically 
sent to the server. localStorage saves to the browser, always on the client's side. Cookies are sent via request header. 

- What is the session object in Flask?  

In Flask sessions, information isn't limited like the way cookies are. Cookies are just strings, but in routes you can treat sessions as dictionary like objects. They are serialize and signed so a user can't tell what they mean and can't change them, yet they are stored as cookies. 

- What does Flask's `jsonify()` do?  

`jsonify()` is like a function that turns key-value pairs into a JavaScript object in the most convenient way without handwriting it all. Then the json viewer in Chrome can undoubtedly recognize you return as json.

