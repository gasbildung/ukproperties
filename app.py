from flask import Flask, request, render_template
from logic import analyse_postcode

app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template('result.html')

@app.route('/', methods=['POST'])
def my_form_post():
    text = request.form['text']
    processed_text = analyse_postcode(text)
    if processed_text:
        return processed_text
    else:
        return "No data found, please try again."

app.run()