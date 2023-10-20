// import React from "react";
// import { BrowserRouter, Routes, Route, Link } from 'react-router-dom';
// import Home from "/Components/Home";
// import Login from "/Components/Login";
// import Profile from "/Components/Profile.jsx";
// import SignUp from "/Components/SignUp";
// import GuestEvent from "/Components/GuestEvent";
// import HostEvent from "/Components/HostEvent";

// function App() {
//   return (
//     <BrowserRouter>
//       <div>
//         <h1 className="navbar-title">
//           Get-Together
//         </h1>
//         <nav className="navbar navbar-expand-lg custom-navbar">
//           <ul className="navbar-nav mr-auto">
//             <li><Link to={'/'} className="nav-link">Home</Link></li>
//             <li><Link to={'/Login'} className="nav-link">Login</Link></li>
//             <li><Link to={'/Profile'} className="nav-link">Profile</Link></li>
//             <li><Link to={'/SignUp'} className="nav-link">SignUp</Link></li>
//             <li><Link to={'/GuestEvent'} className="nav-link">GuestEvent</Link></li>
//             <li><Link to={'/HostEvent'} className="nav-link">HostEvent</Link></li>
//           </ul>
//         </nav>
//         <hr />
//         <Routes>
//           <Route path='/' element={<Home />} />
//           <Route path='/Login' element={<Login />} />
//           <Route path='/Profile' element={<Profile />} />
//           <Route path='/SignUp' element={<SignUp />} />
//           <Route path='/GuestEvent' element={<GuestEvent />} />
//           <Route path='/HostEvent' element={<HostEvent />} />
//         </Routes>
//       </div>
//     </BrowserRouter>
//   );
// }

// export default App;



import React from "react";
import { BrowserRouter, Routes, Route, Link } from 'react-router-dom';
import Home from "/Components/Home";
import Login from "/Components/Login";
import Profile from "/Components/Profile.jsx";
import SignUp from "/Components/SignUp";
import Event from "/Components/Event"

function App() {
  return (
    <BrowserRouter>
      <div>
        <h1 className="navbar-title">
          Get-Together
        </h1>
        <nav className="navbar navbar-expand-lg custom-navbar">
          <ul className="navbar-nav mr-auto">
            <li><Link to={'/'} className="nav-link">Home</Link></li>
            <li><Link to={'/Login'} className="nav-link">Login</Link></li>
            <li><Link to={'/Profile'} className="nav-link">Profile</Link></li>
            <li><Link to={'/SignUp'} className="nav-link">SignUp</Link></li>
            <li><Link to={'/Event'} className="nav-link">Event</Link></li>
          </ul>
        </nav>
        <hr />
        <Routes>
          <Route path='/' element={<Home />} />
          <Route path='/Login' element={<Login />} />
          <Route path='/Profile' element={<Profile />} />
          <Route path='/SignUp' element={<SignUp />} />
          <Route path='/Event' element={<Event />} />
        </Routes>
      </div>
    </BrowserRouter>
  );
}

export default App