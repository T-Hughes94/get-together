import React, { useState, useEffect } from 'react';

function Home() {
  const [events, setEvents] = useState([]);

  useEffect(() => {
    fetch('/api/events')
      .then((response) => response.json())
      .then((data) => {
        setEvents(data);
      })
      .catch((error) => {
        console.error('Error:', error);
      });
  }, []);

  return (
    <div>
      <h1>Welcome to Get Together!</h1>
      <p>Discover and plan events with ease!</p>

      <h2>Events</h2>
      <img src='URL HERE' />
      <ul>
        {events.map((event) => (
          <li key={event.id}>
            <img src="./assets/dogparty.jpg" alt="Event" />
            <h3>{event.name}</h3>
            <p>Date: {event.date}</p>
            <p>Location: {event.location}</p>
            <p>{event.description}</p>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default Home;

