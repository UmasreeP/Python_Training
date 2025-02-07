"""
Python for web development

We have many web frameworks like
flask
django
fastapi
many more
"""

"""
Here we are using flask framework
"""

"""
using flask framework
1. using flask framework, we can develop websites
2. using flask framework, we can develop REST-API
3. using flask framework, we can develop Micro Services
"""

"""
We are targetting,
How to use flask framework for developing REST-API
"""

"""
To understand API/REST-API,
Example: Suppose, we are planning to provide access to our my_database.db
with others/public.

One options is, we can create separate credentials with some permissions
and we can share with others.

This OPTION is limited for few users/few-projects
"""

"""
Providing access to others/public became critical, so
we got 2 solutions

1. SOAP: Simple Object Access Protocol
2. REST: REpresentational State Transfer

both are called architetures/designs/styles
both tells how we can provide access to others/public

both tells to introduce some DOOR/GATE/INTERFACE between 
our-application/db/resources with others/public
it is like
our-application/db/resources  <--INTERFACE--> others/public

both tells how to write such interface

this INTERFACE is also called APPLICATION PROGRAMMING INTERFACE (API)
"""

"""
REST came after SOAP
- REST easy to implement and manage
- REST is popular
"""

"""
I our case, no need to implement REST architecture from scratch
Because
flask-framework is already implemented REST architecture
SO,
we just need to know, how to create REST-API using flask framework
"""

"""
We are planning to provide full-access/complete-access to our database.

full-access/complete-access means?
- Creating new record
- Reading existing records
- Updating existing records
- Deleting existing records
"""

"""
HTTP web standard: 
- We have something like HTTP methods
    GET, POST, PUT, PATCH, DELETE

full-access/complete-access means?
POST        - Creating new record
GET         - Reading existing records
PUT/PATCH   - Updating existing records
DELETE      - Deleting existing records
"""

"""
For any web application/API, 
we need web server to run our web application/API.

flask has builtin web server
Since this  builtin web server is not strong, we CAN'T use it for
production deployment. We can make use for development purposes
"""

"""
In this release,
we are developing REST-API to provide access to 
reading all records(GET) from our database 'my_database.db'

PLANNED END POINT: http://127.0.0.1:5000/getdbdata
"""

# ----------
# Create App
############
import flask
# my_rest_api_app = flask.Flask("Some App Name")
# OR
my_rest_api_app = flask.Flask(__name__) # It will take file name
#######################

# ----------
# END POINT-1: GET: Creating API to access all the records
# PLANNED END POINT: http://127.0.0.1:5000/getdbdata
############
@my_rest_api_app.route("/getdbdata", methods=["GET"]) # URL MAPPING
def get_all_records_function():
    import sqlite3
    my_db_connection = sqlite3.connect("my_database.db")
    my_db_cursor = my_db_connection.cursor()
    my_query = "SELECT * FROM MY_TABLE"
    my_db_cursor.execute(my_query)
    my_db_result = my_db_cursor.fetchall()
    return flask.jsonify(my_db_result)
#######################

# ----------
# Run builtin Server
############
my_rest_api_app.run() # default host='127.0.0.1', port=5000
# my_rest_api_app.run(host='', port='')
#######################