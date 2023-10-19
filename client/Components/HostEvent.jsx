// import React, { Component } from 'react';

// class HostEvent extends Component {
//   constructor(props) {
//     super(props);
//     this.state = {
//       eventTitle: '',
//       guestInvites: '',
//       eventDescription: '',
      
//     };
//   }

//   handleInputChange = (event) => {
//     const { name, value } = event.target;
//     this.setState({ [name]: value });
//   };

//   handleHostEvent = () => {
    
//     const { eventTitle, guestinvites, eventDescription } = this.state;


//     fetch('/api/host-event', {
//       method: 'POST',
//       headers: {
//         'Content-Type': 'application/json',
//       },
//       body: JSON.stringify({ eventTitle, guestinvites, eventDescription }),
//     })
//       .then((response) => response.json())
//       .then((data) => {
//         if (data.success) {
          
//           this.props.history.push(`/events/${data.eventId}`);
//         } else {
//           alert(data.message);
//         }
//       })
//       .catch((error) => {
//         console.error('Error:', error);
//       });
//   };
// //add class names to divs, etc, for Terence when he does the CSS.
//   render() {
//     return (
//       <div> 
//         <h1>Events I am Hosting</h1>
//         <form>
//           <div>
//             <label htmlFor="eventTitle">Event Title:</label>
//             <input
//               type="text"
//               id="eventTitle"
//               name="eventTitle"
//               value={this.state.eventTitle}
//               onChange={this.handleInputChange}
//             />
//           </div>
//           <div>
//             <label htmlFor="guestInvites">Guest Invites:</label>
//             <input
//               type="text"
//               id="guestInvites"
//               name="guestInvites"
//               value={this.state.eventLocation}
//               onChange={this.handleInputChange}
//             />
//           </div>
//           <div>
//             <label htmlFor="eventDescription">Event Description:</label>
//             <textarea
//               id="eventDescription"
//               name="eventDescription"
//               value={this.state.eventDescription}
//               onChange={this.handleInputChange}
//             />
//           </div>
//         </form>
//       </div>
//     );
//   }
// }

// export default HostEvent;




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
    const { eventTitle, guestInvites, eventDescription } = this.state;

    // Your fetch logic here
  };

  render() {
    return (
      <div>
        <h1>Events I am Hosting</h1>
        <form>
          <div>
            <label htmlFor="eventTitle">Event Title:</label>
            <select
              id="eventTitle"
              name="eventTitle"
              value={this.state.eventTitle}
              onChange={this.handleInputChange}
            >
              <option value="">Select an option</option>
              <option value="event1">Event 1</option>
              <option value="event2">Event 2</option>
              <option value="event3">Event 3</option>
            </select>
          </div>
          <div>
            <label htmlFor="guestInvites">Guest Invites:</label>
            <select
              id="guestInvites"
              name="guestInvites"
              value={this.state.guestInvites}
              onChange={this.handleInputChange}
            >
              <option value="">Select an option</option>
              <option value="option1">Option 1</option>
              <option value="option2">Option 2</option>
              <option value="option3">Option 3</option>
            </select>
          </div>
          <div>
            <label htmlFor="eventDescription">Event Description:</label>
            <select
              id="eventDescription"
              name="eventDescription"
              value={this.state.eventDescription}
              onChange={this.handleInputChange}
            >
              <option value="">Select an option</option>
              <option value="description1">Description 1</option>
              <option value="description2">Description 2</option>
              <option value="description3">Description 3</option>
            </select>
          </div>
        </form>
      </div>
    );
  }
}

export default HostEvent;
