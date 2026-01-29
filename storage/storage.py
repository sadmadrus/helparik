import datetime

from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    user_id = Column(Integer)
    first_name = Column(String)
    last_name = Column(String)

    def __init__(self, name, user_id, first_name, last_name):
        self.name = name
        self.user_id = user_id
        self.first_name = first_name
        self.last_name = last_name

    def __repr__(self):
        return f'<User(name={self.name}, user_id={self.user_id}, first_name={self.first_name}, last_name={self.last_name})>'

class Technology(Base):
    __tablename__ = 'technologies'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)

    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __repr__(self):
        return f'<Technology(name={self.name}, description={self.description})>'

class Comment(Base):
    __tablename__ = 'comments'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    technology_id = Column(Integer)
    comment = Column(String)

    def __init__(self, user_id, technology_id, comment):
        self.user_id = user_id
        self.technology_id = technology_id
        self.comment = comment

    def __repr__(self):
        return f'<Comment(user_id={self.user_id}, technology_id={self.technology_id}, comment={self.comment})>'
class Events(Base):
    __tablename__ = 'events'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    event_type = Column(String)
    timestamp = Column(DateTime)
    event_date = Column(DateTime)
    message = Column(String)
    def __init__(self, user_id, event_type, timestamp, event_date, message):
        self.user_id = user_id
        self.event_type = event_type
        self.timestamp = timestamp
        self.event_date = event_date
        self.message = message

    def __repr__(self):
        return f'<Events(user_id={self.user_id}, event_type={self.event_type}, timestamp={self.timestamp}, event_date={self.event_date})>'

engine = create_engine('sqlite:///users.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()


def add_user(name, user_id, first_name, last_name):
    existing_user = session.query(User).filter_by(user_id=user_id).first()
    session.query(User).filter_by(user_id=user_id).first()
    if existing_user:
        return existing_user
    else:
        user = User(name, user_id, first_name, last_name)
        session.add(user)
        session.commit()
        return user

def getCommetnBytech(technology):
    tech = session.query(Technology).filter_by(name=technology).first()
    if tech:
        comments = session.query(Comment).filter_by(technology_id=tech.id).all()
        return comments
    else:
        return None

def addComment(user_id, technology, comment):
    tech = session.query(Technology).filter_by(name=technology).first()
    if tech:
        comment = Comment(user_id, tech.id, comment)
        session.add(comment)
        session.commit()
        return comment
    else:
        return None

def getCommentsByUser(user_id):
    comments = session.query(Comment).filter_by(user_id=user_id).all()
    return comments

def GetCommetsByUserAndTechnology(user_id, technology=None):
    if technology:
        tech = session.query(Technology).filter_by(id=technology).first()
    comments = session.query(Comment).filter(user_id==user_id and technology==tech.id).all()
    return comments

def getEvents():
    events = session.query(Events).filter(Events.event_date <= datetime.datetime.now()).all()
    return events

def GetTechnologiesID(technology):
    technologies = session.query(Technology).filter_by(name=technology).first()
    return technologies
def addEvent(user_id, event_type, event_date, message):
    event = Events(user_id, event_type, datetime.datetime.now(), event_date, message)
    session.add(event)
    session.commit()
    return event

def removeEvent(event_id):
    event = session.query(Events).filter_by(id=event_id).first()
    session.delete(event)
    session.commit()
    return event
