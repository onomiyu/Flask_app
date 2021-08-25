import flask
from main import app, db
from main.models import Entry

@app.route('/')
def show_entries():
    entries = Entry.query.all()
    return flask.render_template('entries.html', entries=entries)

@app.route('/add',methods=['POST'])
def add_entry():
    entry = Entry(name = flask.request.form['name'], want = flask.request.form['want'])
    db.session.add(entry)
    db.session.commit()
    return flask.redirect(flask.url_for('show_entries'))
