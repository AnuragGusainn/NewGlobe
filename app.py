from flask import Flask, render_template_string

app = Flask(__name__)

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
                    font-size: 2em;
                    color: #4CAF50;
                    animation: fadeIn 3s ease-in-out, pulse 1.5s infinite;
                }
                @keyframes fadeIn {
                    from { opacity: 0; }
                    to { opacity: 1; }
                }
                @keyframes pulse {
                    0% { transform: scale(1); }
                    50% { transform: scale(1.05); }
                    100% { transform: scale(1); }
                }
            </style>
        </head>
        <body>
            <div class="status">Lesson Completed: 75%</div>
        </body>
    </html>
    '''
    return render_template_string(html_content)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
