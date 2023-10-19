import React, { Component } from 'react';


//without FETCH data to test the text fields.

class EventPage extends Component {
  constructor(props) {
    super(props);
    this.state = {
      eventTitle: '',
      Invites: '',
      eventDescription: '',
      events: [],
      userId: 'user123', // Replace with the actual user ID fetched from the backend
    };
  }

  handleInputChange = (event) => {
    const { name, value } = event.target;
    this.setState({ [name]: value });
  };

  render() {
    return (
      <div>
        <h1>Event Details</h1>
        <div>
          <label htmlFor="eventTitle">Event Title:</label>
          <input
            type="text"
            id="eventTitle"
            name="eventTitle"
            value={this.state.eventTitle}
            onChange={this.handleInputChange}
            readOnly = {true}
          />
        </div>
        <div>
          <label htmlFor="Invites">Guest Invites:</label>
          <input
            type="text"
            id="Invites"
            name="Invites"
            value={this.state.Invites}
            onChange={this.handleInputChange}
            readOnly = {true}
          />
        </div>
        <div>
          <label htmlFor="eventDescription">Event Description:</label>
          <textarea
            id="eventDescription"
            name="eventDescription"
            value={this.state.eventDescription}
            onChange={this.handleInputChange}
            readOnly = {true}
          />
        </div>
        {/* <button onClick={this.handleEventSubmit}></button> */}
      </div>
    );
  }
}

export default EventPage;


//WITH FETCH DATA

// import React, { Component } from 'react';

// class EventPage extends Component {
//   constructor(props) {
//     super(props);
//     this.state = {
//       eventTitle: '',
//       Invites: '',
//       eventDescription: '',
//       events: [],
//       userId: 'user123', // Replace with the actual user ID fetched from the backend
//     };
//   }

//   componentDidMount() {
//     fetch('/api/get-event-details')
//       .then((response) => response.json())
//       .then((data) => {
//         if (data.success) {
//           this.setState({
//             eventTitle: data.eventTitle,
//             Invites: data.invites,
//             eventDescription: data.eventDescription,
//           });
//         } else {
//           console.error('Error fetching event data:', data.message);
//         }
//       })
//       .catch((error) => {
//         console.error('Error:', error);
//       });
//   }

//   handleInputChange = (event) => {
//     const { name, value } = event.target;
//     this.setState({ [name]: value });
//   };

//   render() {
//     return (
//       <div>
//         <h1>Event Details</h1>
//         <div>
//           <label htmlFor="eventTitle">Event Title:</label>
//           <input
//             type="text"
//             id="eventTitle"
//             name="eventTitle"
//             value={this.state.eventTitle}
//             onChange={this.handleInputChange}
//             readOnly={true}
//           />
//         </div>
//         <div>
//           <label htmlFor="Invites">Guest Invites:</label>
//           <input
//             type="text"
//             id="Invites"
//             name="Invites"
//             value={this.state.Invites}
//             onChange={this.handleInputChange}
//             readOnly={true}
//           />
//         </div>
//         <div>
//           <label htmlFor="eventDescription">Event Description:</label>
//           <textarea
//             id="eventDescription"
//             name="eventDescription"
//             value={this.state.eventDescription}
//             onChange={this.handleInputChange}
//             readOnly={true}
//           />
//         </div>
//         <button onClick={this.handleEventSubmit}>Submit Event</button>
//       </div>
//     );
//   }
// }

// export default EventPage;
