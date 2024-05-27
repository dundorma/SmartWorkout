import React from 'react';
import { BrowserRouter as Router, Route } from 'react-router-dom';
import Header from './components/Header';
import Sidebar from './components/Sidebar';
import Footer from './components/Footer';
import Home from './pages/Home';
import Camera from './pages/Camera';
import Subscription from './pages/Subscription';
import Notifications from './pages/Notifications';
import Account from './pages/Account';
import SignIn from './pages/SignIn';
import LogIn from './pages/LogIn';
import './App.css';

function App() {
  return (
    <Router>
      <div className="App">
        <Header />
        <Sidebar />
        <div className="main-content">
          <Route path="/" exact component={Home} />
          <Route path="/camera" component={Camera} />
          <Route path="/subscription" component={Subscription} />
          <Route path="/notifications" component={Notifications} />
          <Route path="/account" component={Account} />
          <Route path="/signin" component={SignIn} />
          <Route path="/login" component={LogIn} />
        </div>
        <Footer />
      </div>
    </Router>
  );
}

export default App;


/*
import logo from './logo.svg';
import './App.css';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      </header>
    </div>
  );
}

export default App;
*/