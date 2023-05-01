# Earning Call Text Summarization Using SBERT 

**Author**: *Korkrid Akepanidtaworn, University of Colorado Boulder*

Earning Call Analytics is a solution that helps individual investors, traders, and analysts to extract insights from the transcripts of corporate earnings calls. The pain point is that it's time-consuming and prone to errors when it comes to analyzing earning calls transcript & webcast. This data product will save you tons of hours perusing documents and help you make informed, data-driven decisions about investments in the stock market at the end of the day. 

## Target Audience

Individual investors, traders, analysts, or those who are beginning to start investing. 

## Uniqueness

This data product is, for one, AI-driven using natural language processing (NLP) techniques to automatically extract key information from the transcripts, such as sentiment, tone, topics, themes, questions, answers, and action items. Microsoft provides several APIs such as Sentiment API, Text Analytics API, Anomaly Detector API, Generative AI etc. which are scalable, trusted, and simple to get started with this project. With a combination of data analysis, visualization, and scalable architecture, I hope Earning Call Analytics can unlock trends and patterns over time, understand market sentiments, and gain a competitive edge in the stock market.

## Tech Stack

* Web application basic form, reporting - Flask, Azure Web App Service, Power BI
* Data collection - AlphaVantage, Yahoo Finance API, QuanDL, and Kaggle
* Data analyzer - Cognitive Services APIs by Microsoft, Python's Pandas Library, Scikit-learn, Time-Series API 
* Unit tests - pytest for Python
* Data persistence any data store - MongoDB for Unstructured Data, SQL Database for Structured Data, and Data Lake Storage for Raw Data
* Code Repository - GitHub
* Rest collaboration internal or API endpoint - Flask, Swagger, Docker
* Product environment - Azure, Windows
* Integration tests - pytest for Python
* Using mock objects or any test doubles - mock-requests or unittest.mock for Python
* Continuous integration - GitHub Actions
* Production monitoring instrumenting - Python's built-in logging module
* Event collaboration messaging - Apache Kafka
* Continuous Delivery - GitHub Actions, Heroku Pipeline

## Whiteboard Architecture

There are five major components in the architecture:

1. Data Collection (DC) - There are several APIs available for data collection, for instance, Yahoo Finance API,  Earning Call Transcript API- FinancialModelingPrep,  Free S&P 500 Earnings Call Transcripts (marketbeat.com),  Conference Calls & Earnings Call Transcripts Sources - Knowledge Base (stanford.edu) ,  Earnings Call Transcripts | Seeking Alpha, Kaggle.

2. Database (DB) - I need to store unstructured data. NoSQL is appropriate for managing non-relational data because it doesn't have a pre-defined model. MongoDB and Elasticsearch are some good choices here. I also want to manage unstructured data in data lake at a very first stage, so that I preserve it in raw form. 

3. Data Analyzer (DA) - I want to analyze, discover, and extract useful information from the earning call transcripts and webcast. Rather than training the data on my own, I can leverage numerous pre-trained APIs to get started:

* Cognitive Services APIs by Microsoft (Sentiment API, Text Analytics API, Anomaly Detector API, Generative AI etc.)
* Python's Pandas Library (a powerful data analysis library for Python that is widely used in finance and data science)
* Scikit-learn (a Python library that provides a range of pre-trained models for classification, regression, clustering, and other tasks.)
* Time-Series API (such as Prophet by Facebook)

4. Web - This is the component that will interact with the end users in the form of either web application or Power BI.

5. Message Queue - A message queue can be a useful tool for managing data flow and processing. Apache Kafka is an open source distributed streaming platform that can be used for messaging, storage, and processing of large-scale data streams. It provides high throughput, low latency, and fault-tolerant messaging capabilities, making it an excellent choice for real-time data processing. I can point to either Database (DB) or Data Analyzer (DA). 

![](../img/TFJoS071SOCy9xffijzKHA_56e96935f1694d079ced23932dbb92a1_Earning-Call-Analytics-Whiteboard-Exercise.png)

## Setting up a Web Application

Flask is a good choice for setting up a web app because it is a lightweight and flexible Python framework that allows you to create dynamic and interactive websites with minimal code. Flask also supports various extensions that can enhance its functionality, such as SQLAlchemy for database integration, Flask-WTF for form validation, and Flask-RESTful for building RESTful APIs. Flask is easy to learn and use, and it can scale well for complex applications.

It integrates well with other Python libraries and tools.

Here are the steps to get started with Flask on Windows:

1. Install Python: If you don't have Python installed on your machine, you can download and install the latest version of Python from the official Python website at https://www.python.org/downloads/. Follow the installation instructions provided on the website.
2. Install Flask: Once Python is installed, you can use pip (Python package installer) to install Flask. Open a command prompt or terminal window and run the following command:

```
pip install flask
```

This will install the Flask package and its dependencies.

3. Create a Flask App: Create a new Python file with a .py extension and add the following code:

```
from flask import Flask, jsonify, render_template, request
from summarizer import Summarizer
from summarizer.sbert import SBertSummarizer
from prometheus_client import Counter, generate_latest, REGISTRY
import time

# create an instance of the SBERT summarizer
model = SBertSummarizer('paraphrase-MiniLM-L6-v2')

app = Flask(__name__)

@app.route("/")
def msg():
    return render_template('index.html')

# define the health check endpoint
@app.route('/health')
def health_check():
    response = jsonify({'status': 'ok'})
    response.status_code = 200
    return response

# define the main endpoint for summarization
@app.route("/summarize",methods=['POST','GET'])
def getSummary():
    body=request.form['data']
    result = model(body, num_sentences=5)
    return render_template('summary.html',result=result)

# Define a counter metric for the number of requests
REQUESTS = Counter('requests_total', 'HTTP requests total', ['method', 'endpoint'])

# define the metrics endpoint
@app.route("/metrics")
def metrics():
    # Increment the counter metric
    REQUESTS.labels(method=request.method, endpoint=request.path).inc()

    # Generate and return the latest metrics as a string
    return generate_latest(REGISTRY), 200, {'Content-Type': 'text/plain'}

# start the Flask app
if __name__ =="__main__":
    app.run(debug=True,port=8000)
```

Run the App: Save the file with a name like `app.py` and run the following command in the command prompt or terminal window:

```
python app.py
```

This will start the Flask development server and make the app accessible at `http://127.0.0.1:5000/` in your web browser.

```
 * Serving Flask app 'app' (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 316-584-348
```

To stop the server, press Ctrl+C in the command prompt or terminal window.

## Dockerize a Flask Application

Docker is a tool that makes it easier to create, deploy, and run applications using containers.

A docker container is a collection of dependencies and code organized as software that enables applications to run quickly and efficiently in a range of computing environments.

A docker image, on the other hand, is a blueprint that specifies how to run an application. In order for Docker to build images automatically, a set of instructions must be stored in a special file known as a Dockerfile.

The instructions in this file are executed by the user on the command line interface in order to create an image. 

![](../img/docker-illustration-2.png)


With Docker, I ensure:

- Portability: Docker containers can be easily moved from one environment to another without any compatibility issues. This means you can develop your application on your local machine, test it on a staging server, and then deploy it on a production server without having to worry about differences in the underlying infrastructure.
- Isolation: Docker containers provide a level of isolation between the application and the host operating system, which helps to prevent conflicts with other applications running on the same machine. This makes it easier to maintain the stability and security of the system.
- Consistency: Docker containers ensure that the application and its dependencies are consistent across all environments. This means that the same container image can be used for development, testing, and production, which reduces the chances of configuration errors and other issues.
- Scalability: Docker containers can be easily scaled up or down to meet the changing demands of an application. This makes it possible to handle spikes in traffic and to optimize resource usage.
- Efficiency: Docker containers are lightweight and require minimal resources to run. This means that you can run more containers on the same machine compared to running multiple virtual machines, which reduces the cost of infrastructure and improves overall efficiency.

Here's my Dockerfile I come up with:
```
# Use the official Python base image
FROM python:3.9-slim-buster

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file to the working directory
COPY requirements.txt .

# Install the project dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code to the working directory
COPY . .

# Expose the port on which the Flask app will run
EXPOSE 80

# Set the environment variable for Flask
ENV FLASK_APP=app.py

# Start the Flask application
CMD ["flask", "run", "--host=0.0.0.0", "--port=80"]
```

I trigger GitHub Actions to push my docker image to DockerHub, which is a cloud-based registry service provided by Docker that allows users to store and share Docker container images. 

![](../img/docker-illustration.png)

Here's how my GitHub workflow is. I also enable CI/CD during this process.

```
name: Docker

# This workflow uses actions that are not certified by GitHub.
# They are provided by a third-party and are governed by
# separate terms of service, privacy policy, and support
# documentation.

on:
  push:
    branches:
      - main
    pull_requests:
      branches:
        - main

env:
  # Use docker.io for Docker Hub if empty
  REGISTRY: docker.io
  # github.repository as <account>/<repo>
  IMAGE_NAME: kylethedockerate/msds-dtsa-5714-earningscall

jobs:
  build:

    runs-on: ubuntu-latest
    permissions:
      contents: read
      packages: write
      # This is used to complete the identity challenge
      # with sigstore/fulcio when running outside of PRs.
      id-token: write

    steps:
      - name: Checkout repository
        uses: actions/checkout@v3

      # Workaround: https://github.com/docker/build-push-action/issues/461
      - name: Setup Docker buildx
        uses: docker/setup-buildx-action@79abd3f86f79a9d68a23c75a09a9a85889262adf

      # Login against a Docker registry except on PR
      # https://github.com/docker/login-action
      - name: Log into registry ${{ env.REGISTRY }}
        if: github.event_name != 'pull_request'
        uses: docker/login-action@28218f9b04b4f3f62068d7b6ce6ca5b26e35336c
        with:
          registry: ${{ env.REGISTRY }}
          username: kylethedockerate 
          password: ${{ secrets.DOCKERHUB_KEY }}

      # Extract metadata (tags, labels) for Docker
      # https://github.com/docker/metadata-action
      - name: Extract Docker metadata
        id: meta
        uses: docker/metadata-action@98669ae865ea3cffbcbaa878cf57c20bbf1c6c38
        with:
          images: ${{ env.REGISTRY }}/${{ env.IMAGE_NAME }}

      # Build and push Docker image with Buildx (don't push on PR)
      # https://github.com/docker/build-push-action
      - name: Build and push Docker image
        id: build-and-push
        uses: docker/build-push-action@ac9327eae2b366085ac7f6a2d02df8aa8ead720a
        with:
          context: .
          push: ${{ github.event_name != 'pull_request' }}
          tags: ${{ steps.meta.outputs.tags }}
          labels: ${{ steps.meta.outputs.labels }}
          cache-from: type=gha
          cache-to: type=gha,mode=max

```

## Hosting on Azure Web App

Unfortunately, Heroku is no longer free. My docker image is very large (2+ GBs). I decide to host my app on Azure. 

* [Deploy and run a containerized web app with Azure App Service - Training | Microsoft Learn](https://learn.microsoft.com/en-us/training/modules/deploy-run-container-app-service/)
* [Deploying a Docker based web application to Azure App Service | Azure DevOps Hands-on-Labs](https://www.azuredevopslabs.com/labs/vstsextend/docker/)

You can try my web app from the following link: [Text Summarizer App using SBert](https://earningcallsm.azurewebsites.net/)

![](../img/Text-Summarizer-App-using-SBert-Input.png)

![](../img/Text-Summarizer-App-using-SBert-Output.png)

## Data Collector

Here are some of the available APIs for fetching earning call transcripts:

* Finnhub. Finnhub is a financial data provider that offers a variety of APIs, including an earnings call transcripts API. This API allows you to fetch transcripts for earnings calls from over 10,000 companies.
* Earnings Whispers. Earnings Whispers is a website that provides earnings estimates and transcripts for earnings calls. The website offers an API that allows you to fetch transcripts for earnings calls from over 3,000 companies.
* Refinitiv Eikon. Refinitiv Eikon is a financial data platform that offers a variety of APIs, including an earnings call transcripts API. This API allows you to fetch transcripts for earnings calls from over 10,000 companies.
* IEX Cloud. IEX Cloud is a financial data platform that offers a variety of APIs, including an earnings call transcripts API. This API allows you to fetch transcripts for earnings calls from over 4,000 companies.
* CNBC Pro. CNBC Pro is a subscription service that provides access to a variety of financial data, including earnings call transcripts. The service offers an API that allows you to fetch transcripts for earnings calls from over 2,000 companies.
* SeekingAlpha. SeekingAlpha is a crowd-sourced content service that publishes news and analysis on financial markets. It was founded in 2004 by David Jackson, a former Morgan Stanley technology analyst. The company is headquartered in New York City.

A good starting point here is **SeekingAlpha**. Seeking Alpha API from RapidAPI is an API that queries stock news, market-moving, price quotes, charts, indices, analysis, and many more from investors and experts on seeking alpha stock research platform. In addition, it has a comprehensive list of endpoints for different categories of data. Seeking Alpha API works using simple API logic in which It sends a request to a specific endpoint and obtains the necessary output as the response. When sending a request, it includes x-RapidAPI-key and host as authentication parameters so that the server can identify it as a valid request. In addition, the API requests body contains the optional parameters to process the request. Once the API server has received the request, it will process the request using the back-end application. Finally, the server will send back the information requested by the client in JSON format.

![](../img/seekingalpha-logo.png)

The Seeking Alpha API provides a lot of endpoints, including a default endpoint. These endpoints belong to 9 categories.

1. Market
2. Symbol
3. Analysis
4. Article
5. News
6. Press Release
7. Transcript
8. Author 
9. Comment

You can get a list of transcripts of a specific company and get more details about a particular transcript using transcript endpoints. 

Then, I will insert these data to MongoDB, which is a good choice for many applications because it offers several advantages over traditional relational databases. Some of these advantages are:

- MongoDB is schemaless, which means it can store data in flexible and dynamic documents that can have different fields and structures. This allows for faster development and easier data modeling, especially for complex or unstructured data.
- MongoDB is scalable, which means it can handle large amounts of data and high traffic without compromising performance or reliability. MongoDB supports horizontal scaling through sharding, which distributes data across multiple servers, and replication, which creates copies of data for backup and fault tolerance.
- MongoDB is expressive, which means it supports a rich and powerful query language that can perform complex operations on the data. MongoDB also supports various indexing options, aggregation frameworks, and text search features that enable fast and flexible data analysis and manipulation.

Here is the complete script for retrieving data from The Seeking Alpha API and uploading it to MongoDB. 

![](../img/maxresdefault.jpg)

```
import requests
import io
import json

# Make a GET request to the Seeking Alpha API endpoint
url = "https://seeking-alpha.p.rapidapi.com/transcripts/v2/list"
querystring = {"id":"aapl","size":"20","number":"1"} # Set query parameters
headers = {
	"X-RapidAPI-Key": "a2d702a09bmshb89eec70e7c02edp173778jsnc274b366bb28",
	"X-RapidAPI-Host": "seeking-alpha.p.rapidapi.com"
} # Set headers
response = requests.get(url, headers=headers, params=querystring) # Send GET request
print(json.dumps(response.json(), indent = 1)) # Pretty-print the JSON response

# Extract the JSON data from the response
data = response.json()

# Connect to a MongoDB Atlas cluster
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://koak2789:oCge9tsmX9AozHKH@clustertesting-msds.bvcccni.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

# Get the database and collection objects
db = client.sample_earningcall # Get the database named "sample_earningcall"
collection = db.companylist # Get the collection named "companylist"

# Insert the JSON data into the collection
collection.insert_many(data["data"])

# Find and print the first document in the collection
print(collection.find_one())
```

![](../img/Data-Cloud-MongoDB-Cloud.png)

## Data Analyzer

Data analysis and machine learning are important because they help us discover patterns, insights and predictions from large and complex datasets.

SBertSummarizer is a tool that uses sentence embeddings to extract the most relevant sentences from a text and form a summary. It is based on the SBERT model, which is a variant of BERT that computes sentence-level representations. SBertSummarizer can handle long and complex texts and produce coherent and concise summaries.

Here's the full code for my data analysis part:

```
# Download the summarizer
from summarizer import Summarizer
from summarizer.sbert import SBertSummarizer

# Load the summarizer
model = SBertSummarizer('paraphrase-MiniLM-L6-v2')

# Set the number of sentences to summarize
num_sentences = 5

# Set the body text
body = '''Spread over more than 253.38 acre, of which the waterbody comprises 180.60 acre, Madiwala lake in BTM layout was rejuvenated in 2018 with the addition of a biodiversity park. But a year later, the state government handed over the custody of the lake to the civic agency, Bruhat Bengaluru Mahanagara Palike (BBMP), claiming the decision would help in better upkeep of the waterbody. Environmental activists, however, said that the results have been quite the opposite since the change of guard. The lake was earlier with the Karnataka Forest Department.

Notably, the office of the Range Forest Officer is inside the lake area. Pointing at the poor maintenance of the lake, the officials from the forest department said that lavatories meant for the visitors are not functional and the fuses from the meter board at the amphitheatre area of the lake were taken away since the January electricity bill of Rs 16,000 was not paid.

A forest department official said, “The two lavatories that were constructed a few years ago are yet to be open to the public. The reason is that water connection has still not been provided to the lavatories. The trees are not maintained properly and only two staffers have been deployed by the BBMP for the upkeep of such a huge lake. We wanted to put up two information boards on birds frequenting the park of the lake but the BBMP denied us permission.”

“We want the lake to be given back to us so that the ecology of the lake is maintained well. It has been learnt from reliable sources that the custody of the lake will be given back to us later this year. The nursery and the butterfly park are in a shambles today. We used to generate Rs 25,000 on weekends and Rs 8,000 on weekdays from sale of tickets. But the BBMP has stopped boating services and it has withdrawn the entry fee,” he added.

In the recent tree census carried out by the civic agency, over 2,000 trees were counted at the lake. Officials said that more trees are yet to be counted.Lake activist Naveen S, who has planted hundreds of trees near the lake with the help of the forest department, accused the BBMP of neglecting the waterbody.

“During heavy monsoon, the untreated sewage enters the lake from the storm water drains (SWD). The BBMP has not addressed this issue. Most important, buildings have been built near the SWD and the lake, encroaching the buffer zone. Near the periphery of the lake, several bamboo trees were removed and when we requested the authorities to plant native species at vacant patches, the permission was denied,” he said.

Referring to the severe waterlogging that the BTM Layout faced last year during the monsoon, Naveen said: “The interconnectivity between Hulimavu lake and Madiwala lake has been adversely affected owing to the encroachment. We have found it difficult to even highlight the issues to the BBMP as their officers are unresponsive.”

The forest department had allotted a separate parking lot near the lake for the visitors. But after the transfer of the custody of the lake, the visitors now park their vehicles on the footpath and the road.

According to the Karnataka State Pollution Control Board (KSPCB), the water quality index of the lake is unsatisfactory and qualifies under Class D (propagation of wildlife and fisheries).

An engineer from the Bangalore Water Supply and Sewerage Board (BWSSB) informed that a sewage treatment plant (STP) with a 10 mld capacity is being constructed. “We will finish the work within 15 days and the STP will be operational. The work was delayed owing to reasons known only to the higher authorities,” he said.'''

# Summarize the text
result = model(body, num_sentences=num_sentences)

# Print the summary
print(result)
```


## Unit Testing 

Unit testing is a software development practice that involves writing and running small pieces of code to verify the functionality and quality of a larger piece of code. Unit testing in Python is important for several reasons:

- It helps to find and fix bugs early in the development process, before they become more costly and difficult to resolve.
- It improves the readability and maintainability of the code, by making it more modular and structured.
- It facilitates code reuse and refactoring, by ensuring that the code behaves as expected when changes are made.
- It enhances the confidence and reliability of the code, by providing evidence that it meets the specifications and requirements.
- It supports collaboration and communication among developers, by documenting the code's behavior and design.

There are many tools and frameworks available for unit testing in Python, such as unittest, pytest, nose, doctest, etc. Each one has its own features and advantages, but they all share some common principles and best practices. Some of them are:

- Write test cases that are independent, isolated, and repeatable. Each test case should test one specific aspect of the code, and should not depend on the order or outcome of other test cases.
- Use descriptive and meaningful names for test cases, test methods, and test modules. This makes it easier to understand what each test is doing and why it is important.
- Follow a consistent and clear structure for organizing test cases, test methods, and test modules. This makes it easier to navigate and maintain the test code.
- Use assertions to check the expected results against the actual results. Assertions are statements that verify if a condition is true or false, and raise an exception if it is false.
- Use mock objects to simulate external dependencies or side effects. Mock objects are fake objects that mimic the behavior of real objects, but without actually interacting with them. They can be used to isolate the code under test from external factors that are not relevant or predictable.
- Run tests frequently and automatically. Tests should be run every time a change is made to the code, or at least before committing or deploying the code. Tests can be run manually or using tools like continuous integration (CI) or continuous delivery (CD) systems.

Conceptually speaking, I have this Python app - `bmi.py` - as an example:

```
class Bmi:
    def __init__(self, w_kg, h_cm):
        # Initialize object properties
        self.w_kg = w_kg
        self.h_cm = h_cm
        # Don't calculate BMI in __init__, since it can be changed outside class
        # self.bmi = self.w_kg / (self.h_cm / 100) ** 2

    @property  # Readonly
    def bmi(self):
        # Calculate BMI based on object properties
        return self.w_kg / (self.h_cm / 100) ** 2

    def bmi2(self):
        # Calculate BMI based on object properties (same as @property bmi)
        return self.w_kg / (self.h_cm / 100) ** 2

    def category(self):
        # Determine BMI category based on BMI value
        cat = ""
        if self.bmi < 18.5:
            cat = "ต่ำกว่าเกณฑ์"
        elif 18.5 <= self.bmi <= 25:
            cat = "ตามเกณฑ์"
        elif 25 < self.bmi <= 30:
            cat = "เกินเกณฑ์"
        elif self.bmi > 30:
            cat = "อ้วน"
        return cat

    def __str__(self):
        # String representation of object
        # Format BMI value with 2 decimal places and include category
        return "BMI = {:.2f} ({})".format(self.bmi2(), self.category())
```

I put my unit test in `tests` folder called `test_bmi.py`

```
import pytest
from bmi import Bmi

def test_one():
    p1=Bmi(75, 170)
    assert p1.bmi==pytest.approx(25.95, .01)
    assert p1.category() == 'เกินเกณฑ์'

def test_two():
    p1=Bmi(48, 160)
    assert p1.bmi==pytest.approx(18.75, .01)
    assert p1.category() == 'ตามเกณฑ์'

def test_three():
    p1=Bmi(40, 160)
    assert p1.bmi==pytest.approx(15.62, .01)
    assert p1.category() == 'ต่ำกว่าเกณฑ์'
```

* [มาทำ Unit Testing บน Python กันเถอะ !](https://www.borntodev.com/2020/04/07/%E0%B8%A1%E0%B8%B2%E0%B8%97%E0%B8%B3-unit-testing-%E0%B8%9A%E0%B8%99-python-%E0%B8%81%E0%B8%B1%E0%B8%99/)
* [ทดสอบโค้ดโปรแกรมภาษาไพทอนด้วย pytest ~ Python 3](https://python3.wannaphong.com/2015/08/pytest.html)
* [Testing a Flask framework with Pytest | CircleCI](https://circleci.com/blog/testing-flask-framework-with-pytest/)
* [po5i/flask-mini-tests](https://github.com/po5i/flask-mini-tests/tree/master)

## Monitor and Metrics Endpoints

One of the best practices for developing and maintaining a reliable and resilient application is to create a health endpoint that exposes the current status of the application, or a component of the application. A health endpoint is a special URL that returns a simple response indicating whether the application is healthy, unhealthy, or degraded. The health endpoint can be used by external monitoring tools, such as Azure Application Insights, to check the availability and performance of the application. The health endpoint can also be used by internal components, such as load balancers, to route traffic to healthy instances and avoid sending requests to unhealthy or overloaded instances.

Creating a health endpoint for your application has several benefits. First, it allows you to quickly identify and diagnose any issues that may affect the functionality or performance of your application. For example, you can use the health endpoint to check if your application can connect to its dependencies, such as databases, caches, or external services. You can also use the health endpoint to report any errors or exceptions that occur within your application logic. Second, it enables you to improve the user experience and satisfaction by minimizing downtime and ensuring high availability. For example, you can use the health endpoint to implement graceful degradation strategies, such as fallbacks or retries, when your application encounters partial failures or transient errors. You can also use the health endpoint to notify users about planned maintenance or scheduled updates that may temporarily affect the service level of your application. Third, it helps you to optimize the resource utilization and scalability of your application by adjusting the load and capacity according to the demand and health status. For example, you can use the health endpoint to scale up or down your application instances based on the CPU usage, memory consumption, or response time. You can also use the health endpoint to balance the load among your application instances by distributing requests evenly or preferentially.

In fact, my `app.py` has defined /health endpoint and /metrics endpoint.

```
from flask import Flask, jsonify, render_template, request
from summarizer import Summarizer
from summarizer.sbert import SBertSummarizer
from prometheus_client import Counter, generate_latest, REGISTRY
import time

# create an instance of the SBERT summarizer
model = SBertSummarizer('paraphrase-MiniLM-L6-v2')

app = Flask(__name__)

@app.route("/")
def msg():
    return render_template('index.html')

# define the health check endpoint
@app.route('/health')
def health_check():
    response = jsonify({'status': 'ok'})
    response.status_code = 200
    return response

# define the main endpoint for summarization
@app.route("/summarize",methods=['POST','GET'])
def getSummary():
    body=request.form['data']
    result = model(body, num_sentences=5)
    return render_template('summary.html',result=result)

# Define a counter metric for the number of requests
REQUESTS = Counter('requests_total', 'HTTP requests total', ['method', 'endpoint'])

# define the metrics endpoint
@app.route("/metrics")
def metrics():
    # Increment the counter metric
    REQUESTS.labels(method=request.method, endpoint=request.path).inc()

    # Generate and return the latest metrics as a string
    return generate_latest(REGISTRY), 200, {'Content-Type': 'text/plain'}

# start the Flask app
if __name__ =="__main__":
    app.run(debug=True,port=8000)
```

How can you test that the health check is working? 

1. /health endpoint that responds to 200 ok
2. /metrics endpoint that uses a metrics library (# request per second) json data and 200 ok

![](../img/127-0-0-1-5000-health.png)

![](../img/127-0-0-1-5000-metrics.png)

Thank you for following through my design documentation. I trust that you will find it valuable and informative. If you have any feedback or suggestions, please do not hesitate to share them with me. 