from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
class Database:
    def __init__(self):
        self.engine = create_engine('sqlite:///database.db', echo=True)
        self.Session = sessionmaker(bind=self.engine)

    def init_db(self):
        Base.metadata.create_all(self.engine)

    def drop_all(self):
        Base.metadata.drop_all(self.engine)

    def get_session(self):
        return self.Session()

    def get_engine(self):
        return self.engine





