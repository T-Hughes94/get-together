#!/usr/bin/env python3

# Standard library imports

# Remote library imports
from flask import request, session, make_response, jsonify
from flask_restful import Resource

# Local imports
from config import app, db, api
# Add your model imports
from models import User, Event, Host, Guest, Invite, EventBlocked, Blocker, Blockee


# Views go here!

@app.route('/')
def index():
    return '<h1>Phase 4 Project Server</h1>'

############################ full crud user routes ########################################
@app.get('/users/ <int:id>')
def get_users_by_id(id):
    user = User.query.filter(User.id == id).first()

    if not user:
        return make_response(jsonify({"error": "User not found"}), 404)
    return make_response(jsonify(user.to_dict()), 200)

@app.post('/users')
def post_user():
    data = request.get_json()

    try:
        new_user = User(
            name=data.get("name"),
            DOB=data.get("DOB"),
            dietary_restrictions=data.get("dietary_restrictions"),
            profile_image = data.get("profile_image")
        )
        db.session.add(new_user)
        db.session.commit()

        return make_response(jsonify(new_user.to_dict()), 201)
    
    except ValueError:
        return make_response(jsonify({"error": ["validation errors"]}), 406)

@app.patch('/users/<int:id>')
def patch_user_by_id(id):
    user = User.query.filter(User.id == id).first()
    data = request.get_json()

    if not user:
        return make_response(jsonify({"error": "User not found"}), 404)

    try:
        for field in data:
            setattr(user, field, data[field])
        db.session.add(user)
        db.session.commit()

        return make_response(jsonify(user.to_dict()),202)
    
    except ValueError as e:
        print(e.str())
        return make_response(jsonify({"error": ["validation errors"]}),406)

@app.delete('/users/<int:id>')
def delete_user(id):
    user = User.query.filter(User.id == id).first()
    if not user:
        return make_response(jsonify({"error": "User not found"}),404)

    db.session.delete(user)
    db.session.commit()

    return make_response(jsonify({}), 204)


###################################### full crud for events ################################
@app.get('/events/<int:id>')
def get_events_by_id(id):
    event = Event.query.filter(Event.id == id).first()

    if not event:
        return make_response(jsonify({"error": "Event not found"}),404)
    return make_response(jsonify(event.to_dict()),200)

@app.post('/events')
def post_event():
    data = request.get_json()

    try:
        new_event = Event(
            date = data.get("date"),
            title = data.get("title"),
            description = data.get("description"),
            invite_only = data.get("invite_only"),
            age_limit = data.get("age_limit"),
            private_guest_list = data.get("private_guest_list"),
            private_party = data.get("private_party"),
            image = data.get("image")
        )
        db.session.add(new_event)
        db.session.commit()

        return make_response(jsonify(new_event.to_dict()), 201)
    
    except ValueError:
        return make_response(jsonify({"error": ["validation errors"]}), 406)

@app.patch('/events/<int:id>')
def patch_event_by_id(id):
    event = Event.query.filter(Event.id == id).first()
    data = request.get_json()

    if not event:
        return make_response(jsonify({"error": "Event not found"}), 404)

    try:
        for field in data:
            setattr(event, field, data[field])
        db.session.add(event)
        db.session.commit()


        return make_response(jsonify(event.to_dict()), 202)
    except ValueError as e:
        print(e.str())
        return make_response(jsonify({"error": ["validation errors"]}), 406)

@app.delete('/events/<int:id>')
def delete_event(id):
    event = event.query.filter(event.id == id).first()
    if not event:
        return make_response(jsonify({"error": "event not found"}), 404)

    db.session.delete(event)
    db.session.commit()

    return make_response(jsonify({}), 204)

################################### post patch delete for guest ###############################
class GuestById(Resource):

    def delete(self, id):
        guest = Guest.query.filter(Guest.id == id).first()
        if not guest:
            return {"error": "guest not found"}
        db.session.delete(guest)
        db.session.commit()

        return make_response(jsonify({}), 204)
    
    def patch(self, id):
        guest = Guest.query.filter(Guest.id == id).first()
        data = request.form
        try:
            for field in data:
                setattr(guest, field, data[field])
            db.session.add(guest)
            db.session.commit()

            return make_response(jsonify(guest.to_dict()), 202)
        except ValueError as e:
            print(e.str())
            return make_response(jsonify({"error": ["validation errors"]}), 406)
        
api.add_resource(GuestById, '/guests/<int:id>')
        
class Guests(Resource):
    def post(self):
        data = request.get_json()
        try:
            new_guest = Guest(
                user_id = data.get("user_id"),
                event_id = data.get("event_id"),
                rsvp = data.get("rsvp")
            )
            db.session.add(new_guest)
            db.session.commit()

            return make_response(new_guest.to_dict(), 201)
        except ValueError:
            return make_response({"error": ["validation errors"]},406)
        
api.add_resource(Guests, '/guests')


############################## post delete for host ################################
class HostById(Resource):

    def delete(self, id):
        host = Host.query.filter(Host.id == id).first()
        if not host:
            return {"error": "host not found"}
        db.session.delete(host)
        db.session.commit()

        return make_response(jsonify({}), 204)

api.add_resource(HostById, '/hosts/<int:id>')
        
class Hosts(Resource):
    def post(self):
        data = request.get_json()
        try:
            new_host = Host(
                user_id = data.get("user_id"),
                event_id = data.get("event_id")
            )
            db.session.add(new_host)
            db.session.commit()

            return make_response(new_host.to_dict(), 201)
        except ValueError:
            return make_response({"error": ["validation errors"]},406)
        
api.add_resource(Hosts, '/hosts')


############################## post delete for EventBlocked ##########################
@app.post('/events-blocked')
def create_blocked_event():
    data = request.get_json()

    try:
        new_blocked_event = EventBlocked(
            user_id = data.get("user_id"),
            event_id = data.get("event_id")
        )
        db.session.add(new_blocked_event)
        db.session.commit()

        return make_response(jsonify(new_blocked_event.to_dict()), 201)
    except ValueError:
        return make_response(jsonify({"error": ["validation errors"]}),406)
    

@app.delete('/events-blocked/<int:id>')
def delete_blocked_event(id):
    blocked_event = EventBlocked.query.filter(EventBlocked.id == id).first()

    if not blocked_event:
        return make_response(jsonify({"error": "Blocked event not found"}), 404)

    db.session.delete(blocked_event)
    db.session.commit()

    return make_response(jsonify({}), 204)

############################## bespoke routes #######################################
class UserEvents(Resource):
    def get(self, id):
        user = User.query.filter(User.id == id).first()
        if not user:
            return make_response(jsonify({"error": "user not found"}), 404)
        user_events = [e.to_dict() for e in Event.query.filter((id in [h.user_id for h in Event.hosts]) or (id in [g.user_id for g in Event.guests])).all()]
        return make_response(user_events, 200)
    
api.add_resource(UserEvents, '/users/<int:id>/events')

class AvailableEvents(Resource):
    def get(self, id):
        user = User.query.filter(User.id == id).first()
        if not user:
            return make_response(jsonify({"error": "user not found"}), 404)
        # the filter checks in order if the user is a host, a guest, or if the event is private
        available_events = [e for e in Event.query.filter(not (id in [h.user_id for h in Event.hosts] or (id in [g.user_id for g in Event.guests]) or (Event.private_party))).all()]
        # check if the user is blocked from any of the events and remove the event from the list if it is
        for event in available_events:
            if user in event.all_blocked():
                available_events.remove(event)
        return make_response(available_events, 200)

api.add_resource(AvailableEvents, 'users/<int:id>/available-events')

# put in an event id and get all the users who were blocked from that event either explicitly or because they were blocked from the host
class BlockedFromEvent(Resource):
    def get(self, id):
        event = Event.query.filter(Event.id == id).first()
        if not event:
            return make_response({"error": "event not found"}, 404)
        
        blocked_ids = [user.id for user in event.all_blocked()]

        return make_response(blocked_ids, 200)

api.add_resource(BlockedFromEvent, 'events/<int:id>/blocked-from-event')

# put in the users id and get the id of everyone who has blocked that user
class BlockedBy(Resource):
    def get(self, id):
        blocked_by_ids = [u.id for u in User.query.filter(id in [b.blockee.user_id for b in User.blockers]).all()]
        return make_response(blocked_by_ids, 200)
    
api.add_resource(BlockedBy, '/users/<int:id>/blocked-by')

# put in the users id and get back the ids of everyone who that user blocked
class BlockedUsers(Resource):
    def get(self, id):
        users_blocked_by = [u.id for u in User.query.filter(id in [b.blocker.user_id for b in User.blockees]).all()]
        return make_response(users_blocked_by, 200)
api.add_resource(BlockedUsers, '/users/<int:id>/blocked')
    
class BlockUser(Resource):
    def post(self, blocker_id, blockee_id):
        data = request.get_json()
        blocker_user = User.query.filter(User.id == blocker_id).first()
        blockee_user = User.query.filter(User.id == blockee_id).first()
        blocker_user.block(blockee_user)
        return make_response({"response": "user blocked"}, 201)
api.add_resource(BlockUser, '/users/<int:blocker_id>/block/<int:blockee_id>')
        



################################################## log in stuff #######################################
class Login(Resource):
    def post(self):
        data = request.get_json()
        username= data['username']
        password= data['password']
        user = User.query.filter(User.username == username).first()
        if user:
            if user.authenticate(password):
                session['user_id'] = user.id
                return user.to_dict(), 200
            else:
                return {"Error": "password is wrong"}, 401
        return {"Error": "User doesn't exist"}, 401

api.add_resource(Login, '/login')

class CheckSession(Resource):
    def get(self):
        user = User.query.filter(User.id == session.get('user_id')).first()
        if user:
            return user.to_dict(only=('username', 'id'))
        else:
            return {'message': 'Not Authorized'}, 401
        
api.add_resource(CheckSession, '/check_session')


class Logout(Resource):
    def delete(self):
        session['user_id'] = None
        return {}, 204
    
api.add_resource(Logout, '/logout')


            



if __name__ == '__main__':
    app.run(port=5555, debug=True)