import React from 'react';
import { NavLink } from 'react-router-dom';
import '../styles/Sidebar.css';

const Sidebar = () => {
  return (
    <div className="sidebar">
      <nav>
        <ul>
          <li><NavLink to="/" exact>Home</NavLink></li>
          <li><NavLink to="/camera">Camera</NavLink></li>
          <li><NavLink to="/subscription">Subscription</NavLink></li>
          <li><NavLink to="/notifications">Notifications</NavLink></li>
          <li><NavLink to="/account">Account</NavLink></li>
        </ul>
      </nav>
    </div>
  );
};

export default Sidebar;
