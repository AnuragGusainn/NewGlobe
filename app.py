from flask import Flask, render_template_string
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST
from prometheus_client import start_http_server

# Flask application
app = Flask(__name__)

# Prometheus metrics
REQUEST_COUNTER = Counter('flask_http_request_total', 'Total number of HTTP requests', ['method', 'endpoint'])

# Decorator to track requests
@app.before_request
def before_request():
    REQUEST_COUNTER.labels(method=request.method, endpoint=request.path).inc()

# Sample route with CSS animation
@app.route('/lesson-complete', methods=['GET'])
def lesson_complete():
    # Create HTML content with CSS animation
    html_content = '''
    <html>
        <head>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    text-align: center;
                    margin-top: 50px;
                }
                .status {
                    font-size: 2.5em;
                    color: #00FF00; /* Green color for a glowing effect */
                    text-shadow: 0 0 10px rgba(0, 255, 0, 0.8), 0 0 20px rgba(0, 255, 0, 0.6), 0 0 30px rgba(0, 255, 0, 0.4);
                    animation: fadeIn 3s ease-in-out, pulse 1.5s infinite;
                }
                @keyframes fadeIn {
                    from { opacity: 0; }
                    to { opacity: 1; }
                }
                @keyframes pulse {
                    0% { transform: scale(1); }
                    50% { transform: scale(1.1); }
                    100% { transform: scale(1); }
                }
            </style>
        </head>
        <body>
            <div class="status">Lesson Completed: 98%</div>
        </body>
    </html>
    '''
    return render_template_string(html_content)

# Prometheus metrics endpoint
@app.route('/metrics')
def metrics():
    return generate_latest(), 200, {'Content-Type': CONTENT_TYPE_LATEST}

if __name__ == '__main__':
    # Start Prometheus metrics server on port 8001
    start_http_server(8001)
    
    # Run Flask app
    app.run(host='0.0.0.0', port=8000)

