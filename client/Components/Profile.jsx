
import React, { useEffect, useState } from 'react';

function Profile() {
  const [userEvents, setUserEvents] = useState([]);
  const [attendedEvents, setAttendedEvents] = useState([]);
  const [blockedUsers, setBlockedUsers] = useState([]);
  const [user, setUser] = useState({});

  useEffect(() => {
    // check who the user is
    fetch('api/check_session')
    .then(r=>r.json())
    // .then(r=>console.log(r))
    // // Fetch user's data
    // .then(fetch('/api/users/5')) // Replace with the correct user ID or endpoint
    //   .then((response) => response.json())
    .then((userData) => {
      setUser(userData);
      // fetch(`api/users/${userData.id}/events`)
      fetch(`api/users/${userData.id}/events`)
      .then(r=>r.json())
      .then((events)=>{
        setUserEvents(events)
        console.log(events)
      })
    })
    .catch((error) => {
      console.error('Error fetching user data:', error);
    })
  }, []);

  return (
    <div className="profile-container">
      <div className="profile-header">
        <img
          src={user.profile_image}
          alt="User Profile Image"
          className="profile-image"
        />
        <h1 className="profile-username">{user.name}</h1>
        <p className="profile-email">{user.dietary_restrictions}</p>
      </div>

      <div className="profile-section">
        <h2>My Events</h2>
        <ul className="event-list">
          {userEvents.map((event) => (
            <li key={event.id} className="event-item">
              <img src={event.image} alt="Event" className="event-item-image" />
              <h3 className="event-name">{event.title}</h3>
              {/* <p className="event-info">Date: {event.date}</p> */}
              {/* <p className="event-info">Location: {event.dat}</p> */}
              <p className="event-description">{event.description}</p>
            </li>))}
          </ul>
      </div>

      {/* <div className="profile-section">
        <h2>Events Attended by {user.name}</h2>
        <ul className="profile-list">
          {attendedEvents.map((event) => (
            <li key={event.id}>{event.name}</li>
          ))}
        </ul>
      </div> */}

      <div className="profile-section">
        <h2>Blocked Users</h2>
        <ul className="profile-list">
          {blockedUsers.map((blockedUser) => (
            <li key={blockedUser.id}>{blockedUser.username}</li>
          ))}
        </ul>
      </div>
    </div>
  );
}

export default Profile
