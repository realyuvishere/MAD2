from flask import render_template, current_app as app, request, redirect, url_for
from datetime import datetime

@app.route('/', methods=['GET'])
def user_dashboard():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def user_search():
    return render_template('user_search.html')