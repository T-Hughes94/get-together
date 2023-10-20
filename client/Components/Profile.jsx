
import React, { useEffect, useState } from 'react';

function Profile() {
  const [hostedEvents, setHostedEvents] = useState([]);
  const [attendedEvents, setAttendedEvents] = useState([]);
  const [blockedUsers, setBlockedUsers] = useState([]);
  const [user, setUser] = useState({});

  useEffect(() => {
    // Fetch user's data
    fetch('/api/users/5') // Replace with the correct user ID or endpoint
      .then((response) => response.json())
      .then((userData) => {
        setUser(userData);

        // Fetch events hosted by the user
        fetch('/api/events') // Replace with the correct API endpoint
          .then((response) => response.json())
          .then((eventData) => {
            // Filter events hosted by the user
            const hostedEventsData = eventData.filter((event) =>
              userData.hosts.map((host) => host.event_id).includes(event.id)
            );
            setHostedEvents(hostedEventsData);
          })
          .catch((error) => {
            console.error('Error fetching hosted events:', error);
          });

        // Fetch events attended by the user
        fetch('/api/events') // Replace with the correct API endpoint
          .then((response) => response.json())
          .then((eventData) => {
            // Filter events attended by the user
            const attendedEventsData = eventData.filter((event) =>
              userData.guests.map((guest) => guest.event_id).includes(event.id)
            );
            setAttendedEvents(attendedEventsData);
          })
          .catch((error) => {
            console.error('Error fetching attended events:', error);
          });

        // Fetch blocked users
        fetch('/api/users/5/blocked-users') // Replace with the correct user ID or endpoint
          .then((response) => response.json())
          .then((blockedUsersData) => {
            setBlockedUsers(blockedUsersData);
          })
          .catch((error) => {
            console.error('Error fetching blocked users:', error);
          });
      })
      .catch((error) => {
        console.error('Error fetching user data:', error);
      });
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
        <p className="profile-email">Email: {user.email}</p>
      </div>

      <div className="profile-section">
        <h2>Events Hosted by {user.name}</h2>
        <ul className="profile-list">
          {hostedEvents.map((event) => (
            <li key={event.id}>{event.name}</li>
          ))}
        </ul>
      </div>

      <div className="profile-section">
        <h2>Events Attended by {user.name}</h2>
        <ul className="profile-list">
          {attendedEvents.map((event) => (
            <li key={event.id}>{event.name}</li>
          ))}
        </ul>
      </div>

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
