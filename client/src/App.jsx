import React from "react";
import { BrowserRouter, Routes, Route, Link } from 'react-router-dom';
import Home from "/Components/Home";
import Login from "/Components/Login";
import Profile from "/Components/Profile.jsx";
import SignUp from "/Components/SignUp";
import Event from "/Components/Event";
import './index.css';

function App() {
  return (
    <BrowserRouter>
      <div>
        <h1 className="navbar-title">Get-Together</h1>
        <nav className="navbar custom-navbar">
          <ul className="navbar-nav">
            <li className="nav-item"><Link to={'/'} className="nav-link">Home</Link></li>
            <li className="nav-item"><Link to={'/Login'} className="nav-link">Login</Link></li>
            <li className="nav-item"><Link to={'/Profile'} className="nav-link">Profile</Link></li>
            <li className="nav-item"><Link to={'/SignUp'} className="nav-link">SignUp</Link></li>
            <li className="nav-item"><Link to={'/Event'} className="nav-link">Event</Link></li>
          </ul>
          <Routes className="navbar-routes">
            <Route path='/' element={<Home />} />
            <Route path='/Login' element={<Login />} />
            <Route path='/Profile' element={<Profile />} />
            <Route path='/SignUp' element={<SignUp />} />
            <Route path='/Event' element={<Event />} />
          </Routes>
        </nav>
      </div>
    </BrowserRouter>
  );
}

export default App;









