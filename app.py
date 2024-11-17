from flask import Flask
from prometheus_client import Counter, generate_latest, REGISTRY, Gauge, Histogram
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)
metrics = PrometheusMetrics(app)

# Example of a simple counter
REQUEST_COUNT = Counter('request_count', 'Total Request Count')

@app.route('/')
def hello_world():
    REQUEST_COUNT.inc()  # Increment counter
    return 'Hello, krupaaaaaaaaaaaaa'

@app.route('/metrics')
def metrics():
    return generate_latest(REGISTRY), 200, {'Content-Type': 'text/plain; charset=utf-8'}

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5200)
