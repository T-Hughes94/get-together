import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import React from "react";
import { createBrowserRouter, Route, createRoutesFromElements, RouterProvider, Link } from "react-router-dom";
import Home from "../Components/Home";
import Login from "../Components/Login";
import Profile from "../Components/Profile";
import SignUp from "../Components/SignUp"
import GuestEvent from "../Components/GuestEvent"
import HostEvent from "../Components/HostEvent"



function App()  {
  const router=createBrowserRouter(
    createRoutesFromElements(
      <Route>
        
      </Route>

    )
  )
  return (
    <BrowserRouter>
    <Router>
      <div>

      <h1 className="navbar-title">
      Get-Together
        <img
          src="."
           className="navbar-image"
           style={{ width: '150px', height: '200px', borderRadius: '1%'  }}
        />
      </h1> 
      
        
        
        <nav className="navbar navbar-expand-lg custom-navbar">
        <ul className="navbar-nav mr-auto">

         <ul><Link to={'/'} className="nav-link"> Home </Link></ul>

         <ul><Link to={'/Login'} className="nav-link">Login</Link></ul>

         <ul><Link to={'/Profile'} className="nav-link">Profile</Link></ul>

         <ul><Link to={'/SignUp'} className="nav-link">SignUp</Link></ul>

         <ul><Link to={'/GuestEvent'} className="nav-link">GuestEvent</Link></ul>

         <ul><Link to-={'/HostEvent'} className="nav-link">HostEvent</Link></ul>

        </ul>

        
      </nav>
        
        <hr />
        <Routes>
            <Route exact path='/' element={<Home />} />
            <Route path='/Login' element={<Login />} />
            <Route path='/Profile' element={<Profile />} />
            <Route path='/SignUp' element={<SignUp />}/>
            <Route path='/GuestEvent' element={<GuestEvent />}/>
            <Route path='/HostEvent' element={<HostEvent />}/>

        </Routes>
      </div>
    </Router>
    </BrowserRouter>
  );
}

export default App
