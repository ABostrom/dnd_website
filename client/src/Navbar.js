import React from 'react';
import {Container, Button, Navbar, Nav, Form, FormControl, NavDropdown} from 'react-bootstrap'

import {AppName} from './App';
import {GetSpellsByName} from './Spell'

class MainNavBar extends React.Component{
    handleSpellNameClick(){
        console.log("handleSpellNameClick")

        GetSpellsByName();
    }

    handleSpellClassClick(){
        console.log("handleSpellClassClick")
    }

    handleSpellSchoolClick(){
        console.log("handleSpellSchoolClick");
    }

    render(){
        return(
        <Container>
            <Navbar bg="dark" variant="dark" expand="lg">
                <Navbar.Brand href="#home">{AppName}</Navbar.Brand>
                <Navbar.Toggle aria-controls="basic-navbar-nav" />
                <Navbar.Collapse id="basic-navbar-nav">
                <Nav className="mr-auto">
                    <Nav.Link href="#home">Home</Nav.Link>
                    <Nav.Link href="#link">Link</Nav.Link>
                    <NavDropdown title="Spells" id="basic-nav-dropdown">
                    <NavDropdown.Item href="#action/3.1" onClick={this.handleSpellNameClick}>Spells By Name</NavDropdown.Item>
                    <NavDropdown.Item href="#action/3.2" onClick={this.handleSpellClassClick}>Spells By Class</NavDropdown.Item>
                    <NavDropdown.Item href="#action/3.3" onClick={this.handleSpellSchoolClick}>Spells By School</NavDropdown.Item>
                    </NavDropdown>
                </Nav>
                <Form inline>
                    <FormControl type="text" placeholder="Search" className="mr-sm-2" />
                    <Button variant="outline-success">Search</Button>
                </Form>
                </Navbar.Collapse>
            </Navbar>
        </Container>
        );
    }

}


export default MainNavBar;