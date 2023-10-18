import React, { Component } from 'react';

class HostEvent extends Component {
  constructor(props) {
    super(props);
    this.state = {
      eventTitle: '',
      guestInvites: '',
      eventDescription: '',
      
    };
  }

  handleInputChange = (event) => {
    const { name, value } = event.target;
    this.setState({ [name]: value });
  };

  handleHostEvent = () => {
    
    const { eventTitle, guestinvites, eventDescription } = this.state;


    fetch('/api/host-event', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ eventTitle, guestinvites, eventDescription }),
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
        <h1>Events I am Hosting</h1>
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
            <label htmlFor="guestInvites">Guest Invites:</label>
            <input
              type="text"
              id="guestInvites"
              name="guestInvites"
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

export default HostEvent;
