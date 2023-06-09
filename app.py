from flask import Flask, request, render_template
from logic import analyse_postcode

app = Flask(__name__)

@app.template_filter('comma')
def add_commas(value):
    return "{:,.0f}".format(value)

@app.route('/')
def my_form():
    return render_template('index.html', data="")

@app.route('/', methods=['POST'])
def my_form_post():
    text = request.form['text']
    processed_text = analyse_postcode(text)
    if processed_text:
        return render_template('index.html', data=processed_text)
    else:
        return render_template('index.html', data=processed_text)

app.run()