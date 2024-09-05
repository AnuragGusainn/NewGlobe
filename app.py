from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/lesson-complete', methods=['GET'])
def lesson_complete():
    return jsonify({"status": "Lesson Completed 90%"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)

