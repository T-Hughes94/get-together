#!/usr/bin/env python3

# Standard library imports

# Remote library imports
from flask import request, session, make_response, jsonify
from flask_restful import Resource

# Local imports
from config import app, db, api
# Add your model imports
from models import User, Event, Host, Guest, Invite, EventBlocked, UserBlocked


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
@app.get('/events/ <int:id>')
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

        


############################## post delete for host ##############################

# bespoke routes
class UserEvents(Resource):
    
    def get(self, id):
        user_events = [e.to_dict() for e in Event.query.filter((id in [h.user_id for h in Event.hosts]) or (id in [g.user_id for g in Event.guests])).all()]
        return make_response(user_events, 200)
    
api.add_resource(UserEvents, '/user-events/<int:id>')

class AvailableEvents(Resource):

    def get(self, id):
        # need to add user blocked
        # add event not private
        available_events = [e.to_dict() for e in Event.query.filter(not (id in [h.user_id for h in Event.hosts] or (id in [g.user_id for g in Event.guests]) or (id in [b.user_id for b in Event.event_blocked]) or ())).all()]
        return make_response(available_events, 200)

api.add_resource(AvailableEvents, '/available-events/<int:id>')

class BlockedFromEvent(Resource):
    def get(self, id):
        event_blocked_ids = [b.user_id for b in EventBlocked.query.filter(EventBlocked.event_id == id)]
        user_blocked_ids = [b.blockee_id for b in UserBlocked.query.filter(UserBlocked.blocker_id in [h.user_id for h in Host.query.filter(Host.event_id == id)])]
        blocked_ids = list(set(event_blocked_ids + user_blocked_ids))
        return make_response(blocked_ids, 200)

api.add_resource(BlockedFromEvent, '/blocked-from-event/<int:id>')

# log in shit
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