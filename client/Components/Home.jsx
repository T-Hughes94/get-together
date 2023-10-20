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
      <h1 id="welcome-heading" className="main-heading">
        Welcome to Get Together!
      </h1>
      <p className="subtext">Discover and plan events with ease!</p>

      <h2 className="section-heading">Events</h2>
      <img src="URL HERE" alt="Event Image" className="event-image" />
      <ul className="event-list">
        {events.map((event) => (
          <li key={event.id} className="event-item">
            <img src="./assets/dogparty.jpg" alt="Event" className="event-item-image" />
            <h3 className="event-name">{event.name}</h3>
            <p className="event-info">Date: {event.date}</p>
            <p className="event-info">Location: {event.location}</p>
            <p className="event-description">{event.description}</p>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default Home;








