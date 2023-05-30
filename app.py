from flask import Flask, jsonify
from prometheus_flask_exporter import PrometheusMetrics
from datetime import datetime
import random

app = Flask(__name__)
metrics = PrometheusMetrics(app)

@app.route('/')
def home():
    return jsonify({
        'current_time': datetime.now().isoformat(),
        'random_integer': random.randint(0, 100)
    })

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
