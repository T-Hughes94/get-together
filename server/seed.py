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


# from random import choice as rc, randint
import random
from faker import Faker
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app import app
from models import db, User, Host, Guest, Invite, UserBlocked, Event, EventBlocked, Blocker, Blockee

with app.app_context():
    print("Starting seed...")

fake = Faker()

def rand_bool():
    v = random.randint(0,1)
    if v == 1:
        return True
    else:
        return False
    
def create_users():
    def restrictions():
        x = random.randint(0,1)
        if x == 1:
            return "None"
        else:
            return fake.text()
    users = []
    for _ in range(10):
        u = User(
            name = fake.name(),
            DOB = fake.date_time(),
            dietary_restrictions = restrictions(),
            profile_image = 'https://i.pinimg.com/550x/18/b9/ff/18b9ffb2a8a791d50213a9d595c4dd52.jpg',
            password_hash = fake.name()
        )
        users.append(u)
    return users

def create_events():
    events= []
    for _ in range(10):
        e = Event(
            date = fake.date_time(),
            title = fake.name(),
            description = fake.text(),
            invite_only = rand_bool(),
            age_limit = fake.date_time(),
            private_guest_list = rand_bool(),
            private_party = rand_bool(),
            image = "https://t4.ftcdn.net/jpg/01/20/28/25/360_F_120282530_gMCruc8XX2mwf5YtODLV2O1TGHzu4CAb.jpg"
         )
        events.append(e)
    return events 

def create_guests():
    guests = []
    for _ in range(10):
        rsvp_num = random.randint(0,2)
        if rsvp_num == 0:
            rsvp = "Yes"
        elif rsvp_num == 1:
            rsvp = "No"
        else:
            rsvp = " Maybe"
        g = Guest(
            user_id = random.randint(1,10),
            event_id = random.randint(1,10),
            rsvp = rsvp
        )
        guests.append(g)
    return guests

def create_hosts():
    hosts = []
    for _ in range(10):
        h = Host(
            user_id = random.randint(1,10),
            event_id = random.randint(1,10)
        )
        hosts.append(h)
    return hosts

def create_invite():
    invites = []
    for _ in range(10):
        invite = Invite(
            host_id = random.randint(1,10),
            guest_id = random.randint(1,10)
        )
        invites.append(invite)
    return invites
    
def user_blocks():
    blocks = []
    for _ in range(10):
        blocks.append(UserBlocked())
    bnb = []
    block_index = 0
    for block in blocks:
        first_num = random.randint(1,10)
        second_num = random.randint(1,10)
        if second_num != first_num:
            bnb.append(Blocker(user_id = first_num, user_blocked_id = block_index))
            bnb.append(Blockee(user_id = second_num, user_blocked_id = block_index))
        block_index += 1
    return [blocks, bnb]



# def blocks_and_blockees():
#     bnb= []
#     for i in range(10):
#         first_num = fake.random.number(9)+1,
#         second_num = fake.random.number(9)+1,
#         if second_num != first_num:
#             bnb.append(Blocker(
#             user_id = first_num,
#             user_blocked_id = i
#             ))
#     return bnb

def blocked_events():
    create_blocked_events= []
    for _ in range(10):
            create_blocked_events.append(EventBlocked(
            user_id = random.randint(1,10),
            event_id = random.randint(1,10),
            ))
    return create_blocked_events

if __name__ == '__main__':
    with app.app_context():
        User.query.delete()
        Event.query.delete()
        Guest.query.delete()
        Host.query.delete()
        Invite.query.delete()
        UserBlocked.query.delete()
        EventBlocked.query.delete()
        
        users = create_users()
        events = create_events()
        guests = create_guests()
        hosts = create_hosts()
        invites = create_invite()
        blocked_users = user_blocks()
        blocked_events = blocked_events()


        db.session.add_all(users)
        db.session.add_all(events)
        db.session.add_all(guests)
        db.session.add_all(hosts)
        db.session.add_all(invites)
        db.session.add_all(blocked_users[0])
        db.session.add_all(blocked_users[1])
        db.session.add_all(blocked_events)

        db.session.commit()