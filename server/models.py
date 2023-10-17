from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy.orm import validates
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy_serializer import SerializerMixin
from config import bcrypt

from config import db

# Models Here:


class User( db.Model, SerializerMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False, unique=True)
    _password_hash = db.Column(db.String, nullable=False)
    DOB = db.Column = db.Column(db.Date, nullable = False)
    dietary_restrictions = db.Column(db.String)
    profile_image = db.Column(db.String)

    #relationship

    hosts = db.relationship('Host', back_populates='user')
    guests = db.relationship('Guest', back_populates='user')
    event_blockeds = db.relationship('EventBlocked', back_populates='user')
    blocker = db.relationship('UserBlocked', back_populate = 'blocker')
    blockee = db.relationship('UserBlocked', back_populates = 'blockee')

    # need to write the relationships for user blocked 
    # blocked_users = db.relationship('UserBlocked', back_populates='blocker')

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


    # #relationships

    # hosted_by = db.relationship('User', back_populates='hosts')
    # hosted_event = db.relationship('Event', back_populates='hosts')



class Guest(db.Model, SerializerMixin):
    __tablename__  = 'guests'

    id = db.Column(db.Integer, primary_key = True)
    rsvp = db.Column(db.String)

    #relationships with Foreign Key

    user_id = db.Column(db.Integer, db.ForeignKey('user_table.id')) 
    user = db.relationship('User', back_populates= 'guests')
    
    event_id = db.Column(db.Integer, db.ForeignKey('event_table.id'))
    event = db.relationship('Event', back_populates= ('guests'))

    # relationships
    invites = db.relationship('Invite', back_populates = ('guest'))
    # #relationships

    # attended_by = db.relationship('User', back_populates='guests')
    # attended_event = db.relationship('Event', back_populates='guests')




class Invite(db.Model, SerializerMixin):
    __tablename__ = 'invites'

    id = db.Column(db.Integer, primary_key = True)
 

    #relationships with Foreign Key

    host_id = db.Column(db.Integer, db.ForeignKey('hosts.id'))
    host = db.relationship('Host', back_populates=('invites'))

    guest_id = db.Column(db.Integer, db.ForeignKey('guests.id'))
    guest = db.relationship('Guest', back_populates=('invites'))


class UserBlocked(db.Model, SerializerMixin):
    __tablename__ = 'user_blockeds'

    id = db.Column(db.Integer, primary_key = True)


    #relationships with ForeignKey

    blocker_id = db.Column(db.Integer, db.ForeignKey('user_table.id'))
    blocker = db.relationship('User', back_populates='blocker')

    blockee_id = db.Column(db.Integer, db.ForeignKey('user_table.id'))
    blockee = db. relationship('User', back_populates=('blockee'))



class Event(db.Model, SerializerMixin):
    __tablename__ = 'events'

    id = db.Column(db.Integer, primary_key = True)
    date = db.Column(db.Date)
    title = db.Column(db.String)
    description = db.Column(db.String)
    invite_only = db.Column(db.Boolean)
    age_limit = db.Column(db.Date)
    private_guest_list =db.Column(db.Boolean)
    private_party = db.Column(db.Boolean)
    image = db.Column(db.String)

    # #relationships with ForeignKey

    # user_id = db.Column(db.Integer, db.ForeignKey('user_table.id'))
    # user = db.relationship('User', back_populates='events')

    # event_id = db.Column(db.Integer, db.ForeignKey('event.id'))
    # event = db.relationship('')


    #relationships
        
    event_blockeds = db.relationship('EventBlocked', back_populates='event')
    hosts = db.relationship('Host', back_populates='event')
    guests = db.relationship('Guest', back_populates='event')




class EventBlocked(db.Model, SerializerMixin):
    __tablename__ = 'event_blockeds'

    id = db.Column(db.Integer, primary_key= True)


    #relationships with ForeignKey

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    user = db.relationship('User', back_populates=('event_blockeds'))

    event_id = db.Column(db.Integer, db.ForeignKey('events.id'))
    event = db.relationship('Event', back_populates=('event_blockeds'))

    # #relationships

    # blocked_users = db.relationship('User', back_populates='blocked_events')
    # blocked_event = db.relationship('Event', back_populates='blocked_users')




