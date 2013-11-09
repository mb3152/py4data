from sqlite3 import dbapi2 as sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash, render_template, send_from_directory
import os
from werkzeug import secure_filename
from pybtex.database.input import bibtex
from collections import defaultdict
import pandas as pd

#configuration and upload stuff 
app = Flask(__name__)
app.config.update(dict(
    DATABASE='bibtex.db',
    DEBUG=True,
    SECRET_KEY='development key',
    USERNAME='mb3152',
    PASSWORD='testing'))
app.config.from_envvar('FLASKR_SETTINGS', silent=True)
#path where uploaded files will go.
app.config['UPLOAD_FOLDER'] = 'uploads/'
# Only accept bibtex files
app.config['ALLOWED_EXTENSIONS'] = set(['bib'])
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in app.config['ALLOWED_EXTENSIONS']

#start page
@app.route('/')
def index():
    return render_template('welcome2.html')

# upload the bibtex, store in database
@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    collection = request.form['collection']
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    db = get_db()
    parser = bibtex.Parser()
    bibdata = parser.parse_file(filename)
    try:
        sql = (""" 
            CREATE TABLE %s (Title text, Journal text, Author text, Year text, Keywords text)
            """
            %(collection))
        db.execute(sql)
    except OperationalError:
        #table already exists
        sql = (("""DROP TABLE %s""")%(collection))
        db.execute(sql)
        sql = (""" 
            CREATE TABLE %s (Title text, Journal text, Author text, Year text, Keywords text)
            """
            %(collection))
        db.execute(sql)

    for bib_id in bibdata.entries:
        b = bibdata.entries[bib_id].fields
        try:
            try:
                title = b["title"]
                title = title.replace('{}','()')
            except:
                title = 'null'
            try:
                journal = b["journal"]
                journal = journal.replace("\\", "")
                journal = journal.replace('{}','()')
            except:
                journal = 'null'
            try:
                author = b["author"]
                author = author.replace('{}','()')
            except:
                author = 'null'
            try:
                year = b['year']
                year = year.replace('{}','()')
                year = str(year)
            except:
                year = 'null'
            try:
                keywords=b["keywords"]
                keywords = keywords.replace('{}','()')
            except:
                keywords = 'null'
            sql = ("""
                INSERT INTO %s VALUES ('%s', '%s','%s','%s','%s') """
                %(collection, title, journal, author,year,keywords))
            db.execute(sql)
            db.commit()
        except:
            print 'File missing value!'
    return redirect(url_for('query'))

@app.route('/query', methods=['GET', 'POST'])
def query():
    return render_template('query2.html')


@app.route('/query_db', methods=['GET', 'POST'])
def query_db():
    userquery = request.form['userquery']
    db = get_db()
    cur = db.execute(userquery)
    entries = []
    for row in cur.fetchall():
        x = dict(Title=row[0], Journal=row[1], Author=row[2], Year=row[3], Keywords=row[4])
        entries.append(x)
    table = []
    for line in entries:
        z = '____________________________________'
        table.append(z)
        for x , y  in zip(line.values(),line.keys()):
            y= str(y) + ':'
            table.append(y)
            table.append(x)
    return render_template('show.html',data = table)

def init_db():
    with app.app_context():
        db = get_db()
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()
def get_db():
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = connect_db()
    return g.sqlite_db
def connect_db():
    rv = sqlite3.connect(app.config['DATABASE'])
    rv.row_factory = sqlite3.Row
    return rv

if __name__ == '__main__':
    init_db()
    app.run()