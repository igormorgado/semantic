import os
from flask import Flask, render_template, g, jsonify, request, redirect, url_for, session, flash
from gensim import corpora

from nlp import nlp
LangServices = nlp()

app = Flask (__name__,
             static_folder = './dist/static',
             template_folder = './dist')

@app.route("/home")
def hello():
    return "Hello world from flask"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/keywords', methods=['GET', 'POST'])
def keywords():
    response_object = {'keywords': ['birds', 'scatt']}
    post_data = request.get_json()
    if post_data['text'] is not None:
        keywords = LangServices.keywords(post_data['text'])
        if len(keywords) > 0:
            response_object = {'keywords': keywords['ranked phrases']}
    return jsonify(response_object)

port = os.getenv ('PORT', '5006')
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(port), debug=True)
    # serve(app, url_scheme='http', threads=4, port=int(port))
