import React, { useEffect, useState } from 'react';


function Profile({ user }) {
  const [hostedEvents, setHostedEvents] = useState([]);
  const [attendedEvents, setAttendedEvents] = useState([]);
  const [blockedUsers, setBlockedUsers] = useState([]);

  useEffect(() => {

    //fetch user's events, hosted and attending
    fetch(`/api/users/${user.id}/hosted-events`)
      .then((response) => response.json())
      .then((data) => {
        setHostedEvents(data);
      })
      .catch((error) => {
        console.error('Error fetching hosted events:', error);
      });

    fetch(`/api/users/${user.id}/attended-events`)
      .then((response) => response.json())
      .then((data) => {
        setAttendedEvents(data);
      })
      .catch((error) => {
        console.error('Error fetching attended events:', error);
      });

    // fetch blocked users
    fetch(`/api/users/${user.id}/blocked-users`)
      .then((response) => response.json())
      .then((data) => {
        setBlockedUsers(data);
      })
      .catch((error) => {
        console.error('Error fetching blocked users:', error);
      });
  }, [user.id]);

  return (
    <div>
      <h1>{user.username}'s Profile</h1>
      <img src="IMAGE HERE" alt="User Profile Image" />
      <p>Email: {user.email}</p>
      
      <h2>Events I Am Hosting</h2>
      <ul>
        {hostedEvents.map((event) => (
          <li key={event.id}>{event.name}</li>
        ))}
      </ul>

      <h2>Events I Am Attending</h2>
      <ul>
        {attendedEvents.map((event) => (
          <li key={event.id}>{event.name}</li>
        ))}
      </ul>

      <h2>Users I Have Blocked</h2>
      <ul>
        {blockedUsers.map((blockedUser) => (
          <li key={blockedUser.id}>{blockedUser.username}</li>
        ))}
      </ul>
    </div>
  );
}

export default Profile;
