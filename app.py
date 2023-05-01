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