'''Załadować do bazy danych postgres pythonem zawartość pliku foods.csv
Załadować do bazy danych sqllite pythonem zawartość pliku foods.csv korzystając z SQLa
Załadować do bazy danych sqllite pythonem zawartość pliku foods.csv korzystając z SQL Alchemy'''

'''session.add(fooditem)
session.commit()
'''

import csv
import os

print(os.getcwd())
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine

Base = automap_base()
db_url = "postgresql+psycopg2://my_user:secret@127.0.0.1/my_database"
engine = create_engine(db_url)

engine.echo = True #pokazuje co sie dzieje w sqlu

# reflect the tables
Base.prepare(engine, reflect=True)
FoodItem = Base.classes.fooditem
session = Session(engine)

with open('foods.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row)
        food_item = FoodItem(name=row["name"], price=row["price"])
        session.add(food_item)
    session.commit()

