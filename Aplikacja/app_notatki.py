# Przy pierwszym uruchomieniu:
# flask --app app shell
# A następnie:
# >>> db.create_all()
# >>> exit()
#
# Dalej uruchamiamy: flask --app app app
import sqlalchemy
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///notatki.db'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://my_user:secret@127.0.0.1/my_database'
db = SQLAlchemy(app)


class NoteTag(db.Model):
    __tablename__ = 'notetag'
    id = db.Column(db.Integer, primary_key=True)
    tag_id = db.Column(db.Integer, db.ForeignKey('tag.id'))
    note_id = db.Column(db.Integer, db.ForeignKey('note.id'))


class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tagname = db.Column(db.String(80), unique=True, nullable=False)

    def __repr__(self):
        return '<Tag %r>' % self.tagname


class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    body = db.Column(db.String(80), nullable=False)

    def __repr__(self):
        return '<Note %r>' % self.title

    tags = db.relationship("Tag",
                           secondary='notetag',
                           uselist=True,
                           backref='notes',
                           lazy='select')


def assign_tag(note_id, tagname, session):
    note = session.query(Note).filter_by(id=note_id).one()
    tag = session.query(Tag).filter_by(tagname=tagname).one()
    note.tags.append(tag)
    session.add(note)
    session.commit()
    return True


def remove_tag_note(note_id, tagname, session):
    note = session.query(Note).filter_by(id=note_id).one()
    note.tags = [tag for tag in note.tags if tag.tagname != tagname]
    session.add(note)
    session.commit()
    return True


def get_tags(session):
    return session.query(Tag).all()


def get_notes(session):
    return session.query(Note).all()


def create_tag(name, session):
    try:
        tag = Tag(tagname=name)
        session.add(tag)
        session.commit()
    except sqlalchemy.exc.IntegrityError as e:
        print(e)
        session.rollback()
        return False
    else:
        return True


def create_note(title, body, session):
    try:
        note = Note(title=title, body=body)
        session.add(note)
        session.commit()
    except sqlalchemy.exc.IntegrityError as e:
        print(e)
        session.rollback()
        return False
    else:
        return True


def remove_tag(name, session):
    tag = session.query(Tag).filter_by(tagname=name).one()
    session.delete(tag)
    session.commit()


def remove_note(id, session):
    note = session.query(Note).filter_by(id=id).one()
    session.delete(note)
    session.commit()


@app.route('/')
def hello():
    return render_template('form_notatki.html', data=get_tags(db.session)
                           , data2=get_notes(db.session),
                           tytul="Notatki", no_error=True)


@app.route('/assign_tag')
def assign():
    note_id = request.args['note_id']
    tagname = request.args['tagname']
    assign_tag(note_id, tagname, db.session)
    return render_template('form_notatki.html', data=get_tags(db.session)
                           , data2=get_notes(db.session),
                           tytul="Notatki", no_error=True)

@app.route('/remove_tag_note')
def get_remove_tag_note():
    note_id = request.args['note_id']
    tagname = request.args['tagname']
    remove_tag_note(note_id, tagname, db.session)
    return render_template('form_notatki.html', data=get_tags(db.session)
                           , data2=get_notes(db.session),
                           tytul="Notatki", no_error=True)


@app.route('/add_tag')
def add():
    args = request.args
    no_error = create_tag(args["name"], db.session)
    if no_error:
        tytul = "Dodano znacznik"
    else:
        tytul = "Taka znacznik już istnieje"

    return render_template('form_notatki.html', data=get_tags(db.session),
                           data2=get_notes(db.session),
                           no_error=no_error,
                           tytul=tytul)


@app.route('/add_note')
def add_note():
    args = request.args
    no_error = create_note(args["title"], args["body"], db.session)
    if no_error:
        tytul = "Dodano Notatke"
    else:
        tytul = "Taka notatka już istnieje"

    return render_template('form_notatki.html', data=get_tags(db.session),
                           data2=get_notes(db.session),
                           no_error=no_error,
                           tytul=tytul)


@app.route('/remove_tag')
def remove():
    args = request.args
    remove_tag(args["values"], db.session)
    no_error = True
    if no_error:
        tytul = "Usunieto znacznik"
    return render_template('form_notatki.html', data=get_tags(db.session),
                           data2=get_notes(db.session),
                           no_error=no_error,
                           tytul=tytul)