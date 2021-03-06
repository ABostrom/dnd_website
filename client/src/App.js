import React from 'react';
import logo from './logo.svg';
import './App.css';
import 'bootstrap/dist/css/bootstrap.min.css';
import MainNavBar from './Navbar'
import { Container } from 'react-bootstrap';


const AppName = "DnD Website";

function App() {
  return (
    <div className="App">
      <MainNavBar/>
      

      <div className="contents" id="contents">
        <Container>
          Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
          Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. 
          Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. 
          Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
        </Container>
      </div>
    </div>
  );
  }

export default App;

export {
  AppName,
}
