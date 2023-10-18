
import React, { useState } from 'react';

function Signup({ history }) {
  const [name, setName] = useState('');
  const [DOB, setDOB] = useState('');
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');

  const handleInputChange = (event) => {
    const { name, value } = event.target;

    if (name === 'name') {
      setName(value);
    } else if (name === 'DOB') {
      setDOB(value);
    } else if (name === 'email') {
      setEmail(value);
    } else if (name === 'password') {
      setPassword(value);
    }
  };

  const handleSignup = () => {
    // form validation
    if (!name || !DOB || !email || !password) {
      alert('Please fill in all fields.');
      return;
    }

    // POST request for new user account
    fetch('/api/signup', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ name, DOB, email, password }),
    })
      .then((response) => response.json())
      .then((data) => {
        if (data.success) {
          // Handle successful signup, redirect to login page
          history.push('/login');
        } else {
          // Handle signup error
          alert(data.message);
        }
      })
      .catch((error) => {
        console.error('Error:', error);
        // Handle network or other errors
        alert('An error occurred. Please try again.');
      });
  };

  return (
    <div>
      <h1>Sign Up</h1>
      <form>
        <div>
          <label htmlFor="name">Name:</label>
          <input
            type="text"
            id="name"
            name="name"
            value={name}
            onChange={handleInputChange}
          />
        </div>
        <div>
          <label htmlFor="DOB">Date of Birth:</label>
          <input
            type="date"
            id="DOB"
            name="DOB"
            value={DOB}
            onChange={handleInputChange}
          />
        </div>
        <div>
          <label htmlFor="email">Email:</label>
          <input
            type="email"
            id="email"
            name="email"
            value={email}
            onChange={handleInputChange}
          />
        </div>
        <div>
          <label htmlFor="password">Password:</label>
          <input
            type="password"
            id="password"
            name="password"
            value={password}
            onChange={handleInputChange}
          />
        </div>
        <div>
          <button type="button" onClick={handleSignup}>
            Sign Up
          </button>
        </div>
      </form>
    </div>
  );
}

export default Signup;

