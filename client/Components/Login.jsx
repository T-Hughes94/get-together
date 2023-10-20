import React, { useState } from 'react';

const Login = () => {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState('');

  const handleLogin = async () => {
    if (!username || !password) {
      setError('Please fill in both username and password fields.');
      return;
    }

    try {
      const response = await fetch('http://127.0.0.1:5555', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ username, password }),
      });

      if (response.ok) {
        const user = await response.json();
        console.log('Logged in as:', user.name);
        localStorage.setItem('user', JSON.stringify(user)); // Corrected 'Json,stringify' to 'JSON.stringify'
      } else {
        setError('Login failed');
      }
    } catch (error) {
      setError('Error: ' + error.message);
    }
  };

  const handleLogout = () => {
    localStorage.removeItem('user');
  };

  const isUserLoggedIn = !!localStorage.getItem('user');

  return (
    <div className="login-container">
      <h2 className="login-title">Login</h2>
      <form className="login-form">
        <div>
          <label htmlFor="username">Username</label>
          <input
            type="text"
            id="username"
            className="login-input"
            value={username}
            onChange={(e) => {
              setUsername(e.target.value);
              console.log(username);
            }}
          />
        </div>
        <div>
          <label htmlFor="password">Password</label>
          <input
            type="password"
            id="password"
            className="login-input"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
          />
        </div>
        {error && <p className="error-message" style={{ color: 'red' }}>{error}</p>}
        <button className="login-button" type="button" onClick={handleLogin}>
          Login
        </button>
      </form>
    </div>
  );
};

export default Login;


