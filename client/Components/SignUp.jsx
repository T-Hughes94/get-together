
import React, { useState } from 'react';

function Signup({ history }) {
  const [name, setName] = useState('');
  const [dietaryRestrictions, setdietaryRestrictions] = useState('');
  const [password, setPassword] = useState('');
  const [profile_image, setprofile_image] = useState('https://i.natgeofe.com/n/548467d8-c5f1-4551-9f58-6817a8d2c45e/NationalGeographic_2572187_square.jpg')

  const handleInputChange = (event) => {
    const { name, value } = event.target;

    if (name === 'name') {
      setName(value);
    // } else if (name === 'DOB') {
    //   setDOB(value);
    } else if (name === 'dietaryRestrictions') {
      setdietaryRestrictions(value);
    } else if (name === 'password') {
      setPassword(value);
    } else if (name === 'profile_image') {
      setprofile_image(value);
    }  };

  const handleSignup = () => {
    // form validation
    if (!name || !password) {
      alert('Please enter a name and password.');
      return;password
    }
    console.log(JSON.stringify({ name, profile_image, dietaryRestrictions, password }))
    // POST request for new user account
    fetch('/api/users', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ name, profile_image, dietaryRestrictions, password }),
    })
    .then((response) => response.json())
    .then((data) => {
      if (data.ok) {
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
        {/* <div>
          <label htmlFor="DOB">Date of Birth:</label>
          <input
            type="date"
            id="DOB"
            name="DOB"
            value={DOB}
            onChange={handleInputChange}
          />
        </div> */}
        <div>
          <label htmlFor="dietaryRestrictions">Dietary Restrictions:</label>
          <input
            type="text"
            id="dietaryRestrictions"
            name="dietaryRestrictions"
            value={dietaryRestrictions}
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
        <div>
          <label htmlFor="profile_image">Image URL:</label>
          <input
            type="text"
            id="profile_image"
            name="profile_image"
            value={profile_image}
            onChange={handleInputChange}
          />
        </div>
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

