import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, Column, Integer, String, JSON
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from itemadapter import ItemAdapter

# Load environment variables from .env file
load_dotenv()

# Database setup
DATABASE_URL = os.getenv("DATABASE_URL")
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

# Define the model
class Hotel(Base):
    __tablename__ = 'hotels'

    id = Column(Integer, primary_key=True, autoincrement=True)
    country = Column(String)
    title = Column(String)
    img_src_list = Column(JSON)
    rating = Column(String)
    room = Column(String)
    price = Column(String)
    location = Column(String)

# Create the table
Base.metadata.create_all(engine)

class HotelscrapPipeline:
    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        hotel = Hotel(
            country=adapter.get('country'),
            title=adapter.get('title'),
            img_src_list=adapter.get('img_src_list'),
            rating=adapter.get('rating'),
            room=adapter.get('room'),
            price=adapter.get('price'),
            location=adapter.get('location')
        )
        session.add(hotel)
        session.commit()
        return item
