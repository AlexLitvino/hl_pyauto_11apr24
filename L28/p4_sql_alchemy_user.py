# Creating DB

from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, Double, String  # columns and data types kept in columns
from sqlalchemy.orm import sessionmaker, declarative_base

# Quering data
from sqlalchemy import and_, or_
from sqlalchemy import select

sqlite_filepath = r'alchemy.db'
db_path = f"sqlite:///{sqlite_filepath}"
print(db_path)

# Create engine and session
engine = create_engine(db_path)
Session = sessionmaker(engine)  # sessions factory
session = Session()


Base = declarative_base()  # creates the Base class, which is what all models inherit from and how they get SQLAlchemy ORM functionality

# Create table
class User(Base):

    __tablename__ = 'Users'  # table name

    # column definition
    user_id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)
    salary = Column(Double)

    def __str__(self):
        return f"User: {self.name}\nage: {self.age}\nsalary: {self.salary}"

    def __repr__(self):
        return f"User(name={self.name}, age={self.age}, salary={self.salary})"


# Create defined tables, put in function and call when all tables are defined
# Be careful, at first you should define all table-classes (import them) and only after that call create_all, or tables will not be created
Base.metadata.create_all(engine)


results = session.query(User).all()  # SELECT * FROM Users;
print(results)

# # Adding data to table (many lines and line by line)
#
# users = [User(name='John Smith', age=34, salary=534.23),
#          User(name='Anna Smith', age=23, salary=3434.23),
#          User(name='Andrew Gimli', age=21, salary=4534.23),
#          User(name='Aragorn Aratornovich', age=54, salary=4574.3),
#          ]
# session.add_all(users)

# results = session.query(User).all()  # SELECT * FROM Users;
# print(results)

# users2 = [User(name='Torin Trorovich', age=34, salary=534.23),
#           User(name='Isildur Elendilevich', age=23, salary=3434.23),
#           ]
# for user in users2:
#     session.add(user)
# session.commit()  # data will be added to DB on disk only after call commit()

# results = session.query(User).all()
# print(results)
# u = results[0]
# print(u.name)
# print()
#
#
#

# results = session.query(User).filter(User.name.like('%Smith')).all()
# print(results)
#
# results = session.query(User).filter(and_(User.name.like('%Smith'), User.age < 30)).all()
# print(results)



# stmt = select(User).where(User.name == "John Smith")
# print(stmt)
# result = session.execute(stmt)
# print(result.fetchall())
#
# print()
# stmt = select(User).where(User.age == 23).limit(2)
# result = session.execute(stmt)
# print(result.fetchall())
# print()
#
# stmt = select(User).where(User.name == "John Smith").limit(1)
# result = session.execute(stmt)
# print(result.fetchall())
#
# print()
# #stmt = select(User).where(User.name == "John Smith").order_by(User.age)
# #stmt = select(User).order_by(User.age.asc())  # ascending
# stmt = select(User).order_by(User.age.desc())  # descending
# result = session.execute(stmt)
# print(result.fetchall())
#
# print()
# stmt = select(User.name).limit(3)
# result = session.execute(stmt)
# print(result.fetchall())
# print(result.fetchall())

session.close()
