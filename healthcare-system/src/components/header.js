import React from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';
import { Navbar } from 'react-bootstrap';

export default function Header(){
    return(
        <>
        <Navbar bg="dark" variant="dark">
          <Navbar.Brand href="#home">
            Healthcare System
          </Navbar.Brand>
        </Navbar>
      </>
    );
}