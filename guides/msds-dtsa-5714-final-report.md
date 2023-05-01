# Earning Call Text Summarization Using SBERT 

**Author**: Korkrid Akepanidtaworn, University of Colorado Boulder

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
