from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy.orm import validates
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.hybrid import hybrid_property
from config import bcrypt

from config import db

# Models Here:


class User( db.Model, SerializerMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False, unique=True)
    _password_hash = db.Column(db.String, nullable=False)
    DOB = db.Column(db.DateTime, nullable = False)
    dietary_restrictions = db.Column(db.String)
    profile_image = db.Column(db.String)

    #relationships
    hosts = db.relationship('Host', back_populates='user')
    guests = db.relationship('Guest', back_populates='user')
    event_blockeds = db.relationship('EventBlocked', back_populates='user')
    
        # returns the other users that this user has blocked
    blockers = db.relationship('Blocker', back_populates = 'user')
    
        # returns the other users that have blocked this user
    blockees = db.relationship('Blockee', back_populates = 'user')

    # serialize rules
    serialize_rules = ("-hosts.user", "-guests.user", "-event_blockeds.user", "-blockers.user", "-blockees.user")
    # methods
    # block another user (input the entire blockee)
    def block(self, blockee):
        new_blocker = Blocker(
            user_id = self.id
        )
        new_blockee = Blockee(
            user_id = blockee.id
        )
        db.session.add(new_blockee, new_blocker)
        db.session.commit()
        new_blocker.blockee_id = new_blockee.id
        new_blockee.blocker_id = new_blocker.id
        db.session.add(new_blockee, new_blocker)
        db.session.commit()


    #password code
    @hybrid_property
    def password_hash(self):
        return self._password_hash
    
    @password_hash.setter
    def password_hash(self, password):
        password_hash = bcrypt.generate_password_hash(
            password.encode('utf-8')
        )
        self._password_hash = password_hash.decode('utf-8')

    def authenticate(self, password):
        return bcrypt.check_password_hash(
            self._password_hash, password.encode('utf-8')
        )


class Host(db.Model, SerializerMixin):
    __tablename__ = 'hosts'

    id = db.Column(db.Integer, primary_key = True)

    #relationships with Foreign Key
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    user = db.relationship('User', back_populates=('hosts'))

    event_id = db.Column(db.Integer, db.ForeignKey('events.id'))
    event = db.relationship('Event', back_populates=('hosts'))

    # relationship
    invites = db.relationship('Invite', back_populates = ('host'))

    # serialize rules
    serialize_rules = ("-user.hosts", "-event.hosts", "-invites.host")




class Guest(db.Model, SerializerMixin):
    __tablename__  = 'guests'

    id = db.Column(db.Integer, primary_key = True)
    rsvp = db.Column(db.String)

    #relationships with Foreign Key

    user_id = db.Column(db.Integer, db.ForeignKey('users.id')) 
    user = db.relationship('User', back_populates= 'guests')
    
    event_id = db.Column(db.Integer, db.ForeignKey('events.id'))
    event = db.relationship('Event', back_populates= ('guests'))

    # relationships
    invites = db.relationship('Invite', back_populates = ('guest'))

    # serialize rules
    serialize_rules = ("-user.guests", "-event.guests", "-invites.guest")




class Invite(db.Model, SerializerMixin):
    __tablename__ = 'invites'

    id = db.Column(db.Integer, primary_key = True)
 

    #relationships with Foreign Key
    host_id = db.Column(db.Integer, db.ForeignKey('hosts.id'))
    host = db.relationship('Host', back_populates=('invites'))

    guest_id = db.Column(db.Integer, db.ForeignKey('guests.id'))
    guest = db.relationship('Guest', back_populates=('invites'))

    # serialize rules
    serialize_rules = ("-host.invites", "-guest.invites", "-host.user", "-host.event")


class Event(db.Model, SerializerMixin):
    __tablename__ = 'events'

    id = db.Column(db.Integer, primary_key = True)
    date = db.Column(db.DateTime)
    title = db.Column(db.String)
    description = db.Column(db.String)
    invite_only = db.Column(db.Boolean)
    age_limit = db.Column(db.DateTime)
    private_guest_list =db.Column(db.Boolean)
    private_party = db.Column(db.Boolean)
    image = db.Column(db.String)

    #relationships
    event_blockeds = db.relationship('EventBlocked', back_populates='event')
    hosts = db.relationship('Host', back_populates='event')
    guests = db.relationship('Guest', back_populates='event')

    # serialize rules
    serialize_rules = ("-event_blockeds.event", "-hosts.event", "-guests.event")

    # methods
    def all_blocked(self):
        # people blocked by the hosts
        host_users = []
        for host in self.hosts:
            host_users.append(host.user)
        blocked_by_hosts = []
        for user in host_users:
            for blocker in user.blockers:
                blocked_by_hosts.append(blocker.blockee.user)
        # people blocked for the event specifically
        blocked_by_event=[]
        for block in self.event_blockeds:
            blocked_by_event.append(block.user)
        full_list = list(set(blocked_by_event+blocked_by_hosts))
        
        return full_list


class EventBlocked(db.Model, SerializerMixin):
    __tablename__ = 'event_blockeds'

    id = db.Column(db.Integer, primary_key= True)
    #relationships with ForeignKey

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    user = db.relationship('User', back_populates=('event_blockeds'))

    event_id = db.Column(db.Integer, db.ForeignKey('events.id'))
    event = db.relationship('Event', back_populates=('event_blockeds'))

    # serialize rules
    serialize_rules = ("-user.event_blockeds", "-event.event_blockeds")


class Blocker(db.Model, SerializerMixin):
    __tablename__ = 'blockers'

    id = db.Column(db.Integer, primary_key= True)
    
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    user = db.relationship("User", back_populates = "blockers")

    blockee_id = db.Column(db.Integer, db.ForeignKey('blockees.id'))
    blockee = db.relationship('Blockee', back_populates='blocker')

    serialize_rules = ("-user.blockers", "-blockee.blocker")

class Blockee(db.Model, SerializerMixin):
    __tablename__ = "blockees"
    
    id = db.Column(db.Integer, primary_key= True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    user = db.relationship("User", back_populates = "blockees")

    blocker_id = db.Column(db.Integer, db.ForeignKey('blockers.id'))
    blocker = db.relationship('Blocker', back_populates='blockee')

    serialize_rules = ("-user.blockees", "-blockee.blockee")
