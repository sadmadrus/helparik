from sqlalchemy import create_engine, Column, Integer, String
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
        print(f"Технология {technology} не найдена")
    return None