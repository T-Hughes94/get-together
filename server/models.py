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
    name = db.Column(db.String, nullable=False)
    _password_hash = db.Column(db.String, nullable=False)
    DOB = db.Column(db.DateTime)
    dietary_restrictions = db.Column(db.String)
    profile_image = db.Column(db.String)

    #relationships
    hosts = db.relationship('Host', back_populates='user')
    guests = db.relationship('Guest', back_populates='user')
    event_blockeds = db.relationship('EventBlocked', back_populates='user', cascade = 'all, delete')
    
        # returns the other users that this user has blocked
    blockers = db.relationship('UserBlock', foreign_keys='UserBlock.blocker_id', back_populates = 'blocker_relation', cascade = 'all, delete')
    
        # returns the other users that have blocked this user
    blockees = db.relationship('UserBlock', foreign_keys='UserBlock.blockee_id', back_populates = 'blockee_relation', cascade = 'all, delete')

    # serialize rules
    # serialize_rules = ("-hosts.user", "-guests.user", "-event_blockeds.user", "-blockers.blocker_relation", "-blockees.blockee_relation")
    # serialize_rules = ("-hosts.user", "-guests.user", "-event_blockeds.user", "-blockers.blocker_relation", "-blockees", "-blockers.blockee_relation")
    # serialize_rules = ("-hosts.user", "-guests.user", "-event_blockeds.user", "-blockers", "-blockees")
    serialize_only = ("name", "dietary_restrictions", "profile_image", "hosts.event_id", "event_blockeds.event_id", "blockers.blockee_id", "blockees.blocker_id", "guests.invites", "guests.event_id")

    # methods
    # block another user (input the entire blockee)
    def block(self, blockee):
        new_block = UserBlock(
            blocker_id = self.id,
            blockee_id = blockee.id
        )
        db.session.add(new_block)
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
    invites = db.relationship('Invite', back_populates = ('host'), cascade = 'all, delete')

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
    invites = db.relationship('Invite', back_populates = ('guest'), cascade = 'all, delete')

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
    # serialize_rules = ("-host.invites", "-guest.invites", "-host.user", "-host.event", "-guest.event", "-guest.user")
    serialize_only = ("host.user.name", "guest.user.name")

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
    event_blockeds = db.relationship('EventBlocked', back_populates='event', cascade = 'all, delete')
    hosts = db.relationship('Host', back_populates='event', cascade = 'all, delete')
    guests = db.relationship('Guest', back_populates='event', cascade = 'all, delete')

    # serialize rules
    # serialize_rules = ("-event_blockeds.event", "-hosts.event", "-guests.event")
    serialize_only = ("hosts.user", "guests.user", "event_blockeds.user", "description", "image", "titled")

    # methods
    def all_blocked(self):
        # people blocked by the hosts
        host_users = []
        for host in self.hosts:
            host_users.append(host.user)
        blocked_by_hosts = []
        for user in host_users:
            for ub in user.blockers:
                blocked_by_hosts.append(ub.blockee_relation)
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


class UserBlock(db.Model, SerializerMixin):
    __tablename__ = "user_blocks"

    id = db.Column(db.Integer, primary_key = True)

    blocker_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    blockee_id = db.Column(db.Integer, db.ForeignKey("users.id"))

    # relationships
    blocker_relation = db.relationship("User", foreign_keys=[blocker_id], back_populates="blockers")
    blockee_relation = db.relationship("User", foreign_keys=[blockee_id], back_populates="blockees")

    serialize_rules = ("-blockee_relation.blockees", "-blocker_relation.blockers")