from flask import render_template, request
from app import app
from scanner.sql_injection import check_sql_injection
from scanner.xss import check_xss

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        url = request.form['url']
        sql_result = check_sql_injection(url)
        xss_result = check_xss(url)
        return render_template('index.html', sql_result=sql_result, xss_result=xss_result)
    return render_template('index.html')
