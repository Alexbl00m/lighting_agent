from sqlalchemy import create_engine, Column, String, Text, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class ProductSpec(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    spec = Column(Text)
    improvements = Column(Text)
    source_pdf = Column(String)

# Skapa engine och session
engine = create_engine('sqlite:///products.db')  # Eller postgres URL
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()
