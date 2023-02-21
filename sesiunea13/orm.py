"""
ORM - Object Relation Mapping
"""

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)


# connect to db
engine = create_engine('sqlite:///users.db')

# create all tables
Base.metadata.create_all(engine)

# start a session
Session = sessionmaker(bind=engine)
session = Session()

# add user
u1 = User(name='John', age=30)
u2 = User(name='Jane', age=29)
# session.add(u1)
# session.add(u2)
session.commit()

# select
users = session.query(User).all()
for user in users:
    print(user.id, user.name, user.age)

# update
user = session.query(User).filter_by(name='John').first()
user.age = 31
session.commit()
user = session.query(User).filter_by(name='John').first()
print(user.name, user.age)

# delete
user = session.query(User).filter_by(name='Jane').first()
session.delete(user)
session.commit()

users = session.query(User).all()
for user in users:
    print(user.id, user.name, user.age)
