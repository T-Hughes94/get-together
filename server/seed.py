# #!/usr/bin/env python3

# # Standard library imports
# from random import randint, choice as rc

# # Remote library imports
# from faker import Faker

# # Local imports
# from app import app
# from models import db

# if __name__ == '__main__':
#     fake = Faker()
#     with app.app_context():
#         print("Starting seed...")
#         # Seed code goes here!


from random import choice as rc, randint
from faker import Faker
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app import app
from models import db, Cake, CakeBakery, Bakery
with app.app_context():
    print("Starting seed...")
fake = Faker()
def createcakes():
    cakes = []
    for _ in range(10):
        c = Cake(
            name = fake.name(),
            description = fake.sentence(),
         )
        cakes.append(c)
    return cakes

def createbakeries():
    bakery= []
    for _ in range(10):
        b = Bakery(
            name = fake.name(),
            address = fake.address(),
         )
        bakery.append(b)
    return bakery 

def createcakebakeries():
    cakebakeries= []
    for _ in range(10):
       cakebakeries.append(CakeBakery(
            price = randint(1,100),
            cake_id = randint(1,10),
            bakery_id = randint(1,10),
        ))
    return cakebakeries

if name == 'main':
    with app.app_context():
        Cake.query.delete()
        Bakery.query.delete()
        CakeBakery.query.delete()
        cakes = create_cakes()
        bakeries = create_bakeries()
        cakebakeries = create_cakebakeries()

        db.session.add_all(cakes)
        db.session.add_all(cakebakeries)
        db.session.add_all(bakeries)
        db.session.commit()