from flask import Flask, jsonify, render_template_string

app = Flask(__name__)

# Route to display lesson completion status with image
@app.route('/lesson-complete', methods=['GET'])
def lesson_complete():
    # Create HTML content with an image and a comment
    html_content = '''
    <html>
        <body>
            <h1>Lesson Completed: 99%</h1>
            <img src="{{ url_for('NewGlobe', filename='demo_image.jpeg') }}" alt="Demo Image" width="300">
        </body>
    </html>
    '''
    return render_template_string(html_content)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
