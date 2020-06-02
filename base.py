from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

url = 'sqlite:///database.db'

engine = create_engine(url)
Session = sessionmaker(bind=engine)
Base = declarative_base()