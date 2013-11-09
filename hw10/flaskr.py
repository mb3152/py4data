from sqlite3 import dbapi2 as sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash, render_template, send_from_directory
import os
from werkzeug import secure_filename
from pybtex.database.input import bibtex


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
    return render_template('welcome.html')

# upload the bibtex, store in database
@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    db = get_db()
    parser = bibtex.Parser()
    bibdata = parser.parse_file(filename)
    db.execute("""DROP TABLE collection""")
    db.execute("""CREATE TABLE collection
                  (title text, journal text, author text) 
               """)
    for bib_id in bibdata.entries:
        b = bibdata.entries[bib_id].fields
        try:
            title = b["title"]
            journal = b["journal"]
            author = b["author"]
            sql = ("""
                INSERT INTO collection VALUES ('title', 'journal', 'author')
                """) # want to get input and name collection
            db.execute(sql)
            db.commit()
            print 'put ' + title + ' into database'
        except KeyError:
            print str(KeyError) 
    return redirect(url_for('query'))


@app.route('/query', methods=['GET', 'POST'])
def query():
    return render_template('query.html')

@app.route('/query_db', methods=['GET', 'POST'])
def query_db():
    userquery = request.form['userquery']
    db = get_db()
    cur = db.execute(userquery)
    entries = cur.fetchall()
    print entries
    return repr(entries)

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