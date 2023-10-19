import React, { useState, useEffect, Component } from 'react';

class GuestEvent extends Component {
  constructor(props) {
    super(props);
    this.state = {
      eventTitle: '',
      Invites: '',
      eventDescription: '',
      
    };
  }

  handleInputChange = (event) => {
    const { name, value } = event.target;
    this.setState({ [name]: value });
  };

  handleGuestEvent = () => {
    
    const { eventTitle, Invites, eventDescription } = this.state;


    fetch('/api/guest-event', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ eventTitle,Invites, eventDescription }),
    })
      .then((response) => response.json())
      .then((data) => {
        if (data.success) {
          
          this.props.history.push(`/events/${data.eventId}`);
        } else {
          alert(data.message);
        }
      })
      .catch((error) => {
        console.error('Error:', error);
      });
  };
//add class names to divs, etc, for Terence when he does the CSS.
  render() {
    return (
      <div> 
        <h1>Events I am Attending</h1>
        <form>
          <div>
            <label htmlFor="eventTitle">Event Title:</label>
            <input
              type="text"
              id="eventTitle"
              name="eventTitle"
              value={this.state.eventTitle}
              onChange={this.handleInputChange}
            />
          </div>
          <div>
            <label htmlFor="Invites">Guest Invites:</label>
            <input
              type="text"
              id="Invites"
              name="Invites"
              value={this.state.eventLocation}
              onChange={this.handleInputChange}
            />
          </div>
          <div>
            <label htmlFor="eventDescription">Event Description:</label>
            <textarea
              id="eventDescription"
              name="eventDescription"
              value={this.state.eventDescription}
              onChange={this.handleInputChange}
            />
          </div>
        </form>
      </div>
    );
  }
}

export default GuestEvent;




