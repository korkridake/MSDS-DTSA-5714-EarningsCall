# Earning Call Text Summarization Using SBERT 

Earning Call Analytics is a solution that helps individual investors, traders, and analysts to extract insights from the transcripts of corporate earnings calls. The pain point is that it's time-consuming and prone to errors when it comes to analyzing earning calls transcript & webcast. This data product will save you tons of hours perusing documents and help you make informed, data-driven decisions about investments in the stock market at the end of the day. 

## Target Audience

Individual investors, traders, analysts, or those who are beginning to start investing. 

## Uniqueness

This data product is, for one, AI-driven using natural language processing (NLP) techniques to automatically extract key information from the transcripts, such as sentiment, tone, topics, themes, questions, answers, and action items. Microsoft provides several APIs such as Sentiment API, Text Analytics API, Anomaly Detector API, Generative AI etc. which are scalable, trusted, and simple to get started with this project. With a combination of data analysis, visualization, and scalable architecture, I hope Earning Call Analytics can unlock trends and patterns over time, understand market sentiments, and gain a competitive edge in the stock market.

## Tech Stack

* Web application basic form, reporting - Flask, Heroku, Power BI
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

## Tree Directory

```
MSDS-DTSA-5714-EarningsCall/
├── .git/
│   ├── branches/
│   ├── config
│   ├── description
│   ├── FETCH_HEAD
│   ├── HEAD
│   ├── hooks/
│   ├── index
│   ├── info/
│   ├── lfs/
│   ├── logs/
│   ├── objects/
│   ├── packed-refs
│   └── refs/
├── .github/
│   └── workflows/
├── .venv/
│   ├── .gitignore
│   ├── bin/
│   ├── etc/
│   ├── include/
│   ├── lib/
│   ├── lib64/
│   ├── pyvenv.cfg
│   └── share/
├── app.py
├── data/
│   └── META-Q1-2023-Earnings-Call-Transcript.pdf
├── data-analyser-bert-summarization.ipynb
├── data-analyser-bert-summarization.py
├── data-collection-seekingalpha-pymongo.ipynb
├── data-collection-seekingalpha-pymongo.py
├── Dockerfile
├── docs/
│   ├── week-1.md
│   ├── week-2.md
│   ├── week-3.md
│   ├── week-4.md
│   └── week-5.md
├── img/
│   ├── 127-0-0-1-5000-health.png
│   ├── 127-0-0-1-5000-metrics.png
│   ├── Data-Cloud-MongoDB-Cloud.png
│   ├── docker-illustration-2.png
│   ├── docker-illustration.png
│   ├── maxresdefault.jpg
│   ├── seekingalpha-logo.png
│   ├── Text-Summarizer-App-using-SBert-Input.png
│   ├── Text-Summarizer-App-using-SBert-Output.png
│   └── TFJoS071SOCy9xffijzKHA_56e96935f1694d079ced23932dbb92a1_Earning-Call-Analytics-Whiteboard-Exercise.png
├── models/
├── notebooks/
│   └── 00-tree-directory.ipynb
├── Procfile
├── README.md
├── requirements.txt
├── templates/
│   ├── index.html
│   └── summary.html
└── tests/
    ├── __init__.py
    ├── beta_test.py
    ├── test_adv.py
    ├── test_alpha.py
    ├── test_bmi.py
    ├── test_fixture1.py
    ├── test_fixture2.py
    └── test_fixture3.py
```
