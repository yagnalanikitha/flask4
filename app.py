from flask import Flask, render_template, request
from langdetect import detect

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/detect_language', methods=['POST'])
def detect_language():
    input_text = request.form['input_text']
    detected_language = detect(input_text)
    return render_template('index1.html', detected_language=detected_language)

if __name__ == '__main__':
    app.run(debug=True)




