# Data Persistence

For your project, you will be handling data. Conequently, you may need your data to be stored somewhere so that you can use said data later on. A database is one of the best ways to store data for a web application. When choosing a database a few key factors should be considered:

SQL/NoSQL

Ease of implementation

Security

Scalability

Cost/Sustainability 

Perhaps one of the biggest factors influencing your choice would be wether you want a SQL database or a NoSQL database. Some key comparison include:

Since NoSQL have a dynamic schema, they are better for unstructured data. SQL by definition has a well defined schema and thus is better for table based data.

NoSQL is horizontally scalable whereas SQL is vertically scalable. More info can be found 
here

For your project, you have discression in choosing whichever database software you think is best. However for the novice, we show how to use SQLAlchemy with Flask to store user information. SQLAlchemy, as the name suggests, is a SQL database and is great for storing user data (name, email etc) since they are relational entities.

First we install the package using pip.

```
pip install flask-sqlalchemy
```
Once the package is intalled, we need to create a Flask application object, set the database URI and then initialize a model. Below we create a database model called Users which is what we can use to store information about each user. Line 10 is the primary key for the database and it is a numberic idetifier. Line 11 is the name of the user. We can create additional attributes if we wanted.

```
#!/usr/bin/env python3
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Users.sqlite3'

db = SQLAlchemy(app)
class Users(db.Model):
    id = db.Column("User_ID", db.integer, primary_key=True)
    name = db.Column(db.String(20))
```

# Data Collection

Your project may require you to fetch data from an outside source. REST APIs provide a great means for retreving data. To demonstrate data collection, we shall create a simple Python script that fetches data from an API and stores it in a database. For our example, we query the current temperature from weather using their API. Once we get the data, we store it in a database.

```
#!/usr/bin/env python3
import requests
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Weather.sqlite3'

'''
Define the database model
that is used to store 
the temperature.
'''

db = SQLAlchemy(app)
class Weather(db.Model):
    datetime = db.Column(db.DateTime, primary_key=True, default=datetime.utcnow())
    temperature = db.Column(db.Integer, nullable=False)
    
'''
Helper function to get temperature
using API
'''

def get_temperature():
    response = requests.get("https://weatherdbi.herokuapp.com/data/weather/boulder")
    return response.json()["currentConditions"]["temp"]["c"]


'''
In main we first get the current temperature and then 
create a new object that we can add to the database. 
'''
if __name__ == "__main__":
    current_temperature = get_temperature()
    new_entry = Weather(temperature=current_temperature)
    db.session.add(new_entry)
    db.session.commit()
```

Everytime we run the above script it queries the API endpoint for the current temperature and then stores that entry in the database. For your project, you should have a seperate process running your data collection process. If you are using a UNIX system, cronjobs are a great way to have the process scheduled automatically. PaaS technologies such as Heroku has a scheduler which offer similar functionality to that of a cronjob. Depending on the nature of the data you are collecting, you might have the script scheduled to run hourly, daily or weekly/bi-weekly.

# Data Analysis 

APIs are great for fetching raw data, however, sometimes they may not offer an endpoint that provides analyzed data. Furthermore, since you now have a database that stores information, it would be great to do some analysis on that data. To demonstrate data analysis, we showcase a snippet of a Flask API endpoint which returns the average temperature from a range of dates. 

The example also illustrates the use of a REST API within our application.

```
@app.route(average/<start_date>/<end_date>)
def average_temperature():
    sum = 0
    query = db.query(Weather).filter(Weather.date.between(start_date, end_date))
    for item in query:
        sum = sum + item["temp"]
        return sum/query.count()
```