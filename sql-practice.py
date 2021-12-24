from sqlalchemy import (
    create_engine, Column, Integer, String
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# executing the instructions from the "chinook" database
db = create_engine("postgresql:///chinook")
base = declarative_base()


# create a class-based model for "FavouritePlaces" table
class FavouritePlaces(base):
    __tablename__ = "FavouritePlaces"
    id = Column(Integer, primary_key=True)
    country = Column(String)
    capital = Column(String)


# instead of connecting to the database directly, we will ask for a session
# create a new instance of sessionmaker, then point to our engine (the db)
Session = sessionmaker(db)
# opens an actual session by calling the Session() subclass defined above
session = Session()

# creating the database using declarative_base subclass
base.metadata.create_all(db)

lake_district = FavouritePlaces(
    country="England",
    capital="London" 
)

snowdonia = FavouritePlaces(
    country="Wales",
    capital="Cardiff"
)

# add each instance of our favourite places to our session
session.add(lake_district)
session.add(snowdonia)

# commit our session to the database
session.commit()

# query the database to find all favourite places
places = session.query(FavouritePlaces)
for place in places:
    print(
        place.country,
        place.capital,
        sep=" | "
    )