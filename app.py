from flask import Flask, request, render_template_string, jsonify

app = Flask(__name__)

# Webhook endpoint for GitHub
@app.route('/github-webhook/', methods=['POST'])
def github_webhook():
    if request.method == 'POST':
        data = request.json
        # Process the GitHub webhook payload
        print("Received webhook event:", data)
        return jsonify({'status': 'Webhook received successfully!'}), 200

# Your existing route for lesson completion status
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
                    color: #FFD700; /* Gold color for a glowing effect */
                    text-shadow: 0 0 10px rgba(255, 215, 0, 0.8), 0 0 20px rgba(255, 215, 0, 0.6), 0 0 30px rgba(255, 215, 0, 0.4);
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
            <div class="status">Lesson Completed: 90%</div>
        </body>
    </html>
    '''
    return render_template_string(html_content)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
